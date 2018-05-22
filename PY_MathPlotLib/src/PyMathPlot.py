import matplotlib.pyplot as matplot
from matplotlib.dates import date2num
import pandas as pnd
import pylab
import numpy as np
import datetime as dt

def draw_line_using_matlib():
    #Python program to draw a line with suitable label in the x axis, y axis and a title.

    x_value = range(1, 500)
    y_value = [x * 2 for x in x_value]

    matplot.plot(x_value, y_value)
    matplot.xlabel("X-Axis")
    matplot.ylabel("Y-Axis")
    matplot.title("Draw Line using MatPlot")
    matplot.show()

def draw_line_using_givenaxis_value():
    #Python program to draw a line using given axis values with suitable label in the x axis , y axis and a title.

    x_value = [1, 2, 7, 9, 10, 17, 20, 45]
    y_value = [6, 9, 10, 7, 17, 99, 41, 30]

    print("X axis Value :", x_value)
    print("Y axis value :", y_value)

    matplot.plot(x_value, y_value)
    matplot.xlabel("x-axis")
    matplot.ylabel("y-axis")
    matplot.title("Line with given value of x-axis and y-axis")
    matplot.show()

def draw_line_byreadingfrom_textfile():
    # Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis,
    # y axis and a title

    with open("math.text") as textfile:
        value = textfile.read()
    value = value.split('\n')
    x_value = [x.split(' ')[0] for x in value]
    y_value = [y.split(' ')[1] for y in value]
    print(x_value)
    print(y_value)
    matplot.plot(x_value, y_value)
    matplot.xlabel("x-axis")
    matplot.ylabel("y-axis")
    matplot.title("Line with given value of x-axis and y-axis")
    matplot.show()

def chart_for_financial_data():
    #Python program to draw line charts of the financial data of Alphabet Inc. between
    # October 3, 2016 to October 7, 2016
    f_data = pnd.read_csv('financialdata.csv', index_col=0, parse_dates=True)
    # print(f_data)
    # print(f_data.index)
    # print(f_data.columns)
    # f_data.plot(x=f_data.index, y=f_data.columns)
    # matplot.show()

def plot_moreline():
    # Python program to plot two or more lines on same plot with suitable legends of each line.

    x1 = [1, 7, 9]
    y1 = [28, 12, 15]

    x2 = [17, 22, 21]
    y2 = [48, 9, 3]
    # Draw Normal Line
    #matplot.plot(x1, y1, label ="line1")
    #matplot.plot(x2, y2, label="line2")

    # Drwa line with Different width and color
    # matplot.plot(x1, y1, label="line 1", color='blue', linewidth=3)
    # matplot.plot(x2, y2, label="line 2", color='red', linewidth=5)

    # Draw Dotted/dashed Line
    matplot.plot(x2, y2, label="line2", color='blue', linestyle='dotted')
    matplot.plot(x1, y1, label="line1", color='red', linestyle='dashed')


    matplot.xlabel("x-axis")
    matplot.ylabel("y-axis")
    matplot.title('Two or more lines on same plot with suitable legends ')
    matplot.legend()
    matplot.show()

def plot_line_with_marker():
    #Python program to plot two or more lines and set the line markers

    x_value = [15, 10, 9, 11, 17, 20]
    y_value = [11, 10, 17, 15, 11, 9]

    matplot.plot(x_value, y_value, color='red', linestyle='dashdot', linewidth=3,
             marker='o', markerfacecolor='blue', markersize=12)
    matplot.xlabel("x-axis")
    matplot.ylabel("y-axis")
    matplot.title('Plot with marker')
    matplot.show()

def plot_quantities():
    #Python program to plot quantities which have an x and y position.

    x1 = np.random.randint(50, size=10)
    y1 = np.random.randint(30, size=10)
    print(x1)
    x2 = np.random.randint(45, size=15)

    y2 = np.random.randint(20, size=15)

    #pylab.axis([0, 10, 0, 30])
    # matplot.plot(x1,y1)
    # matplot.plot(x2,y2)
    # matplot.show()
    pylab.plot(x1, y1, 'b*', x2, y2, 'ro')
    # show the plot on the screen
    pylab.show()

