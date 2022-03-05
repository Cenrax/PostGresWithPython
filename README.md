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

***Note: For Rest of this blog I will consider the user name as Cenrax and the database name as dq***

```
import psycopg2
conn = psycopg2.connect("dbname=dq user=Cenrax")
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

Let now see an important difference in Postgres as compared to SQlLite:
If you were to inspect the dq database now, you would notice that there actually isn't a table named users in it. This isn't a bug (First time users may assume it) — it's because of a concept called ***SQL transactions***. In short, Postgres uses transactions to ensure data consistency. This groups the queries together and only saves changes when explicitly requested to do so. This contrasts with SQLite, where every query we made that modified the data immediately changed the database. We will study this in more detail on the following screens.

Let's verify what I have written in the previous paragraph.

```
import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
cur.execute("SELECT * FROM users;")
```
<img width="438" alt="image" src="https://user-images.githubusercontent.com/43017632/156875172-9d73f7b7-5c93-48f4-8684-f618e319f27a.png">

You will get an error like this.

So let's see in details why this is happening:

With Postgres, we're dealing with multiple users who could be changing the database at the same time with a remote connection to a server that could fail at any moment. In order to see why this can be a problem, imagine we're keeping track of accounts for different customers at a bank.

We have the following two rows in the table named accounts:

| id | Name | Balance |
| ------ | ------ |
| 1 | Ram | 400 |
| 2 | Cenrax | 8000 |
| 3 | Rosy | 8779 |
