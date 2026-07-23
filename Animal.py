class Animal:
    type="animaltype"

    def __init__(self):
        print("parent constructor")

    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def xyz(self):
        print("hello im from parent class")    

    def greet(self):
        print("hello im animal")    

    