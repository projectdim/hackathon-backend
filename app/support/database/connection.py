# todo make env dependent config

from config.local import config
import psycopg2
schema = config['database']

try:
    # conn = psycopg2.connect("dbname='dim_db' user='postgres' host='db' password='password'")
    print(config)

    conn = psycopg2.connect(user=config['user'],
                            password=config['password'],
                            host=config['host'],
                            port=config['port'],
                            database=config['database']
                            )

    cur = conn.cursor()
except OSError as err:
    print(err)
except:
    print("Unable to connect to the database")
