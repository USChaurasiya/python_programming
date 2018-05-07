import pandas
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import tkinter

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

print(dataset.shape)
print(dataset.head(20))
print(dataset.describe())
print(dataset.groupby('class').size())
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
dataset.hist()
scatter_matrix(dataset)
plt.show()