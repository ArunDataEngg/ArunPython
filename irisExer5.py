'''
Exercise 5: Data Aggregation


1. Calculate the mean, median, and standard deviation of petal length for each species.
2. Count the number of occurrences of each species.



3. Calculate the minimum and maximum petal width for
each species.


4. Find the species with the highest average sepal
width.

'''

import pandas as pd

df=pd.read_csv("iris.csv")
summary=df.groupby('Species')['Petal.Length'].mean()
print(summary)


species_counts = df['Species'].value_counts()
print(species_counts)

min_petalwidth=df.groupby('Species')['Petal.Width'].min()
print(min_petalwidth)


avg_sepal_width = df.groupby('Species')['Sepal.Width'].mean()
print("Species with highest average sepal width: ",max(avg_sepal_width))