import pandas as panda
import numpy as numpy
import matplotlib.pyplot as plot

file = panda.read_csv('file.csv')
file.head()

print(file.isnull().sum())

NaNdelete = file.dropna().reset_index()
print(NaNdelete)

print(NaNdelete.isnull().sum())



