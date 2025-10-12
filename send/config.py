import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",       # Change if your MySQL user is different
        password="",       # Add your MySQL password if set
        database="deep"
    )
