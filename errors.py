a = 'Hello World'
b = input("Enter character to search index = ")

try:
    print(a.index(b))
except ValueError:
    print("Inputted character is not found in the string")

# try:
#     pass
# except:
#     pass
# finally:
#     pass