# Q6
# Merge BIG files

"""
Open the two input files
Open the output file for writing


top1 = the first line of input 1 
top2 = the first line of input 2

Repeat the following:

    if top1 is empty string (input 1 has been exhausted):
        Copy the rest of input 2 to the output file
        STOP repeating

    elif top2 is mepty string:
        Similar action to previous case

    elif top1 < top2:
        Write top1 to output
        top1 = the next line of input 1
        
    elif top2 < top1:
        Similar to previous case
        
    else (top1 is the same as top2)
        Write one of them to the output
        top1 = next line of input 1
        top2 = next line of input 2
        
Close the files
"""



f1 = open("names_set1.txt",'r')
f2 = open("names_set2.txt",'r')
f3 = open("names_output1.txt",'w')

top1 = f1.readline()
top2 = f2.readline()

while top1 or top2:
    if top1 =="":
        f3.write(top2)
        top2 = f2.readline()
    elif top2=="":
        f3.write(top1)
        top1 = f1.readline()
    elif top1<top2:
        f3.write(top1)
        top1 = f1.readline()
    elif top2<top1:
        f3.write(top2)
        top2 = f2.readline()
    else:
        f3.write(top2)
        top1= f1.readline()
        top2 = f2.readline()


f1.close()
f2.close()
f3.close()