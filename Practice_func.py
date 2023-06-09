# To calculate the balanace by using interest and time

# If time is not equal to zero


def bal(a,t):
    i=3
    result = a*((1+ i/t)**t)
    return result
   

a = float(input(" Enter the amount"))

t = float(input(" enter th time in years = "))
# i = float (input("ENter rate of interest = "))

#s = a*((1+ i/t)**t)

x = bal(a,t)
print(f"Total amount = {x} ")
