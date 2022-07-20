def phone_book():
        print('''
        1. List all contacts
        2. Add a new contact 
        3. Delete a contact
        4. Search by name 
        5. Search by number
        6. Exit''')

phonebook=dict()

while(1):
    phone_book()
    num = int(input("Enter option number :"))
    if num==1:
        names = sorted(phonebook.keys())
        for key in names:
            print(key)

    if num==2:
        #Add a new contact
        name = input("Enter the name :")
        phone_number = input("Enter the phone number :")
        phonebook[name] = phone_number
        print("Contact {} : {} added to phone book".format(name,phone_number))
  
    if num==3:
         #Delete a contact
        name = input("Enter the name to delete :")
        if name in phonebook.keys():
            del phonebook[name]
            print("contact {} deleted".format(name))
        else:
                print("No name exited")

    if num==4:
            #seach by contact by name
            name = input("Enter the name to search: ")
            if(name in phonebook.keys()):
                print("{}-{}".format(name,phonebook[name]))
            else:
                print("No contacts exited")
    if num==5:
            #search by number
            number = input("Enter the phone number:")
            numbers = list(phonebook.values())
            if(number in numbers):
                position = numbers.index(number)
                names = list (phonebook.keys())
                print(names[position])
            else:
                print("number not found!")
    if num==6:
            print("Program Exited!")
            break


        



