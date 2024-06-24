#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa in ascending order by states.id
"""
import MySQLdb
import sys

def list_all_states(username, password, database_name):

    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database_name
                )
        cursor = db.cursor()

        query = 'SELECT * FROM states ORDER BY id ASC'
        
        cursor.execte(query)

        states = cursor.fetchall()

        for state in states:
            print(state)

            cursor.close()
            db.close()

        except MySQLdb.Error as e:
            print('MySQL Error {}: {}'.format(e.args[0], e.args[1]))
            sys.exit(1)

        if __name__ == '__main__':
            if len(sys.argv) != 4:
                print('Usage: {} <username> <password> <database_name>'.format(sys.argv[0]))
                sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database_name = sys.argv[3]

        list_all_states(username, password, database_name)
