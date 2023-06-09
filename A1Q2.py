##

# Task 2


#string input , search string , count 

m = input("Enter the string = ").lower()
# Making user input any sentence in form of string
# Function lower() is used to convert to lower case by default

n = input("Enter the search string = ").lower()
# Making user to enter the string to be searched and converting to lower case

print(f"No of times of word '{n}' = {m.count(n)}")
#Using count function to count no. of word appearing in that string
#Hey hows your day going? it is your birthday today
