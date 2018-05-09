import sys
import datetime
import calendar

class PythonBasic:
    def __init__(self):
        print("******************************* Python Basic Program ***************************", '\n')

    def getversion(self):
        print("Python Version on My System is ::", sys.version, '\n')

    def currentdateandtime(self):
        print("Current Date and Time is : ", datetime.datetime.now(), '\n')

    def areaofcircle(self):
        radius = float(input("Radius of circle : "))
        area = 3.14 * (radius * radius)
        print("Area of Circle Having Radius ", radius, " is :: ", area)

    def reverseuserinput(self):
        firstName = input("First Name : ")
        lastName = input("Last Name : ")
        rev = lastName +" "+firstName
        print("User Name in Reverse Order : ", rev, '\n')

    def inputastupleandlist(self):
        element = input("Provide input separated by Comma :: ")
        ele = element.split(",")
        print("Input as List = ", ele, '\n')
        print("Input as Tuple = ", tuple(ele))

    def extentionoffile(self):
        fileName = input("Enter File Name :")
        extention_of_file = fileName.split(".")
        extention = str(extention_of_file[-1])
        print("Extention of given File is : ", extention)

    def gettingfirstandlastcolor(self):
        print("-------------------Color Problem ------------------------")
        color_list = ["Red", "Green", "White", "Black"]
        print("Color List :: ",color_list)
        print("First Color of List is :", color_list[0], " and Last color of list is : ", color_list[color_list.__len__()-1], '\n')

    def  examinationschedule(self):
        print("-------------------Examination Problem  ------------------------")
        examdate = (11, 12, 2014)
        print("Exam Date : ", examdate)
        print("The examination will start from : %i / %i / %i" % examdate, '\n')

    def acceptinteger(self):
        print("-------------------Integer Problem ------------------------")
        n = int(input("Enter Integer Value :"))
        n1 = int("%s" % n)
        n2 = int("%s%s" % (n, n))
        n3 = int("%s%s%s" % (n, n, n))
        result = n1+n2+n3
        print("Output of n+nn+nnn for ", n, " is", result, '\n')

    def printdocument(self):
        print("-------------------Document Problem------------------------")
        arg = float(input("Enter the Argument : "))
        print("Absolute value of Argument is : ", abs(arg), '\n')

    def printcalendar(self):
        print("-------------------Calendar Problem------------------------")
        month = int(input("Enter the Month : "))
        year = int(input("Enter the Year : "))
        print("The month", month, "th of", year,  "is :")
        print(calendar.month(year, month, 2, 1), '\n')

    def differencebtwdate(self):
        print("-------------------Date Difference Problem------------------------")
        dateinput = input("Enter the first Date in DD/MM/YYYY : ")
        dt = dateinput.split("/")
        year = int(dt[2])
        month = int(dt[1])
        date = int(dt[0])

        dateinput1 = input("Enter the Second Date in DD/MM/YYYY : ")
        dt1 = dateinput1.split("/")
        year1 = int(dt1[2])
        month1 = int(dt1[1])
        date1 = int(dt1[0])

        indate1 = datetime.date(year, month, date)
        indate2 = datetime.date(year1, month1, date1)
        print("Difference Between the ", dateinput, " and ", dateinput1, " is ", (indate2-indate1).days, "days", '\n')

    def volumeofsphere(self):
        print("-------------------Sphere Volume Problem------------------------")
        radius = float(input("Enter the radius :"))
        volume = (4/3)*(22/7)*radius*radius*radius
        print("Volume of the sphere having radius ", radius, "is", volume, '\n')

    def returndifference(self):
        print("------------------- Returning Difference Between Number and 17-------------------")
        number = int(input("Enter the Number: "))
        if number > 17:
            print(" Difference is :", (number-17)*2, '\n')
        else:
            print("Difference is :", abs(17-number), '\n')

    def sumofthreenumber(self):
        print("---------------Sum of Three Number, if Number will same it return Thrice of Number-----------------")
        number1 = int(input("Enter First Number:"))
        number2 = int(input("Enter Second Number:"))
        number3 = int(input("Enter Third Number:"))

        sumofnumber = number1 + number2 + number3
        if number1 == number2 == number3:
            sumofnumber = sumofnumber * 3

        print("Sum is: ", sumofnumber, '\n')

    def addingisbeforestring(self):
        print("----------------------- Adding IS as Suffix of Given String --------------------", '\n')
        string = input("Enter the String :")

        if len(string) >= 2 and string[:2] == "Is":
            print("Output String: ", string, '\n')
        string = "Is" + string
        print("Output String :", string, '\n')

    def copyofstring(self):
        print("----------------------- Creating n copy of String --------------------", '\n')
        string = input("Enter the String :")
        number_of_copy =int(input("Enter the Number of Copy :"))
        empty_string = ""
        for x in range(number_of_copy):
            empty_string = empty_string + string

        print("Output String : ", empty_string,  '\n')

    def findingevenandodd(self):
        print("----------------------Finding Even and Odd ---------------------", '\n')
        number = int(input("Enter the Number : "))
        status = False
        if number % 2 == 0:
            status = True

        if status:
            print(number, "is Even Number")
        else:
            print(number, "is Odd Number")

    def counting4inlist(self):
        print("-------------------Getting numbers of 4 in Given List---------------- ", '\n')
        list = []
        numberof4 = 0
        x = 4
        n = int(input("Enter the number of list Element :"))
        for i in range(n):
            element = int(input("Element :"))
            list.append(element)

        print("Given List :", list)
        for x in list:
            if x == 4:
                numberof4 = numberof4 + 1

        print("Number of 4 in list :", numberof4, '\n')

    def ncopyoffirsttwochar(self):
        print("---------------------------- Creating n Copy of First two Char------------------------")
        string = input("Enter the String :")
        n = int(input("Enter the Number of copy: "))

        first2char = string[:2]
        fnat_string = ""
        for i in range(n):
            fnat_string = first2char + fnat_string