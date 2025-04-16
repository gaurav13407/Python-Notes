## Bank Account System

class BANKACCOUNT:
    def __init__(self,owner,balance=0):
       self.owner=owner
       self.balance=balance
       
    def Deposite(self,amount):
           self.balance+=amount
           print(f"{amount}has been depoisted in your account and current balance is{self.balance}")
           
    def withdraw(self,amount):
        if(amount>self.balance):
            print("insufficiant balance")
        else :
            self.balance-=amount
            print(f"{amount} has been withdrawn form your account and your balance is{self.balance}")
            
    def transfer(self,recipent_account,amount):
        if(amount>self.balance):
            print("Insufficiant Balance")
        else:
            self.balance-=amount
            recipent_account.Deposite
            (amount)
            print(f"Transferred ${amount} to {recipent_account.owner}.")
            print(f"Your new balance: ${self.balance}")
    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"
            
    
    def get_balance(self):
        print(self.balance)


Account1=BANKACCOUNT("Gaurav",5000)    
Account2=BANKACCOUNT("Aditiya",3000)
print(Account1.balance)  
print(Account2.balance) 
Account1.Deposite(200)
Account2.Deposite(500)   
Account1.transfer(Account2,1500)
         
