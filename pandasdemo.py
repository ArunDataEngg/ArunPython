'''
pandas is used for dataa analytics. Strong flexible python package which helps with data cleaning and wrangling tasks

adv:
    creates structured data similar to ms excel spreadsheet
    Reads data fro  various sources like csv, txt, xlsx, sql database etc..
    selects rows and column from dataset.
    arranging data in ascending and descending order
    filtering data
    aggregation or summerising data
    transpose data to wide and long format
    merging and concatenating two datasets


'''
import pandas as pd
import numpy as np

df=pd.read_csv("income.csv") #reading csv using pandas
income_dc=df.columns#all data columns from the income dataset
print(income_dc)

'''
#first 2 columns from income dataset
print(income_dc[:2])

#find datatypes for all the columns
print(df.dtypes)

df.Y2008=df.Y2008.astype(float) #converts integer to float
print(df.dtypes)

#print total number of rows and columns
print("total number of rows and columns: ",df.shape)
#print total number of rows
print("total number of rows: ",df.shape[0])

#print total number of columns
print("total number of rows: ",df.shape[1])

#print first five rows

print("First five rows of data set: ")
print(df.head())#by default 5

print("Last five rows of data set: ")
print(df.tail())#by default 5, for value, provide it in the () of tail/head

print(df.iloc[0:5])
print(df[0:5])

'''


#print distinct value of the column index
u_values= df.Index.unique()
#print(u_values,len(u_values))


#random sampling
data=df.sample(n=10) #getting 10 rows as sample from entire dataset


#print("Distinct values of the column index")
#multiple columns by name
#print(df[["Index","State","Y2008"]])
#------------------------------------------------------------
data = df.loc[:,["Index","State","Y2008"]]
#print(data)


data = df.loc[0:2,["Index","State","Y2008"]]
#print(data)
data = df.iloc[0:5,0:4]
#print(data)
Zodiac_data = pd.DataFrame({"Name":["John","Mary","Julia","Kenny","Henry"],
"Sunsign": ["Libra","Virgo", "Leo","Capricon","Aries"]})
#print(Zodiac_data)
#print(Zodiac_data.columns)
Zodiac_data.columns = ["Names","SunSigns"] #renaming the columns
#print(Zodiac_data)
Zodiac_data.rename(columns = {"Names":"Cust_Name"},inplace=True) #renaming the columns
#print(Zodiac_data)
df.columns = df.columns.str.replace('Y','Year')
#print(df.columns)
#print(df.head())
df.set_index("Index",inplace=True)
#print(df.columns)
#print(df.head())
df.reset_index(inplace=True)
#data = df.drop(['Index','State'],axis=1) #dropping columns Index and State
#data = df.drop(['Index',axis="columns") #dropping column Index
#print(data)
data = df.drop(0,axis=0) #removing first row
data = df.drop([0,1,2,4],axis=0)#removing multiple rows with given index
#print(data)
#print(df.sort_values("State",ascending=False))
#print(df.Year2008.sort_values())
#print(df.sort_values(["Index","State"]))





#print(df.describe()) #for 



df["difference"] =df.Year2008 - df.Year2009
print(df["difference"])

df["difference2"] =df.eval("Year2003-Year2002")
#print(df.head())

#df.ratio = df.Year2008/df.Year2009
#print(df.ratio)

data = df.assign(ratio = (df.Year2008/df.Year2009))
#print(data.head())

#print(df.describe()) #for numeric variables

#print(df.describe(include=['object'])) #only for strings/objects

#print(df.Year2008.mean(),df.Year2008.median(),df.Year2008.agg(["mean","median"]))

#print(df.Year2008.min())

#print(df.Year2008.agg(["mean","median","min"]))

#print(df.loc[:,["Year2002","Year2008"]].max())

#print(df.loc[df.Index=="A"])
""" Group By Functions """
#print(df.groupby("Index")["Year2002","Year2003"].min())

#print(df.groupby("Index")["Year2002","Year2003"].agg(["min","max","mean"]))

#print(df.groupby("Index").agg({"Year2002":[min,max],"Year2003": "mean"}))

dt = df.groupby("Index").agg({"Year2002":[min,max],"Year2003": "mean"})
dt.columns = ['Y2002_min', 'Y2022_max', 'Y2003_mean']
#print(dt)

#print(df.groupby(["Index","State"]).agg({"Year2002":[min,max],"Year2003": "mean"}))

""" Filtering """
#print(df[df.Index=="A"])

#print(df.loc[df.Index=="A"])#All the columns where Index ia A
#print(df.loc[df.Index=="A","State"])#only State column where index is A
#filter the rows with Index as A and salary greater than 15 lacs
#print(df.loc[(df.Index=="A")& (df.Year2002>1500000),:])
#filter the rows with index either A or W
print(df.loc[(df.Index=="A")|(df.Index=="W"),:])
##alternative
print(df.loc[df.Index.isin(["A","W"]),:])
#alternative

print(df.query("Year2002>1700000 & Year2003>1500000"))
