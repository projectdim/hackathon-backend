import logging
from time import sleep

import psycopg2

from config.local import config

schema = config['database']
log = logging.getLogger(__name__)
tries = 0
max_tries = 5
sleep_time = 5

while tries < 5:
    try:
        # conn = psycopg2.connect("dbname='dim_db' user='postgres' host='db' password='password'")
        conn = psycopg2.connect(user=config['user'],
                                password=config['password'],
                                host=config['host'],
                                port=config['port'],
                                database=config['database']
                                )

        cur = conn.cursor()
    except OSError as err:
        print(err)
    except Exception as e:
        print(e)
        print("Unable to connect to the database")
    else:
        break

    log.error("Failed, sleeping...")
    tries += 1
    sleep(sleep_time)
