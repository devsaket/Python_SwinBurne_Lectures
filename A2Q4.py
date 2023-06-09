##

#Question 4
#Part(a)

#Importing calendar library
import calendar as c 

#Declaring a function called isLeapYear that takes a year as an integer and returns True
#if it is a leap year and False otherwise


#Using condition if function is divisible by 4,and 400    but not by 100     
def isLeapYear(a):
    #Checking if the year falls under range of 1800 to 20,0000
    if a>=1800 and a<=20000:
        #Using condition if given year is a leap year
        if (a%4==0 and a%100!=0) or a%400==0:
            return True
        else:
            return False
    else:
        return False


#Part(b)
#Declaring a function called daysInMonth that takes a month of a year
#and returns the number of days for that month

def daysInMonth(m,a):
    #Taking m as month where it only takes integer value
    
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

#Part(c)

#Define a function called isValidDate that takes three integers for a day, month and a year
#returns True if the thee integers represent a valid date and False otherwise.
#Using if and else condition to check if days are greater than zero and year falls under range

def isValidDate(d,m,y):
    if (d>0 and d<=daysInMonth(m,y))and (y>1800 and y<20000) :
        return True
    else:
        return False

#Part(d)

#Creating function called dayOfWeek that takes the day, month and year of a date
#and returns a number to represent the day of the week for that date,
#By using Gauss Algorithm

def dayOfWeek(day,month,year):
    
    #If the numbers do not represent a valid date the functionis returning None
    if not isValidDate(day,month,year):
        return None
    #Using Gauss Algorithm to return day of the week by giving 0 to Monday and so on
    else:
        x = year - (14 - month)//12
        y = x + x//4 - x//100 + x//400
        z = month + 12 * ((14 - month) //12) -2
        dow = (day + y + (31 * z)//12) % 7
        return dow

#Part(e)
#Creating function called printCalendar that takes two integers to represent a particular month in a
#particular year and prints out the calendar for that month.

def printCalendar(month, year,day=1):
    print("The Calender in their birth month was : ")
    if isValidDate(day,month,year):
        return c.month(year,month)

#Part(f)
#Adding statements to the existing program to ask the user
#for a birth date of a person (day, month and year

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


#Now writng the main part to execute the program by using exception and handling

def main():
    try:
        n= input("Enter the day, month & year = ").split('-')

        d,m,y = int(n[0]),int(n[1]),int(n[2])
        print(dob(d,m,y))

        print(printCalendar(m,y))
    except ValueError:
        print("please enter data in this format (dd-mm-yyyy)")

    # Part F 
    try:
        d = int(input("Enter the day component of a DOB = "))
        m = int(input("Enter the month component of a DOB = "))
        y = int(input("Enter the year component of a DOB = "))
        print(dob(d,m,y))

        print(printCalendar(m,y))
    except ValueError:
        print("please enter valid date, month & year")


if __name__ =="__main__":
    main()
