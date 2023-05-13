#!/usr/bin/python3
"""Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    #script arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    #connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=db_name,
        charset="utf8")

    #SELECT query to get cities of the given state
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    #execute query
    cursor = db.cursor()
    cursor.execute(query, (state_name,))

    #print results
    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    #close cursor and database connection
    cursor.close()
    db.close()
