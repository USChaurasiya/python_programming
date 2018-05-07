from array import *
from collections import Counter

def display(a):
    print("Array Element", a)
num_array = []

array_exp = array('d', [55,56,78,99,782])

class Arraysample:

    def __init__(self):
        global array_exp
        self.type = input("Type of Array : ")

    def inputarray(self):
        num = input("Enter how many elements you want:")
        print
        'Enter numbers in array: '
        for i in range(int(num)):
            n = int(input("num :"))
            num_array.append(int(n))
        display(num_array)

    def elementbyindex(self):

        print("Num Array :", num_array)
        print
        'Enter the index to find Element from Array : '
        index = int(input("index : "))
        print("Value at ", index)
        print(num_array[index])

    def appendelementatend(self):
        number = int(input("Enter number to append :"))
        num_array.append(number)
        print
        'Array after Appending element : '
        display(num_array)

    def reversearrayelement(self):
        print
        'Reversed Array :'
        display(num_array[:: -1])

    def lengthinbyte(self):

        print("Length in bytes of one array item :", array_exp.itemsize)

    def getcurrentmemoryaddress(self):
        print("Array info :", array_exp.buffer_info())
        print("Memory Buffer in byte: " +str(array_exp.buffer_info()[1] * array_exp.itemsize))

    def numberofoccurence(self):
        number = int(input("Enter number to get occurrences :"))
        print(Counter(num_array))
        print("Number of Occurrence of ", number, " is :: ", num_array.count(int(number)))

    def appenditemtotheendofarray(self):

        print("Array before Appending the element :",num_array)
        num_array.extend(num_array)
        print("Array after Appending the element :", num_array)

    def converttobyte(self):
        byte_array = array_exp.tobytes()
        print("Byte Array : ", byte_array)

    def appendfromspecifiedlist(self):
        print("Array before Appending the specified list :", num_array)
        num_array.extend(array_exp)
        print("Array after Appending the specified list :", num_array)

    def insertelementatspecificposition(self):
        index = int(input("Enter the specific index :"))
        element = int(input("Enter the element to insert in given array : "))
        print("Array before inserting the element :", num_array)
        num_array.insert(index, element)
        print("Array after inserting the element at ", index, "is ", num_array)

    def deleteelementbyindex(self):
        index = int(input("Enter the Index of element :"))
        print("Array before Deleting the element :", num_array)
        num_array.pop(index)
        print("Array after Deleting the element from ", index, "is ", num_array)

    def arraytolist(self):
        print("Given Array :", array_exp)
        array_list = array_exp.tolist()
        print("Array as List :", array_list)



