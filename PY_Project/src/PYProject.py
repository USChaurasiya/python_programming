import sys

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