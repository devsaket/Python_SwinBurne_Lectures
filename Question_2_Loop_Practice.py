# Question 2(a) : Find the sum of first 10 natural numbers
# To display first natural numbers , we will use concept of Loops
# In Loop we use concept of range, which includes : Start, Stop and Step


print(range(1,11,1))
      
s=0 # Intializing any variable before start of the loop with value equal to 0
a= int(input("enter lower range = "))
b = int(input("Enter upper range = "))
for i in range(a,b+1,1):  # Declaration of FOR loop 
      print(i,end=" ")   # Making sure of intendation and printing numbers 
      s = s+i
else:
      print("\n")

print("Sum of these first 10 natural numbers is  : " ,s)
