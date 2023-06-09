##

#Question 2 : Merging big files

#Opening two files f1 and f2 in readmode
f1=''
f2 = ''

try:
    f1 = open("names_set1.txt",'r')
except FileNotFoundError:
    #Using exception handling if no file is available in the given file
    print("There is no file available with this name")
    
try:
    f2 = open("names_set2.txt",'r')
except FileNotFoundError:
    #Using exception handling if no file is available in the given file
    print("There is no file available with this name") 


#Output file f3 in write mode and used for merging files f1 and f2
f3 = open("names_merged_big.txt",'w')

#top1 and top2 are used for frist line of input 1 and input 2 resectively by
#using readline method

top1 = f1.readline()
top2 = f2.readline()

#Using while loop and if condition concept

while top1 or top2:
    #If top1 is empty string then copy the rest of input 2 to output file
    if top1 =="":
        f3.write(top2)
        top2 = f2.readline()
    #If top2 is empty string then copy the rest of input 2 to output file    
    elif top2=="":
        f3.write(top1)
        top1 = f1.readline()

    #In this case we write top1 to output
    elif top1<top2:
        f3.write(top1)
        top1 = f1.readline()
        
     #In this case we write top2 to output    
    elif top2<top1:
        f3.write(top2)
        top2 = f2.readline()

    #In this case top1 is sane as top2 and one of them is written to output
    else:
        f3.write(top2)
        top1= f1.readline()
        top2 = f2.readline()


#Close all the files
        
f1.close()
f2.close()
f3.close()
