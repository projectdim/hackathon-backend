import psycopg2

try:
    conn = psycopg2.connect("dbname='dim_db' user='postgres' host='db' password='password'")
    cur = conn.cursor()
except OSError as err:
    print(err)
    print("I am unable to connect to the database")
except:
    print("I am unable to connect to the database")




# try:
#     cur.execute('SELECT * from dim_db.events')
# except:
#     print("I can't SELECT from events")
#
# rows = cur.fetchall()
# print("\nRows: \n")
# for row in rows:
#     print("   ", row[1])

