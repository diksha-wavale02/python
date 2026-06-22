from p1 import p1
from p2 import p2
class c(p1,p2):
    def pqr(self):
        print("i'm from child class")

    def call_p2_show(self):
        return p2.show(self) 
    
    def __init__(self,name,age):
        print("c constructor")
        p1.__init__(self,name)
        p2.__init__(self,age)


obj=c("ram",20)
'''
obj.xyz()
obj.abc()
obj.pqr
obj.show()
obj.call_p2_show()   
'''    