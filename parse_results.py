import numpy as np
import pandas as pd
import re

#results = 'C:\\SULI2024\\SIMION_files_2024\\run_results.csv'
results = "C:\\SULI2024\\SIMION_files_2024\\full_mic_Coul_results.dart"

with open(results, 'r') as file:
    results_lines = file.readlines()
    
    counter = 0
    start_parse = False
    data_dict = {}
    data_list = []
    
    for row in results_lines:
       
       if 'Ion(' in row:
           start_parse = True
           if data_dict:
               data_list.append(data_dict)
               #print('here')
               data_dict = {}
       if start_parse:
           matches = re.findall('(.*?)\\((.*?)\\)', row)
           key = []
           value = []
           for match in matches:
             key = match[0].strip()
             value = match[1].strip()
             data_dict[key] = (value) 
       else:
           start_parse = False 
            
#print(data_list)
        
results_df = pd.DataFrame(data_list)
results
print(results_df.head())