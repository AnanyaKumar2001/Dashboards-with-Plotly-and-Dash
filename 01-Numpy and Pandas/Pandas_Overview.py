import pandas as pd
import numpy as np

df = pd.read_csv('salaries.csv')
print(df)
print(df['Name'])
print(df['Salary'])
print(df[['Name','Salary']])
print(df['Age'].mean())

ser_of_bool = df['Age'] > 30
print(ser_of_bool)

age_filter = df['Age'] > 30
print(df[age_filter])

df[df['Age'] > 30]
df['Age'].unique()
df['Age'].nunique()
df.info()
df.describe()
df.columns
df.index
mat = np.arange(50).reshape(5,10)
