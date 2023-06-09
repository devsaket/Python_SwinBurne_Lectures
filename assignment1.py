# Question 1 
# String input  ---> no of vowels 

# a = input("Enter your name = ")
# a = a.lower()

# print(f"There are {len(a)} characters in your name.")
# print(f"The Number of times 'A' occurs in your name is {a.count('a')}")
# print(f"The Number of times 'E' occurs in your name is {a.count('e')}")
# print(f"The Number of times 'I' occurs in your name is {a.count('i')}")



# Q 2 
# string input , search string , count 

# m = input("Enter the string = ").lower()
# n = input("Enter the search string = ").lower()

# print(f"No of times of word '{n}' = {m.count(n)}")



# Q 4
# 

# a = float(input("Enter the amount = "))
# i = float(input("Enter the interest = "))
# t = float(input("Enter the time (in years) = "))


# s = a*((1+ i/t)**t)

# print(f"Total amount = {s}")


# Q 6a
# def roundoff(a):
#     c = a.split('.')[1][-1]
#     if c=='1' or c=='2':
#         b = a.split('.')[0] + '.' + a.split('.')[1].replace(c,'0')
#     elif c=='3' or c=='4' or c=='6' or c=='7' or c=='5':
#         b = a.split('.')[0] + '.' + a.split('.')[1].replace(c,'5')
#     elif c=='8' or c=='9':
#         m=a.split('.')[1].replace(c,'0')
#         n=int(a.split('.')[1][-2])+1
#         b = a.split('.')[0] + '.'+str(n)+str(m)[-1]
#     return  b


# m = input("Enter a number = ")
# print(roundoff(m))



# Q5 - 1020304500560  -> 1+2+3+450+56

a = input("Enter a number = ")
# print(a.rsplit('0'))

l = a.rsplit('0')
for  i in range(len(l)):
    if l[i]=='':
        l[i]='0'
        l[i-1]=l[i-1]+ l[i]

# print(l)

li = []
for i in l:
    if int(i)!=0 and i not in li:
        li.append(i)

# print(li)
p=0
t=0
s=''
for i in li:
    if int(i)%2==0:
        s = s+ i +' + '
        p = p+int(i)
        t=t+1
print(s[:-2],' = ',p)
print(p,'/',t,' = ',p/t)
# print(p/t)