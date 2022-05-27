class Account:
    my_bank="stanbic"
    def __init__(self,name,id,account_number,balance):
        self.name=name
        self.id=id
        self.account_number=account_number
        self.balance=balance

    def withdraw(self,amount):
            self.amount=amount
            self.balance-=self.amount
            return self.balance
    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        return self.balance
                
    

        
        
        

    
    


    