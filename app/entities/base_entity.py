from ..support.database.db import Database


class BaseEntity:
    table_name = ''
    schema = 'dim_db'
    database = Database('')
    fields = []

    def find_by_id(self, id):
        query = 'SELECT * FROM ' + self.get_relation_name() + ' WHERE id = ' + str(id)

        return self._execute(query)

    def create(self, payload: dict):
        query = 'INSERT INTO ' + self.get_relation_name() + self.build_field_set(
            payload.keys()) + ' VALUES ' + self.build_field_set(payload.items())

        return self._execute(query)

    def get_relation_name(self):
        return self.schema + '.' + self.table_name

    def _execute(self, query):
        print('>>> executing: ' + query)

        cur = self.database.getCursor()
        cur.execute(query)

        return cur.fetchall()

    def build_field_set(self, fields: list[str]):
        conc_fields = ', '.join(fields)

        return '(' + conc_fields + ')'
