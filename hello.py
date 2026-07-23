try:
    file=open("Myfile.txt","x")
    print(file)
except Exception as e:
    print(e)
#add
with open("Myfile.txt","w") as f:
    f.write("hello ")
    print("data added")     

#read 
#with open("Myfile.txt","r")as f:
#    data=f.read()
#    print(data)
# append
with open("Myfile.txt","a")as f:
    f.write("world")   
