from Account import Account
class Saving_account(Account):
    def __init__(self, bankname, ifsc_code, account_no, ahname,bal):
        super().__init__(bankname, ifsc_code, account_no, ahname)
        self.bal=bal

    def display_Saving_account(self):
        super().display_account()
        return f"{self.bal}"    
    
obj=Saving_account("bank of india","123456","345677","diksha","3000")    