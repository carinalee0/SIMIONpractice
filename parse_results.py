import numpy as np
import pandas as pd
import re

#results = 'C:\\SULI2024\\SIMION_files_2024\\run_results.csv'
#results = "C:\\SULI2024\\SIMION_files_2024\\full_mic_Coul_results.dart"

def digit_check(str):

    if '-' in str:
        str = str.replace('-','')
        
    if '.' in str:
        str = str.replace('.','')
    
    if 'e' in str:
        str = str.replace('e','')

    return str.isdigit()

def parse_results(results):
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
                
                value_list = value.split(' ') # split value by space
                
                if len(value_list) >= 2 and digit_check(value_list[0]):
                    value = value_list[0]
                    unit = value_list[1]
                    key = f'{key}_{unit}' 
            
                data_dict[key] = (value)
         else:
            start_parse = False 
                
    #print(data_list)
            
    results_df = pd.DataFrame(data_list)


    return results_df

if __name__ == '__main__':
    print(parse_results("C:\\SULI2024\\SIMION_files_2024\\full_mic_Coul_results.dart"))