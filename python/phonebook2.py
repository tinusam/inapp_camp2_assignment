class PhoneBook:

    def __init__(self, filename):
        self.filename = filename
        file = open(filename, "r")
        self.pb = dict()
        for line in file:
            contact = line.split()
            self.pb.update({contact[0]:contact[1]})
        file.close()

    def listContacts(self):
        print("Name\t\tPhone")
        for i in sorted(self.pb.keys()):
            print("{}\t\t{}".format(i, self.pb[i]))

    def addContact(self):
        name=input("enter the name")
        phno=int(input("enter the number"))
        if name not in self.pb.keys():
            self.pb.update({name:phno})
            print("1 entry added")
        else:
            print("entry exists")

    def searchByName(self, name):
        if name in self.pb.keys():
            print("entry found - ", name, "-", self.pb[name])
        else:
            print("entry not found")
    
    def searchByNumber(self, phno):
        if phno in self.pb.values():
            for k,v in self.pb.items():
                if phno == v:
                    name = k
                    break   
            print("entry found - ", name, "-", phno)
        else:
            print("entry not found")

    def deleteContact(self, name):
        if name in self.pb.keys():
            del self.pb[name]
            print("1 entry ({}) deleted".format(name))
        else:
            print("entry does not exist")

    def commit(self):
        file = open(self.filename, "w")
        for k,v in self.pb.items():
            file.write("{} {}\n".format(k,v))
        print("Committed edits")
        file.close()
# def phone_book("phonebook.txt"):
#         print('''
#         1. List all contacts
#         2. Add a new contact 
#         3. Delete a contact
#         4. Search by name 
#         5. Search by number
#         6. Exit''')
# while(True):
#     phone_book()
#     num = int(input("Enter option number :"))
#     p = PhoneBook()
#     match num:
#         case 1:p.listContacts()
#         case 2: p.addContact()
#         case 3: p.deleteContact()
#         case 4:p.searchByName()
#         case 5: p.searchByNumber()
#         case 6: break  


book = PhoneBook("phonebook.txt")
book.listContacts()
book.addContact()
book.commit()