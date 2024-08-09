import pandas as pd 
import os
import json

with open("config.json") as f:
    config = json.load(f)  
# Read and store content 
# of an excel file  
read_file = pd.read_excel(config["csv_file"].split('.')[0]+".xlsx") 
  
# Write the dataframe object 
# into csv file 
read_file.to_csv (config["csv_file"],  
                  index = None, 
                  header=True) 
    
# read csv file and convert  
# into a dataframe object 
df = pd.DataFrame(pd.read_csv(config["csv_file"])) 