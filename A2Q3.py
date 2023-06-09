#STUDENT ID : 20925390, First Name: Sahil, Last Name: Sharma


#Question 3 :
#prompting the user to enter numbers of rows, using concept of exception handling
#for pattern given in the question


try:

#prompting the user to enter the number of rows to print the number of rows
#By using "input" function  
    a = int(input("Enter number of rows = "))
    
#Using for loop for "i" with in specified range
    for i in range(0,a):
        for j in range(i,-1,-1):
            print(2**j, end= "   ")

#Printing the pattern if valid for valid input by the user

        print(" ")


except ValueError:    
#Using exception handling if user inputs characters instead of numbers

    print("You must input a number not the characters")




