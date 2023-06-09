# modules - small processing blocks

# def round(n):
#     if n==1 or n==2:
#         n=0
#     elif n==3 or n==4 or n==5 or n==6 or n==7:
#         n=5
#     elif n==8 or n==9 or n==10:
#         n=10

#     return n
    

# def sum2(m,n):
#     p = m+n
#     return p

# def evenOrOdd(x):
#     if x%2==0:
#         return "even"
#     else:
#         return "odd"


# x = int(input("Enter  number to check even od odd ="))
# q = evenOrOdd(x)

# def main():
#     print(round(9))


    # w = int(input("Enter  number to check even od odd ="))
    # q = evenOrOdd(w)
    # print(q)

    # a = int(input("Enter1st number = "))
    # b = int(input("Enter 2nd number = "))
    # c = sum2(a,b)
    # print("sum = ",c)

# if __name__=='__main__':
#     main()


#################################################
####            Revision
##############################################

# Function - block of small programs - modules

# a = int(input("Enter a number = "))
# b = int(input("Enter 2nd number = "))
# c=a+b
# print("Sum = ",c)

# 2000 pairs
# 2000*4 line of code (Addition process repeat)
# 2000*3 variable

# def summation():
#     a = int(input("Enter a number = "))
#     b = int(input("Enter 2nd number = "))
#     c=a+b
#     print("Sum = ",c)

# for i in range(2000):
#     summation()



###### --> within function we cant have input & output operation, we define only core process of the function/program


# def summation(a,b):
#     c=a+b
#     return c

# def main():
#     for i in range(10):
#         a = int(input("Enter a number = "))
#         b = int(input("Enter 2nd number = "))
#         c = summation(a,b)
#         print("Sum = ",c)


# # main function initiater
# if __name__ == '__main__':
#     main()
# ----------------------------------------------

# Even or odd 
# def evenOdd(a):
#     if a%2==0:
#         return 'even'
#     else:
#         return 'odd'

# def factors(m):
#     li = list()
#     for i in range(1,m+1):
#         if m%i ==0:
#             li.append(i)
    
#     return li


# a = int(input("Enter a number = "))
# print(evenOdd(a))
# print(factors(a))

###############################################

# def summation(a,b):
#     return a+b


# x = lambda a, b : a + b
# print(x(4,7))