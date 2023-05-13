#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    #Create cursor object
    cursor = db.cursor()

    #Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #Fetch all rows
    rows = cursor.fetchall()

    #Print the rows
    for row in rows:
        print(row)

    #Close cursor and database connection
    cursor.close()
    db.close()
