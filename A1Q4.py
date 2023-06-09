##

# Task 4


# float data type will be preffered choice as amount and interest is involved

# Making user input the amount
a = float(input("Enter the amount = "))


# Variable declaration "t" for time
t = float(input("Enter the time (in years) = "))

# Formula to calculate the balance
if t==0:
    s=a
elif  t >=0 and t<5:
    i=1.5
    s = a*((1+ i/t)**t)
elif t>=5 and t<7:
    i=1.5
    s = a*((1+ i/t)**t)
elif t>=7:
    i =2
    s = a*((1+ i/t)**t)


print(f"Total amount = {s}")
