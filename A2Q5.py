##

#Question 5

#Reading Bus route data

#Using exception if no particular file is available in given file
try:
    #Reading and displaying the details about the bus stops from given file
    f = open("BusRoute250.txt","r")

    li = f.readlines()

    for i in li:
        #Using strip and split method to separate the lines from given text
        j = i.rstrip('\n')
        j = j.split('/')

        print(j[0])
        print(j[1])
        print(j[2])
        print(j[3])
        print(" ")
except:
    #If no file is found in given file, display the following message
    print("No such file Available")

#Creating list with following fucntions listed below
    
li = list()
busStopList = list()
busStopNames = list()
streetsOnRoute = list()
suburbsOnRoute = list()


#Creating various function to load the data into a list of bus stops
#and make various queries about the bus stops on the route from the given file

#Using Exception handling method in load data fucntion if file is not found
def loadData():
    try:
        with open("BusRoute250.txt","r") as f:
            global li
            li = f.readlines()
             # print(li)
            for i in li:
                j = i.rstrip('\n')
                j = j.split('/')
                busStopList.append(j)
             # print(busStopList)
    except:
        print("Not Found")



#Function defining all bus stop names  
def listAllBusStopNames(): 
    for i in busStopList:
        if i[1] not in busStopNames:
            #Using append function if busstop is not present
            busStopNames.append(i[1])
    
    for j in busStopNames:
        #Printing all the bus stop names
        print(j)


#Function defining all streets on the route
def listAllStreetsOnRoute(): 
    for i in busStopList:
        if i[2] not in streetsOnRoute:
            streetsOnRoute.append(i[2])
    
    for j in streetsOnRoute:
        print(j)

#Function defining all suburbs on the route
def listAllSuburbsOnRoute():
    for i in busStopList:
        if i[3] not in suburbsOnRoute:
            suburbsOnRoute.append(i[3])
    
    for j in suburbsOnRoute:
        print(j)

#Function defining searching by number
def searchByNumber(start, end):
    print(start, end)
    for i in range(len(li)):
        if i>=start-1 and i<=end-1:
            print('stop'+li[i])

#Function defining searching by name
def searchByName(nameKey):
    #Using lower fucntion to handle upper and lower case names
    nameKey = nameKey.lower()
     # busStopList
    for i in range(len(busStopList)):
        if (busStopList[i][1].lower()).find(nameKey)!= -1:
            print('stop'+li[i])

#Function defining searching by street name
def searchByStreet(streetKey): 
    streetKey = streetKey.lower()
   
    for i in range(len(busStopList)):
        if (busStopList[i][2].lower()).find(streetKey)!= -1:
            print(li[i])

#Function defining searching by suburb name
def searchBySuburb(suburbKey): 
    suburbKey = suburbKey.lower()
     # busStopList
    for i in range(len(busStopList)):
        if (busStopList[i][3].lower()).find(suburbKey)!= -1:
             print(li[i])
#Function defining searching done ny anyfield
             
def searchByAnyField(key):
    #Handling upper and lower case
    key = key.lower()
     # busStopList
    for i in range(len(busStopList)):
        if (busStopList[i][1].lower()).find(key)!= -1:
            print(li[i])

        if (busStopList[i][2].lower()).find(key)!= -1:
            print(li[i])

        if (busStopList[i][3].lower()).find(key)!= -1:
            print(li[i])


#Loading the all the data
loadData()
print("\n")
 # print(busStopList)
print()
print()

print(li)
print("######Bus Stop Names#######")

#Displaying Bus Stop Names
listAllBusStopNames()
print("\n")
print("######Street Names#######")

#Displaying Streets Names
listAllStreetsOnRoute()
print("\n")
print("######Suburbs Names#######")

#Displaying Suburbs Names on routes
listAllSuburbsOnRoute()
print("\n")
print("###### Search between Bus Stop ID #######")
# Searching between two bus stops number
a = int(input("Enter the starting Bus Stop ID = "))
b = int(input("Enter the stoping Bus Stop ID = "))
searchByNumber(a,b)


print("\n")
print("###### Search for Bus Stop by any String #######")
d = input("Enter Any String to find the Bus Stop = ")
searchByName(d)

print("###### Search by any String #######")
e = input("Enter Any String = ")
searchByAnyField(e)
print("\n")

