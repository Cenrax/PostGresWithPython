# PostGresWithPython

## Basic Points:

In order to communicate with our Postgres server, we will be using the open source psycopg2 Python library. You can think of psycopg2 as similar to connecting to a SQLite database using the sqlite3 library. Because Postgres supports multiple simultaneous connections, Postgres uses multiple users and databases to improve security and the division of data. Without those values, Postgres won't know who is trying to connect and where, so it will fail.

#### To connect to Postgres we use the following
```
import psycopg2
conn = psycopg2.connect("dbname=databaseName user=userName")
```
