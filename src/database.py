import json


class DatabaseManager:
    ENCODING = 'UTF-8'

    def __init__(self, database):
        self.database = database

    def get_table_names(self):
        return list(map(lambda key: key.decode(self.ENCODING), self.database.keys()))

    def get_table(self, table_name):
        return json.loads(self.database.get(table_name.encode(self.ENCODING)).decode(self.ENCODING))

    def set_table(self, table_name, data):
        self.database.put(table_name.encode(self.ENCODING), json.dumps(data).encode(self.ENCODING))

    def delete_table(self, table_name):
        self.database.delete(table_name.encode(self.ENCODING))
