import atexit

from berkeleydb import db
from lark import Lark, exceptions

from src.executor import SQLExecutor
from src.literals import PROMPT_TEXT


def read_query_input():
    # Read a query input from user, which can be multi-lines or multi-queries
    query_input_lines = []
    while True:
        query_input_line = input().strip()
        query_input_lines.append(query_input_line)

        # Stop reading lines for current input, when encountering semicolon character at the end of the line
        if query_input_line.endswith(';'):
            break

    # Concatenate each line of the input with whitespace character, resulting in a cleaned query input
    return ' '.join(query_input_lines)


def parse_query_input(parser, executor, query_input):
    # Split the query input into multiple queries, where each query ends with semicolon character
    query_list = map(lambda query: query + ';', query_input[:-1].split(';'))

    # For each query
    for query in query_list:
        # Parse the query, and make a tree representing the parsed result as hierarchical nodes
        try:
            tree = parser.parse(query)

        # When parsing failed, print `Syntax error` and skip the remaining queries
        except exceptions.UnexpectedInput:
            print(f'{PROMPT_TEXT}> Syntax error')
            break

        # When parsing is successful, validate and execute the query
        try:
            executor.execute(tree)

        # When the query is invalid, print the error message
        except exceptions.VisitError as e:
            print(f'{PROMPT_TEXT}> {e.orig_exc}')


def cleanup():
    # Reclaim memory resources before terminating this process
    database.close()
    grammar.close()


# Register a cleanup function, which will be called when this process is terminated
atexit.register(cleanup)

# Open the database stored in local file system (Create if no database exists)
database = db.DB()
database.open('myDB.db', dbtype=db.DB_HASH, flags=db.DB_CREATE)

# Instantiate a SQL parser from a lark file, which defines the grammar for parsing SQL
grammar = open('grammar.lark')
parser = Lark(grammar.read(), start='command', lexer='basic')

# Instantiate a SQL executor for handling each type of query
executor = SQLExecutor(database)

# Keep reading query inputs from user, before encountering `EXIT` query
while True:
    # Prompt for a query input
    print(f'{PROMPT_TEXT}>', end=' ')

    # Read a query input from user
    query_input = read_query_input()

    # Parse the query input, and execute the queries
    parse_query_input(parser, executor, query_input)
