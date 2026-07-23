import mysql.connector
#conn create
conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Diksha@123",
    database="d1"
)
print("database connected!")