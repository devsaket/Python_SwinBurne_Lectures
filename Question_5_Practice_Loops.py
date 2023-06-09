#Question 5:  Write a program in C to display the cube of the number upto given an integer.
#To solve this we have to use concept of Loop : For or While


a=int(input("Enter the number of terms for cube root value :" ))
print(a)

for i in range(1,a+1):
    cube = i**3
    print("\n The number is  : ",i, " The cube of this number is : ", cube)
    
    
