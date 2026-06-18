from Bank import Bank
class Account(Bank):
    def __init__(self,bankname,ifsc_code,account_no,ahname):
        super().__init__(bankname,ifsc_code)
        self.account_no=account_no
        self.ahname=ahname

    
    def display_account(self):
        super().display_bank()
        return f"{self.account_no}\n{self.ahname}"

