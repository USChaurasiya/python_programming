import numpy as np

num_array = []

class NumpyExample :

    def __init__(self):
        global num_array
        print("Inside NumpyProgram Class ::")

    def getversionofnumpy(self):
        print("Version of Numpy on System is :", np.__version__)

    def listtonumpyarray(self):
        num = input("Enter how many elements you want:")
        print
        'Enter numbers in array: '
        for i in range(int(num)):
            n = int(input("num :"))
            num_array.append(int(n))

        print("List of Numeric value :: ", num_array)
        arr = np.array(num_array)
        print("One-dimensional NumPy array :: ", arr)

    def creatematrix(self):
        mat = np.arange(2, 11)
        finalmatrix = mat.reshape(3, 3)
        print(finalmatrix)

    def nullvector(self):
        nullvec = np.zeros(10, 'd')
        print("Null Vector :: ", nullvec)
        nullvec[6] = 11
        print("Modified Null Vector :: ", nullvec)

    def arraywithvalueinrange(self):
        start = int(input("Enter the First Number :: "))
        end = int(input("Enter the Last Number :: "))
        num_array = np.arange(start, end, 1)
        print("Array having value between  ", start, "and ", end, " is ::", num_array)

    def reversingarray(self):
        num_array = np.arange(1, 25, 1)
        print("Reversed Array using Numpy :: ", num_array[::-1])


