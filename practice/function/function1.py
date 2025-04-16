## Create a function to convert temperature from celcius to Fahrenheit
def celcius(C):
    return C*(9/5)+32
C=float(input("Enter the Temperature:"))
print(celcius(C))
