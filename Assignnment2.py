

# stuff = {'1' : 'aaa', '2' : 'bbb', '3' : 'ccc'}
# # for k in stuff:
# #     print(k, stuff[k])


# for k in stuff.keys():
#     print(k, stuff[k])

# for k in stuff.values():
#     print(k)

# ##########  Q-1 
# d =dict()
# try:

#     f  = open('abbreviations.txt','r')

#     li = f.readlines()

#     for i in range(len(li)):
#         li[i] = li[i].rstrip('\n')
#         bli = li[i].split(':')
#         d.update({bli[0]: bli[1]})

#     print(d)
# except FileNotFoundError:
#     print("There is no file available with this name")

# a= input("Enter text message = ")
# a = a.split(' ')
# print(a)

# s = ''
# for i in a:
#     if i.lower() in d.keys():
#         s = s + str(d.get(i.lower()))+' '
#     else:
#         s = s + str(i)+' '

# print(s)


############Q2 
# ####### Method 1 
# f= open("names_set1.txt",'r')
# f1= open("names_set2.txt",'r')
# f2 = open("merged.txt",'a+')
# s=set()
# s1=set()

# for i in f:
#     s.add(f.readline().title())

# for j in f1:
#     s1.add(f1.readline().title())

# print(sorted(s))
# print(sorted(s1))
# print(sorted(s|s1))

# for k in sorted(s|s1):
#     f2.write(k)

# print(f2.read())


# ############# Method 2 






# q 3 - Pattern

# try:
#     a = int(input("Enter number of rows = "))
#     for i in range(0,a):
#         for j in range(i,-1,-1):
#             print(2**j, end="    ")
#         print(" ")
# except ValueError:
#     print("You must input a number not the characters")






# Q4 - leap year

import calendar as c 

def isLeapYear(a):
    if a>=1800 and a<20000:
        if a%4==0:
            if a%100==0:
                if a % 400==0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False44
    else:
        return False

# def isLeapYear(a):
#     if a>=1800 and a<=20000:
#         if (a%4==0 and a%100!=0) or a%400==0:
#             return True
#         else:
#             return False
#     else:
#         return False


def daysInMonth(m,a):
    if m in range(1,13):
        if m in [1,3,5,7,8,10,12]:
            return 31
        elif m in [4,6,9,11]:
            return 30
        elif m ==2 and isLeapYear(a):
            return 29
        elif m ==2 and (not isLeapYear(a)):
            return 28
    else:
        return False

def isValidDate(d,m,y):
    if (d>0 and d<=daysInMonth(m,y))and (y>1800 and y<20000) :
        return True
    else:
        return False


