import ac_tools
import m245
# make sure that all connections are closed
ac_tools.close_connections(globals())
# delete users table to avoid conflicts with the one students need to create
m245.delete_users_table("dbname=dq user=dq")
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
query_string = """
    CREATE TABLE users(
        id integer PRIMARY KEY, 
        email text,
        name text,
        address text
    );
"""

cur = conn.cursor()
cur.execute(query_string)
conn.commit()
conn.close()
