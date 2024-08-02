'''
Exercise 9: Applying Custom Functions


Create
a custom function that categorizes flowers as 'small', 'medium', or
'large' based on petal length.
Apply
this function to create a new column in the dataset.
'''

import pandas as pd
df=pd.read_csv("iris.csv")
def categorize_petal_length(petal_length):

    if petal_length < 3:

        return 'small'

    elif petal_length < 5:

        return 'medium'

    else:

        return 'large'


# Apply the custom function to create a new column in the dataset

df['Petal Size'] = df['Petal.Length'].apply(lambda x: categorize_petal_length(x))


print(df.head())