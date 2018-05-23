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

class PersonAddressBook:
    person_address= {}
    def __init__(self):
        print("Inside PersonAddressBook")
        fname = {'fname': '', 'count': 0}
        lname = {}
        email = {'email': ''}
        mobile = {'mobile': ''}
        global person_address
        person_address = {'fname': {}, 'lname': {}, 'email': {}, 'mobile': {},
                          'address': {'streetaddress': [], 'city': [], 'state': [], 'country': []}}
        # self.writing_in_file(self, person_address)
        person_address = self.read_from_file()
        print(person_address)



    @staticmethod
    def writing_in_file(self, object):
        output = open('pyproject.pkl', 'wb')
        pc._dump(object, output)


    def read_from_file(self):
        pkl_file = open('pyproject.pkl', 'rb')
        b = pc.load(pkl_file)
        return b

    def add_person_in_address_book(self):

        ps = PersonAddressBook()
        fname = sys.argv[1]
        lname = sys.argv[2]
        streetadd = sys.argv[3]
        city = sys.argv[4]
        state = sys.argv[5]
        country = sys.argv[6]
        mobile = sys.argv[7]
        email = sys.argv[8]

        if PersonAddressBook.is_fname_present(self, fname, person_address):
            person_address['fname'][fname] += 1
        else:
            person_address['fname'].update({fname: 1})

        if PersonAddressBook.is_lname_present(self, lname, person_address):
            person_address['lname'][lname] += 1
        else:
            person_address['lname'].update({lname: 1})

        if city not in person_address['address']['city']:
            person_address['address']['city'].append(city)
        else:
            pass

        if state not in person_address['address']['state']:
            person_address['address']['state'].append(state)
        else:
            pass

        if country not in person_address['address']['country']:
            person_address['address']['country'].append(country)
        else:
            pass

        if not self.is_address_present( streetadd):
            person_address['address']['streetaddress'].append(streetadd)
        else:
           pass

        if email not in person_address['email']:
            person_address['email'].update({email: 1})
        else:
            print("Email Already Exist.")
            exit()

        if mobile not in person_address['mobile']:
            person_address['mobile'].update({mobile: 1})
        else:
            print("Mobile Already Exist.")
            pass

        PersonAddressBook.writing_in_file(self, person_address)

    def is_fname_present(self, fname ,address_dict):
        if fname in person_address['fname']:
            return True
        return False

    def is_lname_present(self, lname, address_dict):
        if lname in person_address['lname']:
            return True
        return False

    def is_address_present(self, streetaddress):
        for add in person_address['address']['streetaddress']:

            if self.test(streetaddress, add):
                return True
            else:
                return False


    def test(self, st, st1, threshold=0.5):
        stopwords = nltk.corpus.stopwords.words('english')
        stopwords.extend(string.punctuation)
        stopwords.append('')
        tokenizer = nltk.tokenize.TreebankWordTokenizer()
        stemmer = PorterStemmer()

        tokens_a = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(st) \
                    if token.lower().strip(string.punctuation) not in stopwords]
        tokens_b = [token.lower().strip(string.punctuation) for token in tokenizer.tokenize(st1) \
                    if token.lower().strip(string.punctuation) not in stopwords]

        # for token in tokens_a:
        #     print(stemmer.stem(token))
        stems_a = [stemmer.stem(token) for token in tokens_a]

        stems_b = [stemmer.stem(token) for token in tokens_b]

        ratio = len(set(stems_a).intersection(stems_b)) / float(len(set(stems_a).union(stems_b)))

        return (ratio >= threshold)

    def number_of_occurrence_fname(self):
        first_name = input("Enter the First Name to find the number of Occurrence: ")
        if first_name in person_address['fname']:
            print("Number of Occurrence of", first_name, "is :", person_address['fname'][first_name])
        else:
            print("First Name Not Present")

    def number_of_occurrence_lname(self):
        last_name = input("Enter the Last Name to find the number of Occurrence: ")

        if last_name in person_address['lname']:
            print("Number of Occurrence of", last_name, "is :", person_address['lname'][last_name])
        else:
            print('Last name Not present.')