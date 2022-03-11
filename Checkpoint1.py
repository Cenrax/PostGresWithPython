'''
We've provided some code on the left that you need to complete. We've created two connections conn1 and conn2 for the same user. We've given you four instructions that will demonstrate that without committing, two connections can have different views of the database.

    Using cur1, execute the query SELECT * FROM users; and assign the result of fetching all rows resulting from this query to a variable named view1_before.
    Perform the same steps with cur2. That is, using cur2, execute the query SELECT * FROM users;, and assign the result of fetching all rows resulting from this query to a variable named view2_before.
    Commit the first connection conn1.
    Perform the same query again with cur2, and assign the result to a variable named view2_after.
    Run the code, and inspect the values of the variables. What do you observe?

'''
import psycopg2
conn1 = psycopg2.connect("dbname=dq user=dq")
cur1 = conn1.cursor()
cur1.execute("INSERT INTO users VALUES (%s, %s, %s, %s);", (1, 'alice@dataquest.io', 'Alice', '99 Fake Street'))
conn2 = psycopg2.connect("dbname=dq user=dq")
cur2 = conn2.cursor()
# add your code here
# step 1
cur1.execute("SELECT * FROM users;")
view1_before = cur1.fetchall()
# step 2
cur2.execute("SELECT * FROM users;")
view2_before = cur2.fetchall()
# step 3
conn1.commit()
# step 4
cur2.execute("SELECT * FROM users;")
view2_after = cur2.fetchall()
