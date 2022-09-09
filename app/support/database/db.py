from .connection import conn
import psycopg2
import psycopg2.extras


class Database:
    schema = 'dim_db'
    conn = conn

    def __init__(self, table):
        self.table = table

    def getCursor(self):
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    # def execute(self, query):
    #     self.cur.execute(query)
    #     return self.cur.fetchall()

    def find_by_id(self, id):
        self.cur.execute('SELECT * FROM ' + self.schema + '.' + self.table + ' WHERE id = ' + str(id))
        return self.cur.fetchall()

    def createQueryBuilder(self, table):
        return Query(table)


class Query:
    table = None
    cur = None

    def __init__(self, cur, table):
        self.table = table
        self.cur = cur

    def execute(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def find_by_id(self, id):
        self.cur.execute('SELECT * FROM ' + schema + '.' + self.table + ' WHERE id = ' + str(id))
        return self.cur.fetchall()
