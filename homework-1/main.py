"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import os
import csv

CSV_DATA = os.path.join('north_data')


def csv_to_postgres(csv_data, csv_file, table_name):
    try:
        with psycopg2.connect(
                host="localhost",
                database="north",
                user="postgres",
                password="0707"
        ) as conn:
            with conn.cursor() as cur:

                with open(f"{csv_data}/{csv_file}", 'r') as file:
                    reader = csv.reader(file)
                    next(reader)  # Пропускаем заголовки

                    for row in reader:
                        # Вставляем данные в таблицу
                        insert_query = f"INSERT INTO {table_name} VALUES ({', '.join(['%s'] * len(row))})"
                        cur.execute(insert_query, row)
                        conn.commit()

                cur.execute(f"SELECT * FROM {table_name}")
                rows = cur.fetchall()

                for row in rows:
                    # Распечатываем таблицу в консоли
                    print(row)
    finally:
        conn.close()


if __name__ == '__main__':
    csv_to_postgres(CSV_DATA, 'customers_data.csv', 'customers')
    csv_to_postgres(CSV_DATA, 'employees_data.csv', 'employees')
    csv_to_postgres(CSV_DATA, 'orders_data.csv', 'orders')
