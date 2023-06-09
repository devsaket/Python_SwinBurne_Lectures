# Infinite Loop
# i=0
# while True:
#     print(i)
#     i=i+1


# Simple calculator using infinite loop
# i=1
# while i>0:
#     print("Menu".center(60,'-'))
#     print(" + for addition\n- for subtraction")
#     m = input("Enter your choice = ")

#     if m is '+':
#         a = int(input("Enter first number = "))
#         b = int(input("Enter Second number = "))
#         c=a+b
#         print(f"sum of {a} & {b} = {c}")
#     elif m is '-':
#         a = int(input("Enter first number = "))
#         b = int(input("Enter Second number = "))
#         c=a-b
#         print(f"subtraction of {a} & {b} = {c}") 
#     else:
#         print("Invalid option")
    
#     i=int(input("Do you want to continue? press 0 to quit and press any key to continue "))

#     if i>0 or i<0:
#         i=1
#     else:
#         i=0



# continue keyword
# for i in range(1,100):
#     if i%5 == 0:
#         continue
#     print(i,end=" ")

# break keyword
# for i in range(1,100):
#     if i%5 == 0:
#         break
#     print(i,end=" ")



while True:
    print("Menu".center(60,'-'))
    print(" + for addition\n- for subtraction")
    m = input("Enter your choice = ")

    if m is '+':
        a = int(input("Enter first number = "))
        b = int(input("Enter Second number = "))
        c=a+b
        print(f"sum of {a} & {b} = {c}")
    elif m is '-':
        a = int(input("Enter first number = "))
        b = int(input("Enter Second number = "))
        c=a-b
        print(f"subtraction of {a} & {b} = {c}") 
    else:
        print("Invalid option")
    
    i=input("Do you want to continue? press 0 to quit and press any key to continue ")

    if i=='0':
        break