def plot_line_with_diff_format():
    #Python program to plot several lines with different format styles in one command using arrays.

    t = np.arange(0., 5., 0.5)
    matplot.plot(t, t, 'g--', t, t ** 2, 'bs', t, t ** 3, 'r^')
    matplot.show()

def multiple_type_chart():
    #Python program to create multiple types of charts (a simple curve and plot some quantities) on a single set of axes

    data = [(dt.datetime.strptime('2016-10-03', "%Y-%m-%d"), 772.559998),
            (dt.datetime.strptime('2016-10-04', "%Y-%m-%d"), 776.429993),
            (dt.datetime.strptime('2016-10-05', "%Y-%m-%d"), 776.469971),
            (dt.datetime.strptime('2016-10-06', "%Y-%m-%d"), 776.859985),
            (dt.datetime.strptime('2016-10-07', "%Y-%m-%d"), 775.080017)]

    x = [date2num(key) for (key, value) in data]
    y = [value for (date, value) in data]
    fig = matplot.figure()
    graph = fig.add_subplot(111)
    graph.plot(x, y, 'r-o')
    graph.set_xticks(x)
    graph.set_xticklabels(
        [date.strftime("%Y-%m-%d") for (date, value) in data]
    )
    matplot.show()

def creating_multiple_plot():
    # Python Program to create Multiple Plot
    fig = matplot.figure()
    fig.subplots_adjust(bottom=0.020, left=0.020, top=0.900, right=0.900)

    matplot.subplot(2, 1, 1)
    matplot.xticks(())
    matplot.yticks(())

    matplot.subplot(2, 3, 4)
    matplot.xticks(())
    matplot.yticks(())

    matplot.subplot(2, 3, 5)
    matplot.xticks(())
    matplot.yticks(())

    matplot.subplot(2, 3, 6)
    matplot.xticks(())
    matplot.yticks(())

    matplot.show()


def draw_bar_graph():
    x = ['JavaScript', 'Python', 'Java', 'Ruby', 'Php', 'C++', 'CSS']
    popularity = [23, 10, 9.8, 8.7, 5.59, 4.13, 3.35]
    x_pos = [i for i, _ in enumerate(x)]
    print(x_pos)
    matplot.bar(x_pos, popularity, color='blue')
    matplot.xlabel("Languages")
    matplot.ylabel("Popularity")
    matplot.title("Most Pull Request \n" + "From Github")
    matplot.xticks(x_pos, x)
    # # Turn on the grid
    matplot.minorticks_on()
    matplot.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    matplot.show()

def bar_graph_with_different_color():
    x = ['JavaScript', 'Python', 'Java', 'Ruby', 'Php', 'C++', 'CSS']
    popularity = [23, 10, 9.8, 8.7, 5.59, 4.13, 3.35]
    x_pos = [i for i, _ in enumerate(x)]
    matplot.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan', 'pink'])

    #matplot.bar(x_pos, popularity, color='blue')
    matplot.xlabel("Languages")
    matplot.ylabel("Popularity")
    matplot.title("Most Pull Request \n" + "From Github")
    matplot.xticks(x_pos, x)
    # # Turn on the grid
    matplot.minorticks_on()
    matplot.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    matplot.show()


def draw_pie_chart():
    languages = 'JavaScript', 'Python', 'Java', 'Ruby', 'Php', 'C++', 'CSS'
    popuratity = [23, 10, 9.8, 8.7, 5.59, 4.13, 3.35]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b", "#8c784b"]
    explode = (0.1, 0, 0, 0, 0, 0, 0)
    matplot.pie(popuratity, explode=explode, labels=languages, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    matplot.axis('equal')
    matplot.show()


def pie_chart_for_country():
    df = pnd.read_csv('medal.csv')
    country_data = df["country"]
    medal_data = df["gold_medal"]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0)
    matplot.pie(medal_data, labels=country_data, explode=explode, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    matplot.title("Gold medal achievements of five most successful\n" + "countries in 2018 Commonwealth Games")
    matplot.show()