def dayOfWeek(day,month,year):
    if not isValidDate(day,month,year):
        return None
    else:
        x = year - (14 - month)//12
        y = x + x//4 - x//100 + x//400
        z = month + 12 * ((14 - month) //12) -2
        dow = (day + y + (31 * z)//12) % 7
        return dow

def dob(day,month,year):
    if isValidDate(day,month,year):
        d= dayOfWeek(day,month,year)
        if d==1:
            return "The Person was born on a Monday"
        elif d==2:
            return "The Person was born on a Tuesday"
        elif d==3:
            return "The Person was born on a Wednesday"
        elif d==4:
            return "The Person was born on a Thrusday"
        elif d==5:
            return "The Person was born on a Friday"
        elif d==6:
            return "The Person was born on a Saturday"
        elif d==7:
            return "The Person was born on a Sunday"
    else:
        return "The given date is invalid."

def printCalendar(month, year,day=1):
    print("The Calender in their birth month was : ")
    if isValidDate(day,month,year):
        return c.month(year,month)
    
def main():
    try:
        n= input("Enter the day, month & year = ").split('-')

        d,m,y = int(n[0]),int(n[1]),int(n[2])
        print(dob(d,m,y))

        # print(printCalendar(m,y))

        # print(printCalendar(4,2021))
    except ValueError:
        print("please enter data in this format (dd-mm-yyyy)")


if __name__ =="__main__":
    main()


    

########## Q 5 
# try:
#     f = open("BusRoute250.txt","r")

#     li = f.readlines()

#     for i in li:
#         j = i.rstrip('\n')
#         j = j.split('/')

#         print(j[0])
#         print(j[1])
#         print(j[2])
#         print(j[3])
#         print(" ")
# except:
#     print("No such file Available")

# li = list()
# busStopList = list()
# busStopNames = list()
# streetsOnRoute = list()
# suburbsOnRoute = list()

# def loadData():
#     try:
#         with open("BusRoute250.txt","r") as f:
#             global li
#             li = f.readlines()
#             # print(li)
#             for i in li:
#                 j = i.rstrip('\n')
#                 j = j.split('/')
#                 busStopList.append(j)
#             # print(busStopList)
#     except:
#         print("Not Found")
    
    
# def listAllBusStopNames(): 
#     for i in busStopList:
#         if i[1] not in busStopNames:
#             busStopNames.append(i[1])
    
#     for j in busStopNames:
#         print(j)

# def listAllStreetsOnRoute(): 
#     for i in busStopList:
#         if i[2] not in streetsOnRoute:
#             streetsOnRoute.append(i[2])
    
#     for j in streetsOnRoute:
#         print(j)

# def listAllSuburbsOnRoute():
#     for i in busStopList:
#         if i[3] not in suburbsOnRoute:
#             suburbsOnRoute.append(i[3])
    
#     for j in suburbsOnRoute:
#         print(j)

# def searchByNumber(start, end):
#     print(start, end)
#     for i in range(len(li)):
#         if i>=start-1 and i<=end-1:
#             print('stop'+li[i])

# def searchByName(nameKey): 
#     nameKey = nameKey.lower()
#     # busStopList
#     for i in range(len(busStopList)):
#         if (busStopList[i][1].lower()).find(nameKey)!= -1:
#             print('stop'+li[i])


# def searchByStreet(streetKey): 
#     streetKey = streetKey.lower()
#     # busStopList
#     for i in range(len(busStopList)):
#         if (busStopList[i][2].lower()).find(streetKey)!= -1:
#             print(li[i])

# def searchBySuburb(suburbKey): 
#     suburbKey = suburbKey.lower()
#     # busStopList
#     for i in range(len(busStopList)):
#         if (busStopList[i][3].lower()).find(suburbKey)!= -1:
#             print(li[i])

# def searchByAnyField(key):
#     key = key.lower()
#     # busStopList
#     for i in range(len(busStopList)):
#         if (busStopList[i][1].lower()).find(key)!= -1:
#             print(li[i])

#         if (busStopList[i][2].lower()).find(key)!= -1:
#             print(li[i])

#         if (busStopList[i][3].lower()).find(key)!= -1:
#             print(li[i])



# loadData()
# a=input()
# # print(busStopList)
# print()
# print()
# print()
# print()
# print(li)
# print("######Bus Stop Names#######")
# listAllBusStopNames()
# a=input()
# print("######Street Names#######")
# listAllStreetsOnRoute()
# a=input()

# print("######Suburbs#######")
# listAllSuburbsOnRoute()
# a=input()
# print("######Search #######")

# searchByNumber(5,10)
# a=input()
# searchByName("de")
# print("######Search any field #######")
# searchByAnyField("gar")
# a=input()




# Q2

# def read_non_empty_line(input):
#     while True:
#         line = input.readline()
#         if line == "":
#             return ""
#         if line.isspace() == False:
#             return line.strip()

# def combine_sorted_files(file1, file2, output):

#     read_file1, read_file2 = True, True

#     with open(output,'w') as output_file:
#         with open(file1,'r') as input_file1:
#             with open(file2,'r') as input_file2:
#                 while True:
#                     if read_file1:
#                         line1 = read_non_empty_line(input_file1)
                    
#                     if read_file2:
#                         line2 = read_non_empty_line(input_file2)

#                     if line1 == "" or line2 == "":
#                         break

#                     read_file1, read_file2 = False, False
#                     print(line1,line2)
#                     if line1 == line2:
#                         smaller = line1
#                         read_file1 = True
#                         output_file.write(smaller+"\n")
#                         break
#                     elif line1 < line2:
#                         smaller = line1
#                         read_file1 = True
#                         output_file.write(smaller+"\n")
#                         break
#                     else:
#                         smaller = line2
#                         read_file2 = True
#                         output_file.write(smaller+"\n")
#                         break

#                 while line1 != "":
#                     output_file.write(line1+"\n")
#                     line1 = read_non_empty_line(input_file1)
#                 while line2 != "":
#                     output_file.write(line2+"\n")
#                     line2 = read_non_empty_line(input_file2)



# combine_sorted_files("names_set1.txt", "names_set2.txt", "names_output")




# f1 = open("names_set1.txt",'r')
# f2 = open("names_set2.txt",'r')
# f3 = open("names_output1.txt",'w')

# top1 = f1.readline()
# top2 = f2.readline()

# while top1 or top2:
#     if top1 =="":
#         f3.write(top2)
#         top2 = f2.readline()
#     elif top2=="":
#         f3.write(top1)
#         top1 = f1.readline()
#     elif top1<top2:
#         f3.write(top1)
#         top1 = f1.readline()
#     elif top2<top1:
#         f3.write(top2)
#         top2 = f2.readline()
#     else:
#         f3.write(top2)
#         top1= f1.readline()
#         top2 = f2.readline()


# f1.close()
# f2.close()
# f3.close()