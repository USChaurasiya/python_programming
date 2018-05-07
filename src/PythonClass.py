import itertools
import src.Array as Array


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

