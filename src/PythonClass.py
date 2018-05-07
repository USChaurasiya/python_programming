import src.Array as Array
import itertools

class PythonClass:
    def __init__(self):
        print("**************************Python Program For Class and Object***************************", '\n')

    def integertoromannumeral(self):
        print("Problem 1:: --------------------Integer To Roman Conversion----------------------", '\n')
        number = int(input("Enter Number : "))
        int_number = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        int_in_roman = ''
        i = 0
        while number > 0:
            for _ in range(number // int_number[i]):
                int_in_roman += roman_symbol[i]
                number -= int_number[i]
            i += 1
        print("Roman Equivalent of ", number, "is :: ", int_in_roman, '\n')
        return int_in_roman


    def romannumeraltointeger(self):
        print("Problem 2:: --------------------Roman To Integer Conversion----------------------", '\n')
        number = input("Enter Roman Number : ")
        roman_symbol = {'I': 1, 'V': 5, 'IX': 9, 'X': 10, 'L': 50, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        integer_value= 0
        for i in range(len(number)):
            if i > 0 and roman_symbol[number[i]] > roman_symbol[number[i - 1]]:
                integer_value += roman_symbol[number[i]] - 2 * roman_symbol[number[i - 1]]
            else:
                integer_value += roman_symbol[number[i]]
        print("Integer Value of ", number, "is :: ", integer_value, '\n')
        return integer_value


    def parenthesesvalidation(self):
        print("Problem 3:: --------------------Parenthesis Validation----------------------", '\n')
        string = input("Enter Expression to Validate Parenthesis: ")
        brackets_list = {"{", "[", "("}
        brackets_map = {"]": "[", "}": "{", ")": "("}
        stack = []
        for bracket in string:
            if bracket in brackets_list:
                stack.append(bracket)
            elif not stack:
                return False
            elif stack.pop() != brackets_map[bracket]:
                return False
        return not stack


    def findinguniquesubsest(self):
        print("Problem 4:: --------------------Finding All Unique Subsets of given Set----------------------", '\n')
        input_set = Array.Arraysample.inputarray(self)
        print("All Unique Subsets Of given Set ", input_set, "is ::", self.findsubsets([], sorted(input_set)), '\n')


    def findsubsets(self, current, in_set):
        if in_set:
            return self.findsubsets(current, in_set[1:]) + self.findsubsets(current + [in_set[0]], in_set[1:])
        return [current]


    def findingpair(self):
        print("Problem 5 : ---------Finding number Pair Having Sum equal to Specific Number-----------", '\n')
        numbers = Array.Arraysample.inputarray(self)
        first_index = 0
        second_index = 0
        target = int(input("Enter the Target Value : "))
        for x in range(numbers.__len__()):
            for y in range(numbers.__len__()-1):
                if numbers[x] + numbers[y] == target:
                    first_index = y
                    second_index = x
        print("Output :", first_index, ",", second_index)


    def elementssumequaltozero(self):
        print("Problem 6 : ---------Finding three number Having Sum equal to Zero-----------", '\n')
        numbers = Array.Arraysample.inputarray(self)
        # for x in range(numbers.__len__()):
        #     for y in range(numbers.__len__()-1):
        #         for z in range(numbers.__len__()-2):
        #             if numbers[x] + numbers[y] + numbers[z] == 0:
        #                 first_index = z
        #                 second_index = y
        #                 third_index = x
        # print("Output :", first_index, ",", second_index, ",", third_index)
        # numbers.sort(reverse=True)
        # for triplet in itertools.combinations(numbers, 3):
        #     if sum(triplet) == 0:
        #         print("::::", list(triplet))
        #         return list(triplet)
        # return []
        print("Input Array is : ", numbers)
        status = False
        for i in range(0, numbers.__len__() - 2):
            for j in range(i + 1, numbers.__len__() - 1):
                for k in range(j + 1, numbers.__len__()):
                    if (numbers[i] + numbers[j] + numbers[k] == 0):
                        print("Triplets Are :", numbers[i], numbers[j], numbers[k], '\n')
                        status = True
        if (status == False):
            print(" No Triplet Found Whose sum is Equal to Zero. ", '\n')

    def powercalculation(self):
        print("Problem 7 : ----------Implementation of Power Method-----------", '\n')
        base = int(input("Enter the Base Value: "))
        power = int(input("Enter the Power :"))
        print("Output : ", self.pow(base, power), '\n')


    def pow(self, base, power):
        if (power == 0):
            return 1
        elif (int(power % 2) == 0):
            return (pow(base, int(power / 2)) * pow(base, int(power / 2)))

        else:
            return (base * pow(base, int(power / 2)) * pow(base, int(power / 2)))
        print("Output ::", base)


    def reverse_string(self):
        print("Problem 8 : ----------Reversing The String Word-----------", '\n')
        string = input("Enter the String :")
        str = string.split(" ")
        print(str)
        rev_string = str.__reversed__()

        print("Reversed String : ", ' '.join(rev_string), '\n')

    def areaofrectangle(self):
        print("Problem 10 : ----------Reversing The String Word-----------", '\n')
        length = float(input("Enter the length of Rectangle :"))
        width = float(input("Enter the Width of Rectangle :"))
        area = length * width
        print("Area of the Rectangel is : ", area, '\n')
        return area


class Circle:
    def __init__(self, radius):
        print("Problem 11 : ----------Area and Perimeter of Circle-----------", '\n')
        self.radius = radius
        self.pi = 3.14
        print("Radius of Circle is :", radius)

    def areaofcircle(self):

        area = self.pi * self.radius * self.radius
        print("Area of Circle having radius ", self.radius, "is :", area)

    def perimeterofcircle(self):
        perimeter = 2 * self.pi * self.radius
        print("Perimeter of the Circle of radius ", self.radius, "is :", perimeter)