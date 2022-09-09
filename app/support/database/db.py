from app.support.database.connection import conn, schema
import psycopg2
import psycopg2.extras


class Database:
    conn = conn

    def getCursor(self):
        return self.conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    def createQueryBuilder(self):
        return Query()


class Query:
    cur = None
    conn = None

    def __init__(self):
        self.cur = Database().getCursor()
        self.conn = conn

    def select(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def modify(self, query):
        self.cur.execute(query)
        return self.conn.commit()
