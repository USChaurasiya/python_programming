from collections import Counter

def sortingdict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print("Actual Dict Item :", mydict, '\n')
    print("Dict in ascending order :", '\n')
    a1_sorted_keys = sorted(mydict, key=mydict.get, reverse=False)
    for r in a1_sorted_keys:
        print(r, mydict[r])
    print('\n')
    print("Dict in descending order :")
    a1_sorted_keys = sorted(mydict, key=mydict.get, reverse=True)
    for r in a1_sorted_keys:
        print(r, mydict[r])

def addingkeyindict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print("Existing Dict: ", mydict, '\n')
    mydict.update({'uma': 99})
    print("Updated Dict :", mydict)

def concatenatemultipledict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    mydict1 = {'Gill': 10, 'Shah': 12, 'Joshef': 97, 'michel': 32}
    mydict2 = {'satya': 70, 'veejay': 78, 'stonish': 72, 'mark': 3}
    mydict4 = {}
    print("First Dict :", mydict, '\n')
    print("second Dict :", mydict1,'\n')
    print("Third Dict :", mydict2, '\n')

    for item in (mydict, mydict1, mydict2): mydict4.update(item)
    print("Concatenated Dict :", mydict4)

def iskeyalreadyexistindict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    keys = input("Enter the key Which you want to check :")
    if keys in mydict:
        print("Key is already exist in Dict")
    else:
        print("Key is not Present.")

def iteratedictusingloop():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    for key , value in mydict.items():
        print(key , value)

def dictcontainnumber():
    n = int(input("Input a number "))
    d = dict()

    for x in range(1, n + 1):
        d[x] = x * x

    print(d)

def squarethekeyvalue():
    # sample_dict = dict()
    # number = int(input("Enter the starting range:"))
    # last = input((input("Enter the End range :")))
    # for x in range(number, last):
    #     sample_dict[x] = x ** x
    # print(sample_dict)

    d = dict()
    for x in range(1, 15):
        d[x] = x ** 2
    print(d)

def mergetwodict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    mydict1 = {'Gill': 10, 'Shah': 12, 'Joshef': 97, 'michel': 32}
    print("First Dict :", mydict)
    print("Second Dict :", mydict1, '\n')
    mydict2 = mydict.copy()
    mydict2.update(mydict1)
    print("After merge: ", mydict2)

def sumofallitemindict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print("Given Dict : ", mydict)
    print("sum of all the dict value :", sum(mydict.values()), '\n')

def multiplyalldictvalue():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print("Given Dict :", mydict)
    multi_output = 1
    for key in mydict:
        multi_output = multi_output * mydict[key]
    print("Multiplication of dict value :", multi_output, '\n')

def removekeyfromdict():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print("Given Dict :", mydict)
    keys = input("Enter the key Which you want to delete :")
    if keys in mydict:
        del mydict[keys]
    else:
        print("Key not found")
    print("After removing key :", mydict)

def maptwolistintodict():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    print("Keys List :", keys)
    print("Values List :", values)
    color_dictionary = dict(zip(keys, values))
    print(color_dictionary)

def sortdictbykey():
    mydict = {'carl': 40, 'alan': 2, 'bob': 1, 'danny': 3}
    print("Input Dict :", mydict)
    for key in sorted(mydict):
        print("%s: %s" % (key, mydict[key]))

def combinetwodict():
    mydict = {'carl': 400, 'alan': 782, 'bob': 100, 'danny': 523}
    mydict1 = {'carl': 404, 'alan': 289, 'bob': 187, 'danny': 300}
    d = Counter(mydict) + Counter(mydict1)
    print(d)