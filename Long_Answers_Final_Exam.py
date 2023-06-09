#Q1(a)
## Write a program that asks the user to enter the volume (a float) and the height of a can.
## The program then calculates and displays the radius of the can.
## Note: The volume v of can with diameter d and height h is given by:

##import math
##
##Vol = float(input("Enter the volume of Can: "))
##Ht = float(input("Enter the height of Can: "))
##
##d = math.sqrt((4*Vol)/(Ht * math.pi))
##print("The diameter of can is : ",d)
##
##r = d/2
##r = format(r,".2f")
##print("The radius of the given Can is : ",r)
##

#Q1(b)

# a = input("Enter the time :") #17:10
# li = a.split(':')
# print(li)
# s =int(li[0])*60 + int(li[1])
# print(s)



#Q1(c) Write a program that reads two times in 24-hour format
#(where the first time is earlier than the second one).
#The program then computes and prints the number of hours and minutes between the two times.
# import datetime
# a = input("Enter the start time :")
# b = input("Enter the end time :")
# li = a.split(':')
# li1 = b.split(':')
# c = datetime.timedelta(hours= int(li[0]) ,minutes= int(li[1]) )
# d = datetime.timedelta(hours= int(li1[0]) ,minutes= int(li1[1]) )
# e  = d-c
# print(type(e))
# li3 = str(e).split(':')
# print(f'hours = {li3[0]} and minutes  = {li3[1]}')




#Q2(a) Write a program that asks the user to enter his or her full name,
#which consists of two or more names, separated by space characters.
#The program then prints out how many non-space characters the full name contains.

##first_name = input("Enter the first name :")
##last_name = input("Enter the last name :")

# full_name = input("Enter the full name :")
##
##name_length = len(full_name)
# count = 0
# for i in full_name.split(' '):
#     count +=len(i)
# ##
# print("The non-space character in full names are :",count)
# i=0
# while i<len(full_name):
#     if full_name[i] != ' ':
#         count +=1
#     i+=1
# print("The non-space character in full names are :",count)


#Q2(b)Write a program that asks the user to enter 2 or more integers
#to be entered on one line, separated by commas.
#The program then reads the numbers, computes and prints out the average.

#Taking multiple inputs
# a = input("ENter multiple values seperated by comma = ")
# li = a.split(',')
# print(li)
# s=0
# av=0
# for i in li:
#     s=s + int(i)

# av = s/len(li)
# print(av)




#Q3(a)A program is needed to read two times in 24-hour format,
#where each time is entered as two integers.
#The program then compares the two times and print out one of the following






#Q3(b)Suppose the rules for calculating income tax are as follows:
#10 percent on the first $40,000
#20 percent on the amount over $40,000 up to $80,000
#30 percent on the amount over $80,000 up to $120,000
#40 percent on the amount over $120,000
#Write a program to get the income of a person
#prints out the amount of tax the person has to pay.

##t1= 0.1
##t2= 0.2
##t3= 0.3
##t4= 0.4
##
##income = float(input("Enter the income : "))
##if income <= 40000:
##    tax = income*t1
##    net_income = income - (t1*income)
##    print("The next income under this package is; ",net_income, "and tax is; ",tax)
##
##elif income >40000 and income <=80000:
##    tax = income * t2
##    net_income = income -(t2*income)
##    print("The next income under this package 2 is; ",net_income, "and tax is; ",tax)
##    
##elif income >80000 and income<=120000:
##    tax = income * t3
##    net_income = income -(t3*income)
##    print("The next income under this package 3 is; ",net_income, "and tax is; ",tax)
##
##else:
##    tax = income * t4
##    net_income = income -(t4*income)
##    print("The next income under this package 4 is; ",net_income, "and tax is; ",tax)

    

#Q4(a) Write a program that reads a string
#prints how many vowels the string contains. Vowels are a, e, i, o and u.

# li=['a','e','i','o','u']
# strg= input("Enter any sentence :")

# count = 0
# for i in strg:
#    if i in li:
#        count += 1

# print("String has vowel",count)

#Q4(b)
#Let numbers be a list of integers.
#Write statements to determine if all the numbers are positive and print out either
#All the numbers are positive
#or Not all the numbers are positive


# numbers =[10,12,-2,-4,-9,11]

# for num in numbers:
#     if num>=0:
#         print(num,end =" ")
    
    
    

#Q5(a)
#Write a function with the header getDivisors(n) that takes an integer n and return a list of all the proper divisors of n.
#A proper divisor of n is a divisor which is greater than 1 and less than n.
#For example, if n is 18, the function should return the list [2, 3, 6, 9]

# def getDivisors(n):
#     li=[]
#     for i in range(2,n):
#         if n%i==0:
#             li.append(i)

#     return li

# a = int(input("Enter a number = "))
# print(getDivisors(a))



#q5(b)Write a function with the header countDivisors(n) that takes an integer n and returns the
#number of proper divisors of n. For example, if n is 18, the function should return 4.
#Note: You can use the function defined for part (a), if you wish.

# def countDivisors(n):
#     a = getDivisors(n)
#     return len(a)

# print(countDivisors(a))

#Q5(c)Write a function with the header isPrime(n) that takes an integer n and
#returns True if n is a prime number and False otherwise.
#Note: you can use the function defined for part (a) or part (b), if you wish.

# def isPrime(n):
#     if countDivisors(n) == 0:
#         return True
#     else:
#         return False

# print(isPrime(a))





#Q6(a)Let numbers be a list of integers.Write statements to set
#All elements that are greater than 100 to 100, and
# All elements that are less than 0 to 0

# numbers = [121,134,34,23,-9,-7,-4]
# for i in numbers:
#     if i>100:
#         print("greater than 100")
#     elif i<0:
#         print("less than 0")






#Q6(b)Let numList be a list of integers.
#Write statements to get a list of all numbers in numList but without any duplicates.
#Add statements to build a dictionary in which a key is a number in numList and
#the value is how many times the number appears in  numList.
#For example, if numList is {10, 20, 30, 30, 10, 10}, then the dictionary is
#{10: 3, 20: 1, 30: 2}

# li = [10, 20, 30, 30, 10, 10]
# li1=[]

# for i in li:
#     if i not in li1:
#         li1.append(i)

# print(li1)

# d = {}
# for i in li1:
#     d.update({i:li.count(i)})

# print(d)



# Q7

# f = open('authors.txt','r')
# g = f.readlines()

# for i in g:
#     li = i.split(';')
#     print(li[0],',',li[1])
#     li2 = li[2].split(',')
#     for j in li2:
#         print(j,end=", ")
#     print("")
    


# Q8 

# f = open('numbers.txt','r')
# g = f.readlines()
# print(g)
# s=0
# for i in g:
#     s = s + int(i)

# print(s)