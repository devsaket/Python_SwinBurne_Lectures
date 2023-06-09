# Iterative statement
# Repetitive 

# print(range(10))
# print(range(0,10))
# print(range(0,10,1))

# for i in range(10,0,-1):
#     print(i,end=" ")



# i=0
# while i<10:
#     print(i, end=" ")
#     i=i+1


# s=0
# for i in range(1,11):
#     print(i, end=" ")
#     s= s+i
# print("\nTotal sum = ",s)

# i=1
# s=0
# while i<11:
#     print(i, end=" ")
#     s=s+i
#     i=i+1
# print("\n Total Sum = ",s)

# 
# s=0
# a = int(input("Enter no of terms = "))
# for i in range(1,a*2):
#     if i%2 != 0:
#         print(i)
#         s=s+i

# print("Total = ",s)

# 
# s=0
# i=0
# a= int(input("Enter no of terms = "))
# while i< a*2:
#     if i%2!=0:
#         print(i)
#         s=s+i
#     i=i+1
# print("Total = ",s)


# a = int(input("Enter the no = "))
# for i in range(a,0,-1):
#     print('*' * i)



# Nested Loops 

# for  i in range(10):
#     print(" i =  ",i)
#     for  j in range(10):
#         print("j=",j,end="  ")
#     print(" ")

# for  i in range(10):
#     for  j in range(10):
#         print(j,end=" ")
#     print(" ")

# for  i in range(10):
#     for  j in range(i, 10):
#         print(j,end=" ")
#     print(" ")

# a = int(input("Enter the no of lines : "))
# for  i in range(a):
#     for  j in range(i, a):
#         print("*",end=" ")
#     print(" ")


# for  i in range(10):
#     for  k in range(10-i-1):
#         print(" ",end=" ")

#     for  j in range(i+1):
#         print(j,end=" ")

#     for  m in range(i):
#         print(m,end=" ")
#     print(" ")

# a=10
# for  i in range(a):
#     for j in range(a-i+1):
#         print(end=" ")
    
#     for k in range(i+1):
#         print("*",end=" ")
#     print(" ")

# a=4
# t=1
# for  i in range(a):
#     for j in range(a-i+1):
#         print(end=" ")
    
#     for k in range(i+1):
#         print(t,end=" ")
#         t=t+1
#     print(" ")

# a=6
# t=1
# for  i in range(a):
#     for j in range(a-i+1):
#         print(end=" ")
    
#     for k in range(i+1):
#         print(t,end=" ")
#     t=t+1
#     print(" ")



# 
# s=0
# for i in range(1,10):
#     if i%2 != 0:
#         print(i,end="+ ")
#         s=s+i

# print("\nTotal = ",s)


# s=0
# for i in range(1,100):
#     if i%5 == 0:
#         print(i,end="+ ")
#         s=s+i

# print("\nTotal = ",s)

# s=0
# for i in range(1,100):
#     print(i,end="+ ")
#     s=s+i

# print("\nTotal = ",s)

# s=0
# for i in range(1,10):
#     print("1/",i,end=" + ")
#     s=s+ 1/i

# print("\nTotal = ",s)


# s=0
# for i in range(1,11):
#     print(i**2,end="+ ")
#     s=s+i**2

# print("\nTotal = ",s)



# s=0
# for i in range(1,11):
#     print("1/",i**2,end="+ ")
#     s=s+ 1/(i**2)

# print("\nTotal = ",s)


# s=0
# for i in range(1,11):
#     print("1/",i**i,end="+ ")
#     s=s+ 1/(i**i)

# print("\nTotal = ",s)


# q6

# a = int(input("Enter a number = "))

# for i in range(1,11):
#     print(f"{a} * {i} = {a*i}")

# q7

# a = int(input("Enter a number = "))

# for j in range(1,a+1):
#     for i in range(1,11):
#         print(f"{i}*{j}={j*i}",end=" ")
#     print(" ")