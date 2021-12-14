import psycopg2
import csv

username = 'Ihnatenko_Nikolai'
password = 'Kolya'
database = 'Nikolai_DB'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'Files/StudentsPerformance.csv'

query_0 = '''
CREATE TABLE StudentsPerformance_copy
(
    gender   	   VARCHAR(8)	NOT NULL,
    parental_level_of_education    VARCHAR(50)	NOT NULL,
    test_preparation_course     VARCHAR(50)	NOT NULL,
    math_score INT NOT NULL,
    reading_score INT NOT NULL,
    writing_score INT NOT NULL
);
'''

query_1 = '''
DROP TABLE IF EXISTS StudentsPerformance_copy
'''

query_2 = '''
INSERT INTO StudentsPerformance_copy (gender, parental_level_of_education, test_preparation_course, math_score, reading_score, writing_score) 
VALUES (%s, %s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_1)
    cur.execute(query_0)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for row in reader:
            values = (row['gender'], row['parental level of education'],
                      row['test preparation course'], row['math score'],
                      row['reading score'], row['writing score'])
            cur.execute(query_2 , values)

    conn.commit()