# import sys
# for line in sys.stdin:
#     print(line.title(),end='')


# import sys
# j = ''
# for line in sys.stdin:
#     line = line.rstrip('\n') 
#     strSplit = line.split(" ")
#     longestWord = 0
    
#     for i in strSplit:
#         if len(i) == longestWord:
#             continue
#         if len(i)>longestWord:
#             longestWord = len(i)
#             j=i
#     print(j)


# import sys
# for line in sys.stdin:
#     l = line.split('|')
#     m = l[0].rstrip(' ')
#     m = m.split(' ')
#     l[1]= l[1].lstrip(' ')
#     n= l[1].rstrip('\n')
#     n = n.split(' ')
#     for x in range(len(m)):
#         m[x] = int(m[x])
#         n[x] = int(n[x])


#     for i in range(len(m)):
#         print(m[i]*n[i], end=" ")

#     print("")


# import itertools
# import sys

# def Permutations(Lst,size):
#     return list(itertools.permutations(Lst,size))

# def expression(lst1,lst2):
#     for x in lst1:
#         for i in lst2:
#             op1=i[0]
#             op2=i[1]
#             op3=i[2]
#             op4=i[3]
        
#             str1=str(x[0])+op1+str(x[1])
#             str2=str(str1)+op2+str(x[2])
#             str3=str(str2)+op3+str(x[3])
#             str4=str(str3)+op4+str(x[4])
#             exp=eval(str4)

#             if(exp==42):
#                 return True
#     return False

# for line in sys.stdin:
#     NumPermutations=Permutations(line,5)
#     Operators=['+','-','*','+','-','*']
#     OpPermutations=Permutations(Operators,4)
#     Result=expression(NumPermutations,OpPermutations)

#     if(Result==True):
#         print("\nYES")
#     else:
#         print("\nNO")



import itertools
import sys

def Permutations(Lst,size):
    return list(itertools.permutations(Lst,size))

def expression(lst1,lst2):
    for x in lst1:
        for i in lst2:
            op1=i[0]
            op2=i[1]
            op3=i[2]
            op4=i[3]

            str1=str(x[0])+op1+str(x[1])
            str2=str(str1)+op2+str(x[2])
            str3=str(str2)+op3+str(x[3])
            str4=str(str3)+op4+str(x[4])
            exp=eval(str4)

            if(exp==42):
                return True
    return False


Numbers = []
for line in sys.stdin:
    numbers = line.split(' ')

    for i in numbers:
        Numbers.append(int(i))

    NumPermutations=Permutations(Numbers,5)

    Operators=['+','-','*','+','-','*']

    OpPermutations=Permutations(Operators,4)

    Result=expression(NumPermutations,OpPermutations)

    if(Result==True):
        print("\nYES")
    else:
        print("\nNO")