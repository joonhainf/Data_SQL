import psycopg2
psycopg2.__version__

import pandas as pd
import csv

#I need to specify the database I have, so this is my current setup
database = {'user': 'postgres',
'pass': 'book',
'name': 'postgres',
'host': 'localhost',
'port': '5432'}

#See if this works or not
try:
    pgConnectString = f"""host={database['host']}
    port={database['port']}
    dbname={database['name']}
    user={database['user']}
    password={database['pass']}"""

except ImportError:
    print("psycopg2 module is not installed. Please install it using 'pip install psycopg2'.")

except Exception as e:
    print("An error occurred while connecting to the PostgreSQL database:", e)

#Now use a connection and cursor
conn=psycopg2.connect(pgConnectString)
cur = conn.cursor()


#Open the csv file a row at a time and insert 10000 of them into the cursor

with open('C:/Users/joonh/Downloads/Data_SQL/rows.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader) 
    limit = 10000 
    rows_to_insert = [row for _, row in zip(range(limit), reader)]
    cur.executemany('INSERT INTO austin_crime VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', rows_to_insert)

#Commit changes, comment out if you want to keep database as is
conn.commit()


#cur.execute('SELECT * FROM austin_crime')
cur.execute("SELECT * FROM austin_crime WHERE family_violence = 'Y' AND occurred_date BETWEEN DATE '2019-01-01' AND DATE '2020-01-01'")
records = cur.fetchall()



#for record in records:
#    print(record)


cur.close()
conn.close()

records[1:10]
