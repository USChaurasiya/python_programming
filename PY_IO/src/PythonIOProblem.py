from itertools import islice
import linecache
import array
from collections import Counter
import os
from shutil import copyfile
import random


def readingfile(filename):
    print("----------------------------Reading Content of a file---------------------", '\n')
    content = open(filename)
    print("Content of given File is :", '\n')
    print(content.read(), '\n')

def readingnlinesfromfile(filename):
    print("----------------------------Reading n lines of content from file -------------------", '\n')
    linenumber = int(input("Enter the number of line :"))
    with open(filename) as file:
        for line in islice(file, linenumber):
            print(line, '\n')

def appendingtextinexistingfile(filename):
    print("-------------------Appending Text to existing file -------------------------------", '\n')
    with open(filename, "w") as existingfile:
        existingfile.write("Python program to append text to a file and display the text.\n")
    content = open(filename)
    print(content.read(), '\n')


def tail(filename):
    print("-------------------Reading last n line from file -------------------------------", '\n')
    nlines = int(input("Enter number of line:"))
    # count the total number of lines
    tot_lines = len(open(filename).readlines())
    # use line cache module to read the lines
    for i in range(tot_lines - nlines + 1, tot_lines + 1):
        print(linecache.getline(filename, i), '\n')

def readingfromfileandstoringinlist(filename):
    print("-------------------Reading content from file and store in list--------------------", '\n')
    content_list = []
    with open(filename) as file:
        # Content_list is the list that contains the read lines.
        content_list.append(file.readlines())
        print(content_list)

# def readingfromfileandstoringinarray(filename):
#     print("-------------------Reading content from file and store in Array--------------------", '\n')
#     content_array = array.array('b', [])
#     with open(filename) as file:
#         content_array.append(file.readlines())
#         print(content_array)

def longestwordinfile(filename):
    print("---------------------Finding Longest Word in file---------------------", '\n')
    with open(filename, 'r') as file:
        words = file.read().split()

    max_len = len(max(words, key = len))
    for word in words:
        if len(word) == max_len:
            print("Longest word is :: ", word, '\n')

def number_of_lines_in_file(filename):
    print("-------------------------------Number of lines in file -------------------------", '\n')
    num_lines = 0
    with open(filename, 'r') as file:
        for line in file:
            num_lines += 1
    print("Number of lines:", num_lines, '\n')

def frequency_of_word(filename):
    print("-------------------------------Frequency of word in file -------------------------", '\n')
    with open(filename) as f:
        print("Output : ",Counter(f.read().split()), '\n')

def file_size(fname):
    print("----------------------- File Size ----------------------", '\n')
    file_size = os.stat(fname)
    print("File Size is : ", file_size.st_size, '\n')

def writing_list_in_file():
    print("-----------------Writing List into File --------------", '\n')
    my_list = ['Task1', 'Task2', 'Task3', 'Task4', 'Task5']
    with open('file.txt', "w") as myfile:
        for x in my_list:
            myfile.write("%s\n" % x)

    openfile = open('file.txt')
    print("File ontent :", openfile.read())

def copycontent_from_file():
    print("-----------------------Copy Content of one file into other file ----------------------", '\n')
    copyfile('file.txt', 'copyoffile.txt')

def combine_from_onefileto_other():
    with open('textfile.txt') as file1, open('file.txt') as file2:
        for line1, line2 in zip(file1, file2):
            # line1 from abc.txt, line2 from test.txtg
            print(line1 + line2)

def reading_randomline(filename):
    lines = open(filename).read().splitlines()
    print(random.choice(lines))

def is_file_closed(filename):
    f = open(filename, 'r')
    print(f.closed)
    f.close()
    print(f.closed)