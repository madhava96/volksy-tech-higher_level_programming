#!/usr/bin/python3


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(username=sys.argv[1], password=sys.argv[2], database name=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(states) for states in c.fetchall()]
