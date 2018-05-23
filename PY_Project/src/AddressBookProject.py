import pickle as pc
import sys

class PersonAddressBook:
    person_address= {}
    def __init__(self):
        print("Inside PersonAddressBook")
        fname = {'fname': '', 'count': 0}
        lname = {}
        email = {'email': ''}
        mobile = {'mobile': ''}
        global person_address
        # person_address = {'fname': {}, 'lname': {}, 'email': {}, 'mobile': {},
        #                   'address': {'streetaddress': [], 'city': [], 'state': [], 'country': []}}
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

        person_address['address']['state'].append(state)
        person_address['address']['city'].append(city)
        person_address['address']['country'].append(country)
        person_address['address']['streetaddress'].append(streetadd)
        person_address['mobile'].update({mobile: 1})
        person_address['email'].update({email: 1})

        PersonAddressBook.writing_in_file(self, person_address)

    @staticmethod
    def is_fname_present(self, fname ,address_dict):
        if fname in person_address['fname']:
            return True
        return False

    def is_lname_present(self, lname, address_dict):
        if lname in person_address['fname']:
            return True
        return False