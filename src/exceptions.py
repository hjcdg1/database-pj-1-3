class DuplicateColumnDefError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: column definition is duplicated')


class DuplicatePrimaryKeyDefError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: primary key definition is duplicated')


class ReferenceTypeError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: foreign key references wrong type')


class ReferenceNonPrimaryKeyError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: foreign key references non primary key column')


class ReferenceColumnExistenceError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: foreign key references non existing column')


class ReferenceTableExistenceError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: foreign key references non existing table')


class NonExistingColumnDefError(Exception):
    def __init__(self, column_name):
        super().__init__(f'Create table has failed: \'{column_name}\' does not exist in column definition')


class TableExistenceError(Exception):
    def __init__(self):
        super().__init__('Create table has failed: table with the same name already exists')


class CharLengthError(Exception):
    def __init__(self):
        super().__init__('Char length should be over 0')


class NoSuchTable(Exception):
    def __init__(self):
        super().__init__('No such table')


class DropReferencedTableError(Exception):
    def __init__(self, table_name):
        super().__init__(f'Drop table has failed: \'{table_name}\' is referenced by other table')


class SelectTableExistenceError(Exception):
    def __init__(self, table_name):
        super().__init__(f'Selection has failed: \'{table_name}\' does not exist')


class InsertTypeMismatchError(Exception):
    def __init__(self):
        super().__init__('Insertion has failed: Types are not matched')


class InsertColumnExistenceError(Exception):
    def __init__(self, column_name):
        super().__init__(f'Insertion has failed: \'{column_name}\' does not exist')


class InsertColumnNonNullableError(Exception):
    def __init__(self, column_name):
        super().__init__(f'Insertion has failed: \'{column_name}\' is not nullable')


class SelectColumnResolveError(Exception):
    def __init__(self, column_name):
        super().__init__(f'Selection has failed: fail to resolve \'{column_name}\'')


class WhereIncomparableError(Exception):
    def __init__(self):
        super().__init__('Where clause trying to compare incomparable values')


class WhereTableNotSpecified(Exception):
    def __init__(self):
        super().__init__('Where clause trying to reference tables which are not specified')


class WhereColumnNotExist(Exception):
    def __init__(self):
        super().__init__('Where clause trying to reference non existing column')


class WhereAmbiguousReference(Exception):
    def __init__(self):
        super().__init__('Where clause contains ambiguous reference')


class EtcError(Exception):
    def __init__(self):
        super().__init__('Etc error')
