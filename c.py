from A import A

class C(A):
    def __init__(self,qty):
        print("from c")
        super().__init__(3000)
        self.qty=qty