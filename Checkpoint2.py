#the dataset is there in this repo
import psycopg2
import csv
conn = psycopg2.connect("dbname=dq user=cenrax")
cur = conn.cursor()
with open('user_accounts.csv', 'r') as file:
    next(file) # skip csv header
    reader = csv.reader(file)
    for row in reader:
        cur.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", row)
        
conn.commit()
conn.close()
