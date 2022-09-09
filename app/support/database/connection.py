import psycopg2

try:
    conn = psycopg2.connect("dbname='dim_db' user='postgres' host='db' password='password'")
    cur = conn.cursor()
except OSError as err:
    print(err)
except:
    print("Unable to connect to the database")
