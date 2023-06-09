# import math
# def Distance (X1,Y1,X2,Y2):
#     deltaX = X2 - X1
#     deltaY = Y2 - Y1
#     DX2 = deltaX * deltaX
#     DY2 = deltaY * deltaY
#     Result = math.sqrt(DX2 + DY2)
#     return Result


# Q36
# import datetime
# d = datetime.timedelta(hours=0,minutes=0,seconds=0)
# try:
#     f= open('afile.txt','r')
#     g = f.readlines()
#     for i in g:
#         li = i.split(':')
#         d = d+  datetime.timedelta(hours=int(li[0]),minutes=int(li[1]),seconds=int(li[2]))
    
#     li1 = str(d).split(':')
#     print(f"Time value of {li1[0]} hours {li1[1]} minutes {li1[2]} seconds")

#     e = datetime.time(int(li1[0]),int(li1[1]),int(li1[2]))
#     # print(e)
#     e = e.strftime('%I:%M:%S')
#     print("Time in 12-hour format ",e)

# except FileNotFoundError:
#     print("There is no file available with the given name '")








# I=0
# while I<len(L):
#     X = L[I]
#     print(I,X)
#     I = I +1


# output = 

# 0 3
# 1 9 



# l = [15,10,20,5]
# li=[]

# for i in range(len(l)):
#     li.append([])
#     c = 0 
#     for j in range(len(l)):
#         if l[i]>l[j]:
#             c+=1
#     li[i].append(l[i])
#     li[i].append(c)

# print(li)


# 37 b


fname = input("Please enter the file name = ")
li=[]
try :
    f = open(fname, 'r')
    g = f.readlines()
    for i in range(len(g)):
        li.append([])
        d = g[i].split(';')
        # li[i].append(int(d[0]))
        e= d[1].split(' ')
        print(e)
        for j in e:
            c=0
            # li.append([])
            li[i].append(int(d[0]))
            if j not in li[i]:
                li[i+c].append(j)
                c+=1
    
    print(li)
        


except FileNotFoundError:
    print("There is no file available with the given name '")