"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2

# connect to db
conn = psycopg2.connect(host='localhost', database='test', user='postgres', password='0707')
try:
    with conn:

        with conn.cursor() as cur:
            # execute query
            cur.execute('INSERT INTO user_account VALUES (%s, %s)', (6, 'Jake'))

            cur.execute('SELECT * FROM user_account')
            rows = cur.fetchall()
            for row in rows:
                print(row)

finally:
    conn.close()
