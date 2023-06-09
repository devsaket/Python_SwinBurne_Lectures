# def gene():
#     n =1
#     print("printed first")
#     yield n

#     n =n+1
#     print("printed second")
#     yield n

#     n =n+1
#     print("printed last")
#     yield n

# a=  gene()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# ----------------------------------------------------------------------

# def gene(m):
#     n =1
#     if m==1:
#         print("printed first")
#         return n
#     elif m==2:
#         n =n+1
#         print("printed second")
#         return n
#     elif m==3:
#         n =n+1
#         print("printed last")
#         return n


# m=3
# print(gene(m))

# ----------------------------------------------------------------------
# a="hello"
# for i in range(len(a)-1,-1,-1):
#     print(a[i])

# ----------------------------------------------------------------------
# def rever(a):
#     for i in range(len(a)-1,-1,-1):
#         yield a[i]                          # ['o','l','l','e','h']

# a="hello"
# # print(rever(a))
# for j in rever(a):
#     print(j)

# ----------------------------------------------------------------------

# m = [1,3,6,9,10]
# ml = [x**2 for x in m]
# print(ml)

# mg = (x**2 for x in m)
# print(mg)
# print(next(mg))
# print(next(mg))
# print(next(mg))
# for i in mg:
#     print(i)