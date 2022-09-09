from ..support.database.db import Database


class BaseEntity:
    table_name = ''
    schema = 'dim_db'
    database = Database('')

    def find_by_id(self, id):
        query = 'SELECT * FROM ' + self.schema + '.' + self.table_name + ' WHERE id = ' + str(id)

        return self._execute(query)

    def _execute(self, query):
        print('>>> executing:')
        print(query)
        cur = self.database.getCursor()
        cur.execute(query)

        return cur.fetchall()
