class account:
    def __init__(self,bal):
        self.__bal=bal

    def get_bal(self):
        return self.__bal  

    def set_bal(self,amt):
        self.__bal=amt
        print("bal updated!")

    def __private_method(self):
        return "hello i'm private!"

    def access_pm(self):
        return self.__private_method()    

    def __withdeawl_method(self,amt,bal):
        if bal<=amt:
            self.amt=amt
            self.bal=bal
            new_amt=bal-amt

            print(new_amt) 
        else:
            print("insufficient balnace!")    

    def access_wm(self):
        return self.__withdeawl_method(500,1000)   

    def __debit_method(self,amt,bal):
        self.amt=amt
        self.bal=bal
        if amt>0:
            new_amt=bal+amt
            print("debited successfully!")
            print(new_amt)
           

    def access_dm(self):
        return self.__debit_method(3000,500)    


obj=account(500)
print(obj.get_bal())    
print(obj.set_bal(300)) 
print(obj.access_pm()) 
print(obj.access_wm())
print(obj.access_dm())