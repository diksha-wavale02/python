
#function
#without argument
def greet():
    print("hello")
greet()

def cube(n):
    print(n**3)
num=int(input("Enter a number:"))

cube(num) 

#with argument without return type

def add(a,b):
    return a+b
print(add(70,80))

print(add(8.6,7.2))

#exception 

print("start")
try:
    a=int(input("enter first no:"))
    b=int(input("enter second no: "))
    print(a/b)
except ValueError as e:
    print(e)   

def add(num1,num2):
    print(num1+num2)

try:
    num1=int(input("enter 1st no:"))
    num2=int(input("enter 2nd no:"))
    add(num1,num2)
except ValueError:
    print("enter no only") 
except Exception as a:
    print(a)    

print("------")          



class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("ram",20)
print(s1.name)
s2=student("sita",20)
 
class stud:
    c_name="xyz"
    @classmethod
    def change_c_name(cls):
        return "class method"
    @classmethod
    def change_c_name(cls,new_value):
        return f"updated value is{cls.c_name}"

print(stud.change_c_name())
print(stud.change_c_name1("linkcode"))





