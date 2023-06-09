# String  - sequence/collection of characters
# in other languages
# single characters   'a'
# string  "ram"


# In Python
# Single or Multiple character  'asdsd', "dssdf"

# empty / null string
# a=''
# b = str()
# print(a)
# print(b)

# defining a string 
# a = 'Shyam'
# print(a)

# from user input
# a= input("Enter a name = ")
# print(a)

# String Properties
# a = "Hello World"
# print(len(a))       #for length 
# print(type(a))      #for data type
# del a               #for undefining a variable
# print(dir(''))      #for all the methods

# String Operations 
# Concatenation
# a= 'll'         #a[2:4]
# b='ld'          #a[9:]
# c = a+b
# print(c)

# repetitive
# print('#'*50)

# String Indexing 

#     -11  -10  -9 -8  -7  -6  -5  -4  -3  -2  -1       -ve index
#       H   e   l   l   o       W   o   r   l   d
#       0   1   2   3   4   5   6   7   8   9   10      +ve index

# Accessing 
# a = "Hello World"
# print(a[6])
# print(a[-5])

# String Slicing
# a = "Hello World"
# print(a[1:7])
# print(a[-10:-4])

# print(a[2:4])
# print(a[9:])

# b= (a[2:4]*2 + a[9:]*2)*3
# print(b)

# c = a[-9:-7] + a[-2:]
# print(c)

#           String Methods
print(dir(''))      #for all the methods

# m = 'ram'
# n ='jonny'

# print(m+n)
# print(m.__add__(n))

# print('o' in n)
# a= input("enter your name = ").lower()
# a = 'hello world'
# b="InnoVATION"
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.lower())
# print(a[8].upper())
# a = a.replace('r','R')
# print(a)

# print(a.casefold())       //similar as lower()
# print(b.casefold())

# a = 'hello world'
# b="InnoVATION"
# print(a.swapcase())
# print(b.swapcase())

# print(a.center(100,'-'))
# print(a.count('l'))

# print(a.index('l'))
# print(a.find('l'))

# print(a.index('l',4))
# print(a.find('l',4))

# print(a.index('z')) #if character isnot found, then it gives an error
# print(a.find('z'))    ##if character isnot found, then it gives -1

# Finding for last character
# a = 'hello world'
# print(a.rindex('o'))
# print(a.rfind('o'))

# formatting string
# a = 'hello world'
# b="InnoVATION"
# c =1234

# print("hello ",c," hey ",a," is the new ",b)
# print("hello {} hey {} is the new {}".format(c,a,b))
# print("hello {0} hey {1} is the new {2}".format(c,a,b))
# print("hello {m} hey {n} is the new {p}".format(n=a,p=b,m=c))
# print(f"hello {c} hey {a} is the new {b}")

# d= "India\t is\t my\t country. I love my country."
# print(d.expandtabs(tabsize=16))     #by default, tabsize is 8

# String Conditional Methods
# a = 'hello world'
# b="InnoVATION"
# c ='1234'
# d= "India\t is\t my\t country. I love my country."
# e = '2.34'

# print(a.isalpha())
# print(b.isalpha())

# print(a.isalnum())
# print(c.isalnum())

# print(a.isascii())
# print(c.isdigit())
# print(c.isnumeric())
# print(c.isdecimal())
# print(e.isdigit())
# print(e.isnumeric())
# print(e.isdecimal())       # decimal stands for "Decimal Number System" ( 0-9)

# a = 'HELLOWORLD'
# b="Innovation Initiative"
# c ='1234'
# d= "India\t is\t my\t country. I love my country."
# e = '2.34'

# print(a.isupper())
# print(b.islower())
# print(b.istitle())

# print(" \t\n".isspace())
# print(d.isprintable())
# print(b.isprintable())
# print(a.isidentifier())

a = 'HELLOWORLD'
b="                  Innovation Initiative                 "
c ='1234'
d= "India\t is\t my\t country. I love my country."
e = '2.34'

# print(a.startswith('HELL'))
# print(a.endswith('RLD'))

# print('-'.join(a))

# print(a.ljust(60,'-'))
# print(a.rjust(60,'-'))

# print(len(b))
# print(b.strip())
# print(b.lstrip())
# print(b.rstrip())


# f= 'https://www.google.com/'
# print(f.lstrip('https://'))
# print(f.removeprefix('https://'))
# print(f.rstrip('.com/'))
# print(f.removesuffix('.com/'))

# f = f.replace('google','')
# print(f)

# d= "India is my country.\n I love my country.\n delhi is capital\n"
# # d = d.split()
# # print(len(d))

# d= d.splitlines()
# print(len(d))

# c ='1234'
# print(c.zfill(8))