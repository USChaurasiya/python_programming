import numpy as np
import pickle as pc
import time
import os



class NpArray:
    def __init__(self):
        self.type = input("Type of Array : ")

    def createarray(self):
        print("Problem 1:: --------------------Creating NP Array And Initialize to 1----------------------", '\n')
        a = np.ones((3, 3), 'int32', 3)
        b = np.divide(a, 2)
        print("Array of int32 having shape (3,2) with initial value 0 :: ")
        print('\n')
        print(b, '\n ')

    def createtuple(self):
        print("Problem 2:: --------------------Tuple having 5 Element----------------------", '\n')
        tuple1 = (1000, 501, 57)
        tuple2 = (1001, 502, 58)
        tuple3 = (1102, 503, 45)
        tuple4 = (1054, 504, 50)
        tuple5 = (1078, 505, 10)

        tuple7 = (tuple1, tuple2, tuple3, tuple4, tuple5)
        print("Original Tuple :: ", '\n', tuple7, '\n')
        b = np.asarray(tuple7)
        print("Tuple as numpy array :: ", '\n', b)

    def matrixrandominit(self):
        print("Problem 3:: --------------------Random Initialization of Matrix----------------------", '\n')
        random_matrix = np.random.rand(3, 3)*10
        t1 =time.time()
        print("First Matrix :: ")
        for i in range(2):
            print(random_matrix[i])

        random_matrix1 = np.random.rand(3, 3) * 10
        print("Second Matrix :: ")
        for i in range(2):
            print(random_matrix1[i])
        #multiplication =np.multiply(random_matrix, random_matrix1)
        #print("Time using Np :" , t2-t1)
        multiplication = NpArray.matrixmultiplication(self, random_matrix, random_matrix1)
        print("Multiplication of matrix :: ", '\n', np.asarray(multiplication))

    def matrixmultiplication(self, matrix1, matrix2):
        print(" --------------------Matrix Multiplication without Numpy---------------------", '\n')
        t1 = time.time()
        result = [[0 for row in range(len(matrix1))] for col in range(len(matrix2[0]))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        t2 = time.time()
        NpArray.persistdataondisk(self, result)
        pkl_file = open('myfile.pkl', 'rb')
        mydict = pc.load(pkl_file)
        print("time taken :", t2-t1)
        print("Output from Dump file ::", '\n', np.asarray(mydict))
        return result


    def persistdataondisk(self,obj):
        print(" -------------------Persisting Data on Disk using Pickle-----------------------", '\n')
        output = open('myfile.pkl', 'wb')
        pc._dump(obj, output)
        output.close()


    def printcurrentdirectory(self):

        print(os.listdir())

    def multi(self):
        matrix = np.zeros([1200, 50], int)
        a = np.random.randint(0, 500, 1200)
        b = np.reshape(a, (-1, 50))
        print(b)
       

