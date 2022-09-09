from ..support.database.db import Database


def to_string(item):
    return str(item)


def build_field_set(fields: list[any]):
    fields = map(to_string, fields)
    print(fields)
    conc_fields = ', '.join(fields)

    return '(' + conc_fields + ')'


class BaseEntity:
    table_name = ''
    database = Database()
    fields = []

    def find_by_id(self, id):
        query = 'SELECT * FROM ' + self.get_relation_name() + ' WHERE id = ' + str(id)

        return self._executeQuery(query)

    def find_all(self, limit=100):
        query = 'SELECT * FROM ' + self.get_relation_name()

        if limit:
            query = query + ' LIMIT ' + limit

        return self._executeQuery(query)

    def check_field_exists(self, field):
        if field not in self.fields:
            raise Exception('Field ' + field + 'is not in the field list')

    def create(self, payload: dict):
        map(
            self.check_field_exists,
            payload.keys()
        )

        query = 'INSERT INTO ' \
                + self.get_relation_name() \
                + build_field_set(payload.keys()) \
                + ' VALUES ' \
                + build_field_set(payload.values())

        return self._executeUpdate(query)

    def get_relation_name(self):
        return self.database.schema + '.' + self.table_name

    def _executeQuery(self, query):
        print('>>> executing: ' + query)

        cur = self.database.getCursor()
        cur.execute(query)

        return cur.fetchall()

    def _executeUpdate(self, query):
        print('>>> executing: ' + query)

        cur = self.database.getCursor()
        cur.execute(query)

        self.database.getCursor().execute(query)
        return self.database.conn.commit()
