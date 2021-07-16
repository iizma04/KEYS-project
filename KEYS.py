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

    import os 
import pandas as pd 
paper_path = "./2016 2/"

directory = os.fsencode(paper_path)
init_df = pd.DataFrame()
processed_none_controller_df = pd.DataFrame
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    init_df = pd.concat([init_df, pd.read_csv("./2016 2/"+filename, sep= "\t")])
   
  # just checking if this works and gives me the first 30 rows
  init_df.head(30)
  
  pattern = r'E[1-7-9]'

counter = 0 
output = ""
for row in df ['INPUT'].str.contains(pattern):
    if (row):
        output = df.iloc[counter, 1]
        df.iloc[counter, 0] = output[:-2]
        
        df.iloc[counter, 4].replace("Regulation", "Activation")
        if ((output[-1] == 'u') & (df.iloc[counter, 4] == 'Regulation (Positive)')):
            df.iloc[counter, 4].replace("Positive", "Negative")
        else:
            df.iloc[counter, 4].replace("Negative", "Positive")
    counter += 1
df[25:35]

def processed_data (df):
    file = file.drop(columns = cols[6:9])
    file = file[~file['OUTPUT'].str.contains('::uaz:')]
    file = file[~file['CONTROLLER'].str.contains('::uaz:')]
    return file

    display (processed_data (df))



import pandas as pd
import os 
def processed_data():
    for file in pd.read_csv("./2016 2/"+filename, sep= "\t"):
        file = file.drop(columns = cols[6:9])
        file = file[~file['OUTPUT'].str.contains('::uaz:')]
        file = file[~file['CONTROLLER'].str.contains('::uaz:')]
        return file
      
processed_data(pd.read_csv("./2016 2/"+filename, sep= "\t"))
