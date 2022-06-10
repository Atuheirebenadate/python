
from curses import ALL_MOUSE_EVENTS


class Account:
    my_bank="stanbic"
    def __init__(self,name,id,account_number,):
        self.name=name
        self.id=id
        self.account_number=account_number
        self.balance=0
        self.deposits =[]
        self.withdrawals = []
        self.transaction = 100
        


    def deposit(self,amount):
         self.balance+=amount
         if amount < 0:
              return f"Deposit amount must be greater than zero"
         else:
            self.balance+=amount
            self.deposits.append(f"hello {self.name}, you have dposited{amount}")   
            return f"Hello you have deposited{amount} and your account balance is {self.balance}"   
    def withdraw(self,amount):
            self.balance -= amount
            if amount > self.balance: 
                return f"insufficient balance"
            elif amount <=0:
                return f"widraw amount must be greater than zero"
            else:
                self.account_number-=amount+self.transaction
                self.withdrawals.append(f"Hello {self.name}, you have withdrawn {amount}")
                return f"Hello{self.name} your have withdrawn{amount} your new balance{self.balance}"
    def deposits_statement(self):
        for statement in self.deposits:
            print (statement)
    def withdrawals_statement(self):
        for statement in self.withdrawals:
         print(statement)
    def current_balance(self): 
        balance = self.balance
        print(balance)    

    
         

    
              
            
        
                
    

        
        
        

    
    


    