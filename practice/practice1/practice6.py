##GCD of Two Numbers without any built in function
def gcd(n1,n2):
   while(n2!=0):
       n1,n2=n2,n1%n2
   return n1
        
number1=int(input("enter the first number:"))
number2=int(input("enter the second number:"))
gcd_result=gcd(number1,number2)
print(gcd_result)