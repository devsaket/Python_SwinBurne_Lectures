p = float(input("Enter principal amount = "))
r = float(input("Enter rate of interest = "))
t = float(input("Enter time period = "))
s= p*r*t/100
print("Simple interest = ",s)

total = p + s
print("Total amount = ",total)