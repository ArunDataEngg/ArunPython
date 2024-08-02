'''
Exercise 6: Data Transformation


Normalize
the numerical features (sepal length, sepal width, petal length, petal
width) to a range of 0 to 1.
Create
a new column that is the ratio of petal length to petal width.

'''

import pandas as pd

df=pd.read_csv("iris.csv")
df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']] = (df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']] - df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']].min()) / (df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']].max() - df[['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width']].min())
print(df)

df['Petal.Ratio'] = df['Petal.Length'] / df['Petal.Width']
print(df)