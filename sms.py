import sqlite3
conn=sqlite3.connect("student.db")
cursor=conn.cursor()
#table creation
cursor.execute('''
    create table if not exists stud1(
               roll integer primary key,
               name  text not null,
               sub1 integer not null,
               sub2 integer not null,
               sub3 integer not null,
               sub4 integer not null,
               sub5 integer not null)
               ''')
print("created!")
# ch=int(input("eneter yr choice:"))
# match ch:
#     case 1:
#         insert()
        
#     case 2:
#         update()
#     case 3:
#         delete()        


#insert


roll=int(input("enter roll no:"))
sname=input("enter name:")
sub1=int(input("enter yr sub1 marks:"))
sub2=int(input("enter yr sub2 marks:"))
sub3=int(input("enter yr sub3 marks:"))
sub4=int(input("enter yr sub4 marks:"))
sub5=int(input("enter yr sub5 marks:"))
cursor.execute("insert into stud1(roll ,name,sub1,sub2,sub3,sub4,sub5) values (?,?,?,?,?,?,?)",(roll,sname,sub1,sub2,sub3,sub4,sub5))
conn.commit()
print("data inserted!")

# def update():
# #update
# #update by roll no
#     sid=int(input("enter roll:"))
#     cursor.execute("select * from stud1 where roll=?",(roll,))
#     row=cursor.fetchone()
#     print(row)
#     if roll==row[0]:
#         newname=input("enter new name\n")
#         cursor.execute("update stud1  set name=? where roll=?",(newname,roll))
#         conn.commit()
#         print("data updated!")
#     else:
#         print("no record found")    
# #update by name
# cursor.execute("select sname from where sname=? ",(sname,))   

# row=cursor.fetchone()
# print(row)
# if sname==row[0]:
#     newname=input("enter new name:")
#     cursor.execute("update stud1 set name=? where sname=?",(newname,roll))
#     conn.commit()
#     print("data updated")
# else:
#     print("no record found")


# # view
# cursor.execute("select * from stud1")
