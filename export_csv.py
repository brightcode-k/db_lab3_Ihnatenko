import csv
import psycopg2

username = 'Ihnatenko_Nikolai'
password = 'Kolya'
database = 'Nikolai_DB'
host = 'localhost'
port = '5432'

OUTPUT_FILE = 'Nikolai_DB_{}.csv'

TABLES = [
    'scoring',
    'students',
    'gender',
]

conn = psycopg2.connect(user=username, password=password, dbname=database)
cur = conn.cursor()


def csv_output():
    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])


csv_output()