## Line Equation
def calculate_y(slope, intercept, x):
    return (slope*x)+intercept
slope=float(input("enter the slop:"))
intercept=float(input("enter the intercept:"))
x=float(input("enter the value of x"))
print("the value of y is:",calculate_y(slope,intercept,x))