import sys
import numpy as np
import pickle as pc
import pandas
from stemming.porter2 import stem
from nltk.stem import PorterStemmer
from openpyxl import workbook
import  porterstemmer
import nltk.corpus
#import nltk.tokenize.punkt
import nltk.stem.snowball
import string



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


        # AddressBook.set_key(AddressBook.person_storage, 'fname', person.fname)
        # AddressBook.set_key(AddressBook.person_storage, 'lname', person.lname)
        # AddressBook.set_key(AddressBook.person_storage, 'streetaddress', person.streetadd)
        # AddressBook.set_key(AddressBook.person_storage, 'city', person.city)
        # AddressBook.set_key(AddressBook.person_storage, 'state', person.state)
        # AddressBook.set_key(AddressBook.person_storage, 'country', person.country)
        # AddressBook.set_key(AddressBook.person_storage, 'mobile', person.mobile)
        # AddressBook.set_key(AddressBook.person_storage, 'email', person.email)
        #
        # output = open('pyproject.pkl', 'wb')
        # pc._dump(AddressBook.person_storage, output)
        # print(AddressBook.person_storage)

    def set_key(dictionary, key, value):
        if key not in dictionary:
            dictionary[key] = value

        elif type(dictionary[key]) == list and (value not in dictionary[key]):
            dictionary[key].append(value)

        elif type(dictionary[key]) == list and (value in dictionary[key]):
            pass
        else:
            dictionary[key] = [value]



    def occurenceoffname(self):
        first_name = input("Enter the name :")
        key = "fname"
        print(AddressBook.person_storage)
        counter = 0
        for k in AddressBook.person_storage:
            for x in range(AddressBook.person_storage.get(k).__len__()):
                if k == key and AddressBook.person_storage.get(k)[x] == first_name:
                    counter = counter + 1
                    # print("Number of occurrence of Given name is :", AddressBook.person_storage.get(k).__len__())
        print("Number of occurrence of Given first name is :", counter)




    def occurrenceoflname(self):
        last_name =input("Enter the last name :")
        key = "lname"
        counter = 0
        for k in AddressBook.person_storage:
            for x in range(AddressBook.person_storage.get(k).__len__()):
                if k == key and AddressBook.person_storage.get(k)[x] == last_name:
                    counter += 1
        print("Number of occurrence of Given last name is :", counter)


    def inputmatching(self):
        str2 = input("Enter the First String : ")
        str1 = input("Enter the second String : ")
        AddressBook.test(self, str2, str1)


    def test(self, st, st1,threshold=0.5):
        # st = "1st Main Road, 2nd Cross"
        # st1 = "1st Main2nd Cross"
        stopwords = nltk.corpus.stopwords.words('english')
        stopwords.extend(string.punctuation)
        stopwords.append('')
        tokenizer = nltk.tokenize.TreebankWordTokenizer()
        stemmer = PorterStemmer()

        tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(st) \
                  if token.lower().strip(string.punctuation) not in stopwords]
        tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(st1) \
                    if token.lower().strip(string.punctuation) not in stopwords]

        for token in tokens_a:
            print(stemmer.stem(token))
        stems_a = [stemmer.stem(token) for token in tokens_a]


        stems_b = [stemmer.stem(token) for token in tokens_b]

        ratio = len(set(stems_a).intersection(stems_b)) / float(len(set(stems_a).union(stems_b)))
        print(ratio >= threshold)
        return (ratio >= threshold)


def n_dimesional_array():
    data = np.arange(360).reshape((9, 4, 10))

    with open('test.txt', 'w') as outfile:
        outfile.write('# Array shape: {0}\n'.format(data.shape))

        for data_slice in data:
            np.savetxt(outfile, data_slice, fmt='%-7.2f')
            outfile.write('# New slice\n')


def readfromfile():

    new_data = np.loadtxt('test.txt')
    # Note that this returned a 2D array!
    new_data = new_data.reshape((9, 4, 10))

    print(new_data)
    # Just to check that they're the same...


def writing_inxcel():
    data = np.arange(36).reshape((9, 4))
    df = pandas.DataFrame(data)
    filepath = 'my_excel_file.xlsx'
    df.to_excel(filepath, index=False)




