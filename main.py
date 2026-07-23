from clothes import clothes
from grocery import grocery

c=clothes("clothes","jeans",200,799,"black","M")
g=grocery("grocery","sugar",200,100,"sugarelite","2026-06-01","2027-06-01")
orders=[]

while True:
    print("welcome to dmart!\n1.Grocery section\n2.clothig section\n3.purchase\n4.exit")
    choice=int(input("Eneter your choice:\n"))
    match choice:
        case 1:
            print(g.display_grocery_details())
        case 2:
            print(c.display_clothes_deatils())
        case 3:
            print("purches")
            print("choice\n1.Grocery\n2.clothes\n3.total bill\n4.exit")
            ip=int(input("enter your choice!"))
            match ip:
                case 1:
                    if ip==1:
                        qty=int(input("enter Qty:"))
                        total=g.price*qty
                        orders.append([g.product_name,qty,g.price,total])
                case 2:
                        
                    if ip==2:
                        qty=int(input("enter qty:"))
                        total=c.price*qty
                        orders.append([c.product_name,qty,c.price,total])  
                        
                case 3:        
                    print("you whant to generate your bill")    
                    for items in orders[3]:
                        for j in items:
                            print(sum(items))
                        totalbill=total
                        print(totalbill)
                case 4:
                    print("exit")
                    break;
                case _:
                    print("invalid choice")          
        case 4:
            print("thank you")
            break;
        case _:
             print("invalid choice")   