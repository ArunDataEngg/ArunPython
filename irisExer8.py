'''
Exercise 8: Merging and Joining


Create
a new DataFrame with additional information about each species (e.g.,
typical habitat).
Merge
this new DataFrame with the original Iris DataFrame.

'''

import pandas as pd
df=pd.read_csv("iris.csv")
species_info = pd.DataFrame({

    'Species': ['setosa', 'versicolor', 'virginica'],

    'Habitat': ['mountain meadows', 'woodlands', 'swamps'],

    'Distribution': ['worldwide', 'North America', 'North America']

})


merged_df = pd.merge(df, species_info, on='Species')


print(merged_df.head())