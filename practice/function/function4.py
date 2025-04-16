##Number of Rounds of Lift
def round(total,capacity):
    return total/capacity

total=int(input("total number of people:"))
capacity=int(input("capacity is:"))
print("how many rounds it takes:",round(total,capacity))