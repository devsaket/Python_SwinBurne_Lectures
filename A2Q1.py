#STUDENT ID : 20925390, First Name: Sahil, Last Name: Sharma
#Question 1 

#Build dictionary 
d =dict()

#Using exception handling if there's no file available in the give file

try:
    #Read the words from given text file by using readilnes
    f  = open('abbreviations.txt','r')
    li = f.readlines()

    for i in range(len(li)):
        li[i] = li[i].rstrip('\n')
        bli = li[i].split(':')
        d.update({bli[0]: bli[1]})

    #Printing the dictionary 
    print(d)
     
except FileNotFoundError:
    #Using exception handling if no file is available in the given file
    print("There is no file available with this name")

#Prompting user to input the message and then splitting
    
a= input("Enter text message = ")
a = a.split(' ')
print(a)

s = ''

for i in a:
    #Coverting all the user input to lower case,if input is in uppercase
    
    if i.lower() in d.keys():
        s = s + str(d.get(i.lower()))+' '
    else:
         s = s + str(i)+' '
#Picking the words from thr given text file and looking up in the dictionary to
#connstruct the plain English message with attached words typed after the abbrev.

print(s)
