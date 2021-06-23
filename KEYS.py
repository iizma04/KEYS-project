import pandas as pd 

df = pd.read_csv('PMC4177955-arizona-out.tsv')
 pandas.read_csv(PMC4177955-arizona-out.tsv, sep='\t') 
print(df)
df = df.drop(df.columns[[7, 8, 9, 10, 11, 12, 13, 14]], axis = 1)
print(df)
df = pd.read_csv("PMC4207242-arizona-out.tsv", sep='\t')
print(df)
df = df.drop(df.columns[[7, 8, 9, 10, 11, 12, 13, 14]], axis = 1)
print(df)

sr = pd.Series([''])
