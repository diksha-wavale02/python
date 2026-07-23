class Bank:
    def __init__(self,bankname,ifsc_code):
        self.bankname=bankname
        self.ifsc_code=ifsc_code
    def display_bank(self):
        return f"{self.bankname}\n{self.ifsc_code}"

