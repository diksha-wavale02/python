import sqlite3
conn=sqlite3.connect("student.db")
cursor=conn.cursor()
#table creation
cursor.execute('''
    create table if not exists stud(
               sid integer primary key,
               name  text not null,
               age integer null)
               ''')
print("created!")
#insert 
# cursor.execute("insert into stud(sid ,name,age) values (?,?,?)",(5,"samiksha","19"))
# conn.commit()
# print("data inserted!")
#insert
sid=int(input("enter id"))
sname=input("enter name:")
age=int(input("enter yr age:"))
cursor.execute("insert into stud(sid ,name,age) values (?,?,?)",(sid,sname,age))
conn.commit()
print("data inserted!")


# cursor.execute("select * from stud")
# rows=cursor.fetchall()
# print(rows)
# for r in rows:
#     print(f"{r[0]}")


#single
#sid=int(input("enter id:"))
#cursor.execute("select * from stud where sid=?",(sid,))
#row=cursor.fetchone()
#print(row)


#delete
# sid=int(input("enter id to be deleted:"))
# cursor.execute("delete from stud where sid=?",(sid,))
# print("successfully deleted")
# conn.commit()



#update
# sid=int(input("enter id:"))
# cursor.execute("select * from stud where sid=?",(sid,))
# row=cursor.fetchone()
# print(row)
# if sid==row[0]:
#     newname=input("enter new name\n")
#     cursor.execute("update stud  set name=? where sid=?",(newname,sid))
#     conn.commit()
#     print("data updated!")
# else:
#     print("no record found")    

# cursor.execute("select name from ")    


