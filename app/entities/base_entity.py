from ..support.database.db import Database


class BaseEntity:
    table_name = ''
    schema = 'dim_db'
    database = Database('')

    def find_by_id(self, id):
        cur = self.database.getCursor()
        cur.execute('SELECT * FROM ' + self.schema + '.' + self.table_name + ' WHERE id = ' + str(id))

        return cur.fetchall()
