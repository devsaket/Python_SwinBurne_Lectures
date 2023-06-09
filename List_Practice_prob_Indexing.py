# Example for getting the index of item and replacing it with new item in list

def main():
    #Step 1 : Create List
    phone_list = ["Apple", "Samsung", "Blackberry", "Nokia", "Oppo"]
    print(phone_list)


    #Step 2 : add the item to be added to list
    phone_replacement = input(" enter the phone to be replaced :")

    if phone_replacement in phone_list:
        phone_replacement_index= phone_list.index(phone_replacement)
        new_phone= input(" enter the phone to be added to list ")
        phone_list[phone_replacement_index]= new_phone
    
        print(" The new list for updated phones" )
        print(phone_list)
    else:
       print("That item was not found in the list")
    
    # try:
    #     phone_replacement_index= phone_list.index(phone_replacement)
    #     new_phone= input(" enter the phone to be added to list ")
    #     phone_list[phone_replacement_index]= new_phone
    
    #     print(" The new list for updated phones" )
    #     print(phone_list)
        
    # except ValueError:
    #    print("That item was not found in the list")



if __name__ == '__main__':
    main()

#Step 3 : Index for item to be replaced
# Step 4 : New Item to be added to the list
# Step 5 : Repalce the old item with new item

# phone_list = ["Apple", "Samsung", "Blackberry", "Nokia", "Oppo"]
# print(phone_list)
# phone_replacement= input(" enter the phone to be updated to list ")
# phone_replacement_index= phone_list.index(phone_replacement)
# new_phone= input(" enter the phone to be added to list ")
# phone_list[phone_replacement_index]= new_phone
    
# print(" The new list for updated phones" )
# print(phone_list)