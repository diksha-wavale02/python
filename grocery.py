from dmart import dmart
class grocery(dmart):
    def __init__(self,category,product_name,qty,price,brand_name,mfg,exp):       
        super().__init__(category,product_name,qty,price)
        self.brand_name=brand_name
        self.mfg=mfg
        self.exp=exp


    def display_grocery_details(self):
        print(super().display_store_details())
        print(super().common_features())
        return f"brand_name{self.brand_name}\n mfg{self.mfg}\nexp{self.exp}"    
g=grocery("grocery","sugar",200,100,"sugarelite","2026-06-01","2027-06-01")   
    