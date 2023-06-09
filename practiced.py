# n = 6
# while n>0:
#     n -= 3
#     print(n)

# b = 10
# while True:
#     print(b)
#     if b<9:
#         continue
#     b = b-9

# print(True or True and False)

# def f1(x=1,y=2):
#     x=x+y
#     y+=1
#     print(x,y)

# f1()

'''
def nPrint(m,n):
    while n>0:
        print(m)
        n-=1
nPrint('a',4)
'''

# single line 

'''multi line'''


# x = 1
# x *= x+1
# print(x)


# Swapping of two numbers
# x,y = 1,2
# x,y = y,x
# print(y,x)

# print(2.0**3)

# x = 1
# x  = 2*x+1
# print(x)


# print(round(3.5))


# ###################################################
#####################################################

# line = input("Enter a word ")
# print("You typed",line)
# line = line + "h"
# num = int(line)
# print("you typed the number ",num)

def lm(list):
    x=0
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            x+=1

    return x


a1=[8,10,8,6,4,2]
print(lm(a1))