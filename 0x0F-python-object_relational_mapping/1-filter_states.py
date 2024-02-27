#!/usr/bin/python3

"""
Script to list all states from the database hbtn_0e_0_usa.
This script takes 3 arguments: mysql username, mysql password, and database nme
It uses the MySQLdb module to connect to a MySQL server running port 3306.
Results are sorted in ascending order by states.id.
Results are displayed as they are in the example below.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    List all states from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Name of the database containing the states.

    Returns:
        None
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
