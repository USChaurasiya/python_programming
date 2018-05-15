import sys
import  pickle as pc
#import stemming.porter

#from stemming.porter2 import stem


Users = []


class User:
    def __init__(self):
        global  Users
        #self.name = input("Enter User Name: ")
        #self.date_of_birth = input("Enter the Date of birth : ")
        #self.status = bool(input("Enter the Status whether it is secret or not :"))
        # self.name = name;
        # self.date_of_birth = dob
        # self.status = status



    def adduser(self):
        number = int(input("How many User you want to add :"))

        for i in range(number):
            u = User()
            name = input("Enter User Name :")
            dateofbirth = input("Enter The Date of Birth :")
            status = input("Enter the Secret status (True/false) :")
            u.name = name
            u.date_of_birth = dateofbirth
            u.status = status
            Users.append(u)
            print(name, "Added Successfully......", '\n')

    def dobofuser(self):
        print("PY1 :: ---------------------Getting DOB by User name------------------")
        a = sys.argv[1]
        if a == self.name:
            print(self.date_of_birth)

    def secretuser(self):
        print("PY2 :: ---------------------Secret User------------------")
        a = sys.argv[1]
        for x in range(Users.__len__()):
            if Users[x].status == "True" and Users[x].name == a:
                print("Secret")
            else:
                print("")

class AddressBook:
    person_storage = {}
    address_list = []
    all_keys = []
    all_items = []
    status = False
    def __init__(self):

        global person_storage
        global address_list
        global all_keys
        global all_items
        global status
        pkl_file = open('pyproject.pkl', 'rb')
        AddressBook.person_storage = pc.load(pkl_file)

    def addpersontoaddressbook(self):
        print("------------------------Adding Person in Address book-----------------------", '\n')

        person = AddressBook()
        person.fname = sys.argv[1]
        person.lname = sys.argv[2]
        person.streetadd = sys.argv[3]
        person.city = sys.argv[4]
        person.state = sys.argv[5]
        person.country = sys.argv[6]
        person.mobile = sys.argv[7]
        person.email = sys.argv[8]



        if self.all_keys.__len__() == 0:
            AddressBook.address_list.append(person)
        else:
            for x in range(self.all_items.__len__()):
                if person.email not in self.all_items[x]:
                    AddressBook.address_list.append(person)
                    print(person.fname, " added successfully...")
                else:
                    self.status = True
        if self.status:
            print("Person is already Exist with either same Mobile or Email.")

        self.contacttodict(AddressBook.address_list)

        output = open('pyproject.pkl', 'wb')
        pc._dump(AddressBook.person_storage, output)
        print(AddressBook.person_storage)

    def contacttodict(self, list_of_contacts):
        for item in range(list_of_contacts.__len__()):
            AddressBook.person_storage[list_of_contacts[item].fname] =\
                (list_of_contacts[item].fname, list_of_contacts[item].lname, list_of_contacts[item].streetadd,
                 list_of_contacts[item].city, list_of_contacts[item].state, list_of_contacts[item].country,
                 list_of_contacts[item].mobile, list_of_contacts[item].email)


    def occurenceoffname(self):
        fname = input("Enter First Name :")
        print(AddressBook.person_storage)
