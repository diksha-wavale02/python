class payment:
    def pay(self):
        pass
    print("payment process started....!")
    
class upi(payment):
    def pay(self):
        return "payment done by upi"

class gpay(payment):
    def pay(self):
        return "payment done by gpay"
        
class payment_module :
    def payment_process(self,obj):
        print(obj.pay())
        
        



print("payment")
print("1.upi 2.gpay 3.card 4.exit")
choice=int(input("eneter yr choice:"))

match choice:
    case 1:
        obj=upi()
        #print( obj.pay())
    case 2:
        obj=gpay()
        #print( obj.pay())
    case 3:
        pass
    case 4:
        print("exit")
    case _:
        print("invalid choice")
p=payment_module()
p.payment_process(obj)

#multiple object
obj=[upi(),gpay()]
for i in obj:
    print(i.pay())
        
        
        
    