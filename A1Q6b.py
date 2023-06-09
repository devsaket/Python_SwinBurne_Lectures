##

#Task 6(b)

# Defining function adjust()

def adjust(a):
    if a>=0 and a<3:
        a=0
    elif a>=3 and a<8:
        a=5
    elif a>=8 and a<10:
        a=10
    return a
    

m = int(input("Enter a number "))
print("After Round off  = ",adjust(m))







#Task 6(b)

# Defining function roundoff()
# Using split and replace function in condition operator "if and else"



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

