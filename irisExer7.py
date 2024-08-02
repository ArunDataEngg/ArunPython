'''
Exercise 7: Advanced Data Aggregation

Calculate the 25th, 50th, and 75th percentiles of sepal length for each species.
Determine the range (max - min) of petal length for each species.

'''

import pandas as pd
df=pd.read_csv("iris.csv")

data = df.sample(frac=0.1) #sample of 10% of the entire dataset
print(data)

data = df.sample(frac=0.25) #sample of 10% of the entire dataset
print(data)

data = df.sample(frac=0.75) #sample of 10% of the entire dataset
print(data)


petal_length_range = df.groupby('Species')['Petal.Length'].agg(['min', 'max']).reset_index()
petal_length_range['Range'] = petal_length_range['max'] - petal_length_range['min']
print(petal_length_range[['Species', 'Range']])