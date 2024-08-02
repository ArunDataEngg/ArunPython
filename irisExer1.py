'''Exercise 1: Load and Inspect the Data


1.     
Load the Iris dataset from a CSV file.


2.     
Display the first 10 rows of the dataset.


3.     
Display the data types of each column.
'''

import pandas as pd
#1
df=pd.read_csv("iris.csv")
ir_dc=df.columns
print(df.shape)
print(df.iloc[:])

#2
print(df.iloc[:10])

#
print(df.dtypes)
