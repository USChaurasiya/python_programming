import sys
import pickle as pc
from collections import Counter

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
    status = False
    def __init__(self):

        global person_storage
        global address_list
        global status
        #
        pkl_file = open('pyproject.pkl', 'rb')
        AddressBook.person_storage = pc.load(pkl_file)

    def addpersontoaddressbook(self):
        print("------------------------Adding Person in Address book-----------------------", '\n')
        keys = {"fname", "lname", "streetaddress", "city", "state", "country", "mobile", "email"}
        AddressBook.person_storage = dict([(key, []) for key in keys])
        person = AddressBook()
        person.fname = sys.argv[1]
        person.lname = sys.argv[2]
        person.streetadd = sys.argv[3]
        person.city = sys.argv[4]
        person.state = sys.argv[5]
        person.country = sys.argv[6]
        person.mobile = sys.argv[7]
        person.email = sys.argv[8]

        AddressBook.set_key(AddressBook.person_storage, 'fname', person.fname)
        AddressBook.set_key(AddressBook.person_storage, 'lname', person.lname)
        AddressBook.set_key(AddressBook.person_storage, 'streetaddress', person.streetadd)
        AddressBook.set_key(AddressBook.person_storage, 'city', person.city)
        AddressBook.set_key(AddressBook.person_storage, 'state', person.state)
        AddressBook.set_key(AddressBook.person_storage, 'country', person.country)
        AddressBook.set_key(AddressBook.person_storage, 'mobile', person.mobile)
        AddressBook.set_key(AddressBook.person_storage, 'email', person.email)

        output = open('pyproject.pkl', 'wb')
        pc._dump(AddressBook.person_storage, output)
        print(AddressBook.person_storage)

    def set_key(dictionary, key, value):
        if key not in dictionary:
            dictionary[key] = value

        elif type(dictionary[key]) == list and (value not in dictionary[key]):
            dictionary[key].append(value)

        elif type(dictionary[key]) == list and (value in dictionary[key]):
            pass
        else:
            dictionary[key] = [value]

    # def occurenceoffname(self):
    #     print(list(AddressBook.person_storage))


