#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa in ascending order by states.id
"""
import MySQLdb
import sys

def list_all_states(username, password, database_name):
    
    try:
        db_conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=database_name
                charset="utf8"
                )
        cursor = db_conn.cursor()

        query = "SELECT * FROM states ORDER BY id ASC"
        
        cursor.execute(query)

        states = cursor.fetchall()

        for state in states:
            print(state)

            cursor.close()
            db_conn.close()

        except MySQLdb.Error as e:
            print("MySQL Error: {}".format(e))
            sys.exit(1)

        if __name__ == "__main__":
            if len(sys.argv) != 4:
                print("Usage: {sys.argv[0]} <mysql_username> <mysql_password> <database_name>")
                sys.exit(1)

        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        list_all_states(username, password, database_name)
