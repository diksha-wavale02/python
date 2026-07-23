from A import A
class B(A):

    def __init__(self,age):
        self.age=age
        print("from B")
        super().__init__("sita")
        