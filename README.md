# PostGresWithPython

## Basic Points:

In order to communicate with our Postgres server, we will be using the open source psycopg2 Python library. You can think of psycopg2 as similar to connecting to a SQLite database using the sqlite3 library. Because Postgres supports multiple simultaneous connections, Postgres uses multiple users and databases to improve security and the division of data. Without those values, Postgres won't know who is trying to connect and where, so it will fail.

#### To connect to Postgres we use the following
```
import psycopg2
conn = psycopg2.connect("dbname=databaseName user=userName")
```
The connection object allows the client to interact with the database server until it is closed. To issue commands to the database, you will also need to create a cursor object by calling the connection.cursor() method. This object is the one that we will use to execute our commands. However, whenever you close the connection, you won't be able to issue any additional commands with that connection's cursor.

To execute commands on the Postgres database, you call the cursor.execute() method with a SQL query passed as a string. We often refer to this string as a query string. The **cursor.execute()** method doesn't return the query results right away. It will return None if the query was successful; otherwise, it will return an error otherwise. After executing a query, we can use the cursor object to iterate over all results using a for loop like this:

** Note: For Rest of this blog I will consider the user name as Cenrax and the database name as postgress **

```
import psycopg2
conn = psycopg2.connect("dbname=postgres user=Cenrax")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
for row in cur:
    print(row)
```
Alternatively, we can get the returned value — or values — by calling one of the two methods: **cursor.fetchone()** or **cursor.fetchall()**. The cursor.fetchone() method returns the first result or None if there are no results. On the other hand, the cursor.fetchall() method returns a list containing each row from the result or an empty list [] if there are no rows matching the query.

```
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
all_results = cur.fetchall()
```
Till now we have assumed the table user is created already. Now **we will see how do we create a table in Postgres**

```
import psycopg2
conn = psycopg2.connect("dbname=dq user=Cenrax")
cur = conn.cursor()
cur.execute(
"""
    CREATE TABLE users (
        id integer PRIMARY KEY, 
        email text, 
        name text, 
        address text
    );
""")

```
Now we have created our user table. The commands are almost similar to SQL but sometimes the command may differ so I would encourage please go through the documentation if you are facing an error. I have specified the column names along with their datatypes.
