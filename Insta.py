import random
class insta:
    def __init__(self,name,username,pwd,otp):
        self.name=name
        self.username=username
        self.__pwd=pwd
        self.__otp=None
        
    
    def verify_otp(self,u_otp):
        
        if self.__otp==u_otp :
            print("otp matched!")
        else:
            print("ivalid otp!!") 

    #login

    def login(self,username,pwd):
        if self.username==username and self.__pwd==pwd:
            print("login successfully")
            self.__otp=random.randint(1000,9999)
            print("otp send to yr registered mobile no",self.__otp)
            u_otp=int(input("enter yr otp"))
            self.verify_otp(u_otp)
        else:
            print("invalid creditials")           




obj=insta("ram","ram@123",1234,7890)
obj.login("ram@123",1234)
