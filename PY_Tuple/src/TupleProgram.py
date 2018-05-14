# A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses,
# whereas lists use square brackets. Creating a tuple is as simple as putting different comma-separated values.

def creatingtuple():

    sample_tuple = tuple()
    print(sample_tuple)

def tuplewithdifferentdata():
    data_tuple =("uma", 'shankar', 9999999999, True)
    print("Tuple with data:", data_tuple)

def tuplewithnumber():
    sample_tuple = 10, 15, 78, 99, 74
    print("Sample tuple:", sample_tuple)
    sample_tuple = 15,
    print(sample_tuple)

def unpacktupleitem():
    # create a tuple
    tuplex = 4, 8, 3
    print(tuplex)
    n1, n2, n3 = tuplex
    # unpack a tuple in variables
    print(n1 + n2 + n3)
    # the number of variables must be equal to the number of items of the tuple


def tupletostring():
    tup = ('Uma', 'shankar', 'Jaiswal', '99999999')
    str = ''.join(tup)
    print(str, '\n')

def listtotuple():
    sample_list = [12, 45, 74, 87, 96]
    print("Given List :", sample_list)
    tup = tuple(sample_list)
    print("List as tuple :", tup)

def sliceatuple():
    tup = ('Uma', 'shankar', 'Jaiswal', '99999999')
    print("Actual Tuple :", tup)
    sliced_tuple = tup[2:]
    print("Sliced Tuple :", sliced_tuple)

def lengthoftuple():
    tup = ('Uma', 'shankar', 'Jaiswal', '99999999')

    print("Length of tuple:",len(tup))

def tupletodict():
    sample_tuple = ((10, "uma"), (15, "shankar"), (20, "Jaiswal"))
    print("Given Tuple :", sample_tuple)
    print("Tuple as Dict:", '\n')
    print(dict((y, x) for x, y in sample_tuple))