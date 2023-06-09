# Collections - Group of elements (which may or may not be homogeneous)
# Two types : - 
    # Immutable --(cant be modified ) -- tuple, set
    # Mutable -- (modifiable )  -- list, dict

# List - group of elements

# a = [10,20,30,40,50,60,80,'a@er','fg','ram singh']

# Indexing
#    0  1  2  3   4  5  6    7     8       9 


# length of the list
# print(len(a))

# to access a element

# print(a[7])
# print(a[-3])

# print(a[2:6])

# # to access all the elements (Traversing)
# method 1 
# for i in a:
#     print(i, end="  ")

# method 2
# for j in range(len(a)):
#     print(a[j], end="  ")


# to print all the in-built methods
# print(dir(a))

# list Operations 
# a1 = [10,20,30,40,50,60,80]
# b1 = ['a@er','fg','ram singh']
# c=['erdf','fgdfcxv',"hello world ","this is a toy "]

# # Extending / merging of two list 
# s= a1 + b1+c
# print(s)


# # repetition 
# print(a1*2) 

# a2=list()
# a2=[]
# for i in a1:
#     a2.append(i*2)
    # print(i*2, end="  ")
# print(a2)

# List Methods
# print(dir(a1))

# print(max(a1))
# print(min(a1))
# print(sum(a1))
# print(len(a1))
# print(dir(a1))
# del a1
# print(a1)


# print(a1)
# a1.append(34)
# print(a1)


# a1.insert(2,78)
# print(a1)


# a1 = [10,20,30,40,30,56,30,50,60,80]
# b1 = ['a@er','fg','ram singh']
# c=['erdf','fgdfcxv',"hello world ","this is a toy "]

# li1 = b1
# li1 = b1.copy()
# print(li1)

# li2=[]
# print(li2)
# li2 = li2+b1
# li2.extend(b1)
# print(li2)

# print(a1.count(30))

# print(a1.index(56)).

# a1 = [10,20,30,40,30,56,30,50,60,80]
# b1 = ['a@er','fg','ram singh']
# c=['erdf','fgdfcxv',"hello world ","this is a toy "]
# a1.pop()
# print(a1)

# a1.remove(40)
# print(a1)

# a1.reverse()
# print(a1)

# a1.sort()
# print(a1)

# a1.reverse()
# print(a1)


# a1.sort(reverse=True)
# print(a1)

# a1.clear()
# print(a1)


# a = "india is my country"
# b=a.split()
# print(b[2])

#-----------------------------------------------------------------
# TUPLES -- immutable collection (it cant be modified)
#-----------------------------------------------------------------
# for empty tuple
# t = ()
# t1 = tuple()
# print(t)
# print(t1)

# ----------------------------------------------------------------------
# TUPLE VARIABLE DECLARATION
# ----------------------------------------------------------------------
# names = ('ram','shyam','mohan','sohan','rohan',1,2,3,4.54,34)
# print(names)

# names = 'ram','shyam','mohan','sohan','rohan',1,2,3,4.54,34
# print(names)

# x = (1)
# x=1
# print(x)

# x = (1,)
# x = 1,
# print(x)

# ----------------------------------------------------------------------
# ACCESS TUPLE ELEMENTS
# ----------------------------------------------------------------------
# names = ('ram','shyam','mohan','sohan','rohan',1,2,3,4.54,34)
#            0      1       2        3      4    5 6 7  8   9
# print(names[3])
# print(names[-3])
# print(names[10])


# n = ('ram','shyam','mohan','sohan')
# for i in n:
#     print(i)

# for i in range(len(n)):
#     print(n[i])

# for i in n:
#     if i.endswith('m'):
#         print(i)


# ----------------------------------------------------------------------
# TUPLE UNPACKING
# ----------------------------------------------------------------------
# n = ('ram','shyam','mohan','sohan')
# a,b,c,d = n
# print(a,b,c,d)


# ----------------------------------------------------------------------
# TUPLE PACKING
# ----------------------------------------------------------------------
# a=2
# b=-5
# c='ram'
# d = 'hello world'
# e = 3.432

# nt = a,b,c,e,d
# print(nt)

# ----------------------------------------------------------------------
# TUPLE OPERATIONS
# ----------------------------------------------------------------------
# t1 = (1,2,3,4,5)
# t2 = (7,2,3,'s')
# print(t1 + t2)          #Concatenation
# print(t1*4)             #repetitive

# NOTE: We cant insert,update or delete any element from a tuple.

# print(list(t1))


# ----------------------------------------------------------------------
# SET -- immutable collection (it can be modified)
# ----------------------------------------------------------------------
# for empty set
# a = set()


# a = {2,3,4,1,4,2,7,4,9,1}
# print(a)

# b = '123345433233'
# print(set(b))

# b = {12,3,(2,3,4),56}
# print(b)

# b = {12,3,[2,3,4],56}
# print(b)

# b = {12,3,{2,3,4},56}
# print(b)

# ----------------------------------------------------------------------
# SET OPERATIONS
# ----------------------------------------------------------------------
# s1 = {1,2,3,45,6,7,8}
# s2 = {3,4,6,44,7,45,56}
# print(s1,s2)
# ----------------------------------------------------------------------
# UNION
# ----------------------------------------------------------------------
# print( s1 | s2)
# print(s1.union(s2))
# ----------------------------------------------------------------------
# Intersection
# ----------------------------------------------------------------------
# print(s1 & s2)
# print(s1.intersection(s2))
# ----------------------------------------------------------------------
# DIFFERENCE
# ----------------------------------------------------------------------
# print(s1-s2)
# print(s2-s1)
# print(s1.difference(s2))
# ----------------------------------------------------------------------
# SYMMETRIC DIFFERENCE
# ----------------------------------------------------------------------
# print(s1^s2)
# print(s1.symmetric_difference(s2))


# ----------------------------------------------------------------------
# SET METHODS
# ----------------------------------------------------------------------
# s1.add(23)
# print(s1)

# s3 = s1.copy()
# s3=s1
# print(s3)

# s1.discard(45)
# print(s1)

# s1.discard(59)
# print(s1)

# s1.remove(45)
# print(s1)

# s1.remove(67)
# print(s1)

# s1.pop()
# print(s1)

# s1.update(s2)
# print(s1)


# ----------------------------------------------------------------------
# DICTIONARY -- mutable collection (it can be modified)
# ----------------------------------------------------------------------
# for empty dict
a = {}
b = dict()

# syntax
# var_name = {key:value, key:value, ...}

a = {'name':'ram','address':'chandigarh'}
# print(a)
# print(a['name'])
# print(a.get('name'))
# print(a.values())
# print(a.keys())
# print(a.items())

# a.update({'country':'india','pincode':160011, 'salary':98768.36})
# print(a)

# a['address'] = 'sector 11'
# a['state'] = 'chandigarh'
# print(a)
# a['name'] = 'shyam'
# print(a)

# b=a

# del a['address']
# print(a)

# print(b)
# b.pop('address')
# print(b)

# b.popitem()
# print(b)


# Converting list into dict
li = [11,2,4,5,6,3,5,2,1,8,9]
d={}
for i in range(len(li)):
    d.update({i:li[i]})

print(li)
print(d)

key =list(d.keys())
print(key)
val = list(d.values())
print(val)