
##Calculator

class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def add(self):
        return self.num1+self.num2
        
    def subtract(self):
        return self.num1-self.num2
        
    def multiply(self):
       return self.num1*self.num2
    def divide(self):
        if(self.num2==0):
            print("cant divide by zero")
        else :
            return self.num1/self.num2
            
            
calculator=Calculator(2,3)
print(calculator.add)
print(calculator.subtract)
print(calculator.multiply)
print(calculator.divide)