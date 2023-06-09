#  In Python, there is no need for importing external libraries to read & write files.
# operations - 
    # reading
    # writing 
    # appending

# Types of file : -
        # Binary file 
        # Text file
            # text document
            # excel sheet
            # pdfs 

# f = open("file name",'file mode')

# file Modes 
#   operation                       file modes
    #   read                             r
    #   write                            w    # if the file doesnt exist then create a new one, if exists, then overwrite the content
    #   append                           a 
    #   read+                            r+   # opens a ile for both reading & writing. the file pointer placed at the beginning of the file 
    #   write+                           w+    #open a file for both writing & reading. Overwrites the existing file if thefile exists. if the file does not exist, create a new file for reading & writing
    # append+                            a+     ##open a file for both appending & reading. Overwrites the existing file if thefile exists. if the file does not exist, create a new file for reading & appending

f = open("cities.txt",'r+')
print(f.read())
f.seek(10)
print(f.read())
f.seek(25)
f.write(" Hello Sahil This is python Class ")
f.seek(0)
print(f.readlines()[0].index('Sahil'))
f.close()


# f = open('task','w')
# f.write("hii every one")
# f.close()


# f = open('task','a')
# f.write("Smiley")
# f.close()


# a=input("Enter A NAME = ")
# f = open('task','a')
# f.write(str(int(a)+ 45))
# f.close()


# f = open('task','a')
# a = float(input("Enter first number = "))
# b = float(input("Enter Second number = "))
# f.write(str(a) + ' ' + str(b))

# if a>b:
#     f.write(f"\n{a} is greater than {b}")
# else:
#     f.write(f"\n{b} is greater than {a}")

# f.close()