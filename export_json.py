import json
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
data = {}


def json_output():
    for table in TABLES:
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]
        for row in cur:
            rows.append(dict(zip(fields, row)))
            data[table] = rows
    with open('Files/all_data.json', 'w') as outf:
        json.dump(data, outf, default=str)


json_output()