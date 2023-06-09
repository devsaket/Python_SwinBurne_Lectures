# Program how to use append method to add items to a list

# Step 1:Create empty list

def main():
    name_list = []

    # Step 2: Create variable where names has to be added
    again = "Y"

    # Step3: Add some names to list
    while again == "Y":
        name = input("Enter the name")

        # Adding the name to list
        name_list.append(name)

        # Adding the another name to list
        print('Do you want to add another name?')
        again = input('Y = yes, anything else = no:')
        print()

    # Display the names that were entered

    print(" here are the names yuo entered")

    for name in name_list:
        print(name)


main()
