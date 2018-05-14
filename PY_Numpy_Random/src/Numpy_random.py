import numpy as np

def generating_random_number():
    random_number = np.random.normal(size=5)
    print("Generated number :", random_number)

def randomnumberbtwrange():
    random_number = np.random.randint(low =10, high=30, size=6)
    print("Output :" , random_number)

def matrixwith_randomnumber():
    matrix = np.random.random((3, 3, 3))
    print("Matrix with random value :", matrix)

def max_nim_frommatrix():
    matrix = np.random.random((5, 5, 5))
    print("Matrix :", matrix)
    max_value = matrix.max()
    min_value = matrix.min()

    print("Maximum value in matrix :", max_value)
    print("Minimum Value in matrix :", min_value)

def extract_from_array():
    arr = np.random.rand(10, 4)
    extracted_value = arr[:5, :]
    print("Actual Array :", arr)
    print("Extracted Arry :", extracted_value)

def suffle_number():
    arr = np.arange(10)
    print("Generated array  :", arr)
    np.random.shuffle(arr)
    print("Value after suffle :",arr)

def normalize_matrix():
    matrix = np.random.random((3, 3))
    print("Original Array:")
    print(matrix)
    xmax, xmin = matrix.max(), matrix.min()
    matrix = (matrix - xmin) / (xmax - xmin)
    print("After normalization:")
    print(matrix)

def sorting_random_vector():
    rand_vector = np.random.random(10)
    print("Random Vector :", rand_vector)
    rand_vector.sort()
    print("Sorted vector :", rand_vector)

def check_two_randomarray():
    first_array = np.random.randint(0, 2, 6)
    second_array = np.random.randint(0, 2, 6)
    print("First Array :", first_array)
    print("Second array :", second_array)

    is_equal = np.allclose(first_array, second_array)
    print("Whether Given arrays are equal or not :", is_equal)

def replace_max_value():
    x = np.random.random(15)
    print("Original array:")
    print(x)
    x[x.argmax()] = -1
    print("Maximum value replaced by -1:")
    print(x)

def most_frequent_value():
    num_array = np.random.randint(10, 30, 20)

    print("Given array", num_array)
    print("Most frequent value in the above array:")
    print(np.bincount(num_array).argmax())

def finding_closest_value():
    x = np.arange(100)
    print("Original array:")
    print(x)
    a = np.random.uniform(0, 100)
    print("Value to compare:")
    print(a)
    index = (np.abs(x - a)).argmin()
    print(x[index])