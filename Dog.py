from Animal import Animal 
class Dog(Animal):
   
    def __init__(self):
        print("child constructor!")

    def __init__(self,name,weight,colour):
        self.colour=colour
        super().__init__(name,weight)  

    
    def abc(self):
        print("hello im child class") 

    def dog_details(self):
        super().greet()
        print(f"{self.name}{self.colour}")

        
obj=Dog("lab","7kg","black")
#