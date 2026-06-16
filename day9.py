#different variables
'''globalvar="hey"
class demo:

    pass
    msg="hello"
    
    def __init__(self,age):
        self.name="xyz"
        self.age=age
        print(self.name,self.age)    
    def __del__(self):
        print('deleted') 
    def access_globalvar(self):
        print(globalvar)
        local_var=90
        print(local_var)
    @staticmethod
    def greet(name,objref):
       return f"hello gm{name}{demo.msg}{objref.age}!"           
obj=demo(20) 
print(obj.msg)
print(globalvar) 
obj.access_globalvar()    
print(obj.greet("sita",obj))
'''
#inheritence

class car:
    #instant var
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display_car(self):
        return f"{self.name}{self.price}"  
#class engine:
    #instant var
        
car_obj=car("BMW","2cr")
car_obj.display_car()      



