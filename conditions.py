# if condition:
#     statement
# else:
#     statement


# a = float(input("Enter first number = "))
# b = float(input("Enter Second number = "))

# if a>b:
#     print(f"{a} is greater than {b}")
# else:
#     print(f"{b} is greater than {a}")


# a = float(input("Enter first number = "))
# b = float(input("Enter Second number = "))
# c = float(input("Enter Third number = "))

# if a>b and a>c:
#     print(f"{a} is greater than {b} and {c}")
# elif b>a and b>c:
#     print(f"{b} is greater than {a} and {c}")
# elif c>a and c>b:
#     print(f"{c} is greater than {a} and {b}")
# else:
#     print("All numbers are equal.")


# nested conditions 
# a= int(input("Enter a integer = "))

# if a%2==0:
#     print("div by 2")
# else:
#     print("not div by 2")


# if a%2==0 and a%3==0:
#     print("Div by 2 & 3")
# else:
#     print("Not div by 2 & 3")


# if a%2==0:
#     print("div by 2")
#     if a%3==0:
#         print("div by 3")
#     else:
#         print("not div by 3")
# else:
#     print("not div by 2")


# Leap year

# year %4 == 0 --> leap year
# a= int(input("Enter the year = "))

# if a%4==0:
#     if a%100==0:
#         if a % 400==0:
#             print("centurian Leap year")
#         else:
#             print("Not a centurian leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")



# a= int(input("Enter the year = "))
# if (a%4==0 and a%100!=0) or a%400==0:
#     print("Leap year")
# else:
#     print("Not a leap year")


# a= int(input("Enter a integer = "))

# if a%2==0 or a%3==0:
#     print("div by 2 or 3")
# else:
#     print("not div by 2 or 3")

# a= int(input("Enter a integer = "))
# if a%2==0:
#     print("div by 2")
# elif a%3==0:
#     print("div by 3")
# else:
#     print("not div by 2 or 3")


#  Q 19
# p=0
# id = input("Enter customer id = ")
# name= input("Enter customer name = ")
# unit = float(input("ENter the unit consumed = "))

# if unit>0 and unit<200:
#     p = unit * 1.20
# elif unit>=200 and unit<400:
#     p = unit * 1.50
# elif unit>=400 and unit<600:
#     p = unit * 1.80
# elif unit>=600:
#     p = unit * 2.00


# if p <100:
#     p=100
# elif p>=400:
#     p = p + p* 0.15

# print("Customer id = ",id)
# print("CUstomer name = ",name)
# print("Unit Consumed = ", unit)
# print("Total Bill = ", p)

# Q24
# a = int(input("Enter month number = "))
# if a == 1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
#     print("Month has 31 days")
# elif a==4 or a==6 or a==9 or a==11:
#     print("Month has 30 days")
# elif a==2:
#     print("Month has 28/29 days")
# else:
#     print("This number has no month defined ")

# q26

print("Menu".center(60,'-'))
print(" + for addition\n- for subtraction\n/ for division")
m = input("Enter your choice = ")

if m == '+':
    a = int(input("Enter first number = "))
    b = int(input("Enter Second number = "))
    c=a+b
    print(f"sum of {a} & {b} = {c}")
elif m == '-':
    a = int(input("Enter first number = "))
    b = int(input("Enter Second number = "))
    c=a-b
    print(f"subtraction of {a} & {b} = {c}") 
elif m == '/':
    # a = int(input("Enter first number = "))
    b = int(input("Enter Second number = "))
    try:
        c=a/b
    except NameError:
        print("Variable a is not defined")
        a = int(input("Enter first number = "))
        try:
            c=a/b
        except ZeroDivisionError:
            print("second value is invalid please enter any natural number")
            b = int(input("Enter Second number = "))
            c = a/b
    except ZeroDivisionError:
        print("second value is invalid please enter any natural number")
        b = int(input("Enter Second number = "))
        c = a/b
    finally:
        print(f"Division of {a} & {b} = {c}") 
else:
    print("Invalid option")