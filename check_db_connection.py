#import mysql.connector
import pymysql.cursors

connection = pymysql.connect(host = "127.0.0.1",
                                     database = "addressbook",
                                     user = "root",
                                     password = "")

try:
    cursor = connection.cursor()
    cursor.execute("select id, firstname, lastname from addressbook  where deprecated='0000-00-00 00:00:00'")
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()