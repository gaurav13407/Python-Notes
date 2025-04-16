##Distance covered by a Vehicle
def distance(speed,time):
    return speed*time

speed=float(input("enter the speed of the car:"))
time=float(input("enter the time:"))
print("the distance covered by car is:",distance(speed,time))