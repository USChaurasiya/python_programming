from array import *
from collections import Counter

def display(a):
    print("Array Element", a)

num_array = [1,2]  #List

array_exp = array('d', [])  #Array

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
            array_exp.append(n)
            #num_array.append(int(n))       #for List
        print(id(array_exp))
        return array_exp

        display(array_exp)

    def elementbyindex(self):

        print("Num Array :", array_exp)
        print
        'Enter the index to find Element from Array : '
        index = int(input("index : "))
        print("Value at ", index)
        print(array_exp.__getitem__(index))

    def appendelementatend(self):
        number = int(input("Enter number to append :"))

        #for List
        #num_array.append(number)
        array_exp.append(number)
        print
        'Array after Appending element : '
        display(array_exp)

    def reversearrayelement(self):
        print
        'Reversed Array :'
        #display(num_array[:: -1]) # for List
        array_exp.reverse()
        display(array_exp)

    def lengthinbyte(self):

        print("Length in bytes of one array item :", array_exp.itemsize)

    def getcurrentmemoryaddress(self):
        print("Array info :", array_exp.buffer_info())
        print("Memory Buffer in byte: " + str(array_exp.buffer_info()[1] * array_exp.itemsize))

    def numberofoccurence(self):
        number = int(input("Enter number to get occurrences :"))
        print("Number of Occurrence of ", number, " is :: ", array_exp.count(number))

    def appenditemtotheendofarray(self):

        print("Array before Appending the element :", array_exp )
        array_exp.extend(array_exp)
        print("Array after Appending the element :", array_exp)

    def converttobyte(self):
        byte_array = array_exp.tobytes()
        print("Byte Array : ", byte_array)

    def appendfromspecifiedlist(self):
        print("Array before Appending the specified list :", array_exp)
        array_exp.extend(num_array)
        print("Array after Appending the specified list :", array_exp)

    def insertelementatspecificposition(self):
        index = int(input("Enter the specific index :"))
        element = int(input("Enter the element to insert in given array : "))
        print("Array before inserting the element :", array_exp)
        array_exp.insert(index, element)
        print("Array after inserting the element at ", index, "is ", array_exp)

    def deleteelementbyindex(self):
        index = int(input("Enter the Index of element :"))
        print("Array before Deleting the element :", array_exp)
        array_exp.pop(index)
        print("Array after Deleting the element from ", index, "is ", array_exp)

    def arraytolist(self):
        print("Given Array :", array_exp)
        array_list = array_exp.tolist()
        print("Array as List :", array_list)



