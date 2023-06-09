# Question 8 Write a program in python to display the n terms of odd natural number and their sum
# To solve this question, we can use concept of For or while loop

#a = int(input(" Enter the number of Terms : ")) 
#print(a) # Whatever terms we choose,there will be half of even and odd terms

   
    
# Solving this question with While Loop

s=0
i=0
a = int(input("Enter the number of terms : " ))
while i<a*2:
    if i%2 !=0:
        print(i)
        s =s+i
    i= i+1

print("\n The total sum is " , s)

