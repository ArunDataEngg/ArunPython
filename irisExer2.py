'''Exercise 2: Summary Statistics


1.     
Calculate summary statistics for each feature.


2.     
Calculate the mean sepal length for each
species.
'''
import pandas as pd

df=pd.read_csv("iris.csv")
summary=df.describe()
#print(summary)

#meanSepal=df.mean()
#print(meanSepal)
mean_sepal_length = df.groupby('Species')['Sepal.Length'].mean()


# Print the result

print(mean_sepal_length)