from C import C
from B import B
class D(B,C):
    def __init__(self,price):
        self.price=price
        
        print("from c")
        super().__init__("20")

obj=D(5)
print("age=",obj.age)
print("name=",obj.name)
print("price=",obj.price)
print("qty=",obj.qty)