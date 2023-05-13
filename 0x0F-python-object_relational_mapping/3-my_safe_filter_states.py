#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injections!
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    # Create a cursor object
    cursor = db.cursor()
    # Execute the query (with placeholder)
    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
                   (argv[4],))
    # Fetch all the rows as a tuple of tuples
    rows = cursor.fetchall()
    # Print the rows
    for row in rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
