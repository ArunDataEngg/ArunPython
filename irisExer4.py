'''
Exercise 4: Data Filtering


Filter
the dataset to include only rows where the sepal length is greater than
5.0.
Filter
the dataset to include only rows of the species 'Setosa'.
'''



import pandas as pd

df=pd.read_csv("iris.csv")

print(df.loc[df['Sepal.Length'] > 5.0])

print(df.loc[df['Species']=="setosa"])