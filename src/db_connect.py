import time
import random
import os

from sqlalchemy import create_engine

POSTGRES_HOST = os.getenv('POSTGRES_HOST') or 'localhost'
POSTGRES_USER = os.getenv('POSTGRES_USER') or 'postgres'
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD') or 'my_pass'
POSTGRES_PORT = os.getenv('POSTGRES_PORT') or '5432'
POSTGRES_DB = os.getenv('POSTGRES_DB') or 'my_pg_database'

# POSTGRES_USER ='postgres'
# POSTGRES_PASSWORD ='my_pass'
# POSTGRES_PORT = '5432'
# POSTGRES_DB ='my_pg_database'

def get_last_row():
    query = 'SELECT number FROM numbers WHERE timestamp >= (SELECT max(timestamp) FROM numbers) LIMIT 1'
    with engine.connect() as connection:
        result = connection.execute(query)
        print(f'result: {result}')
        for row in result:
            output = row[0]
            print(f'row[0]: {row[0]}')
    return output


def add_new_row(n):
    # Insert a new number into the 'numbers' table.
    query = f'INSERT INTO numbers (number,timestamp) VALUES ({n},{int(round(time.time() * 1000))});'
    print(f'Inserting value: {n}')
    engine.execute(query)


if __name__ == '__main__':
    engine = create_engine(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')
        # db = psycopg2.connect(host='postgres', port=5432, user='postgres',
        #                       password='123', dbname='chatbotdev')
    engine.connect()
    print(engine)

    engine.execute('CREATE TABLE IF NOT EXISTS numbers ( number BIGINT, timestamp BIGINT);')
    add_new_row(random.randint(1,100000))
    time.sleep(5)
    print(f'The last value insterted is: {get_last_row()}')
    time.sleep(5)
