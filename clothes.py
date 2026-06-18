from dmart import dmart
class clothes(dmart):
    def __init__(self,category,product_name,qty,price,colour,size):
        super().__init__(category,product_name,qty,price)
        self.colour=colour
        self.size=size

    def display_clothes_deatils(self):
        print(super().display_store_deatils())    
        print(super().common_features())
        return f"colour:{self.colour}\nsize:{self.size} "
    
c=clothes("clothes","jeans",200,799,"black","M")
    