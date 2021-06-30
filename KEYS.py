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

temp = list.files(pattern="*.csv")
myfiles = lapply(temp, read.delim)

path = r'C:\Users\izmasyed\Desktop\KEYS project\2016 2'
all_files = glob.glob(path + "/*.csv")

import csv
import os
data_files = os.listdir('/Users/izmasyed/Desktop/KEYS project/2016 2')
def load_files(filenames):
    for file in filenames:
        yield pd.read_csv(filename)
        
     
     import pandas as pd
from glob import glob

stock_files = sorted(glob('arizona-out*.tsv'))

dfs = []

for filename in os.listdir(directory):
    if filename.endswith(".tsv"):
        pandas.concat(filename)
