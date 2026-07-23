import mysql.connector

#conn create
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Diksha@123",
    database="linkkcode"
)
print("database connected!")

cursor = conn.cursor()
cursor.execute("""
    create table if not exists emp(
        empid int primary key auto_increment,
        name varchar(20) not null
    )
""")

conn.commit()  # important to save
conn.close()
print("Table created")