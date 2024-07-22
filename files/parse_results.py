import numpy as np
import pandas as pd
import re
import h5py
from datetime import datetime
from parse_pa_and_fly_script import process_fly

current_time = datetime.now()
timestamp_str = current_time.strftime("%Y%m%d_%H%M%S")

# One-hot encoding the Event column so that the dataframe is all numeric
event_dict = {
    "Ion Created" : 1,
    "Crossed Y = 0 Plane" : 2,
    "Hit Electrode" : 3,
    "Outside Work Bench" : 4
    }


def digit_check(str):

    if '-' in str:
        str = str.replace('-','')
        
    if '.' in str:
        str = str.replace('.','')
    
    if 'e' in str:
        str = str.replace('e','')

    return str.isdigit()

def parse_results(results = "C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\run_results.csv"):
    with open(results, 'r') as file:
        results_lines = file.readlines()
        
        flym_counter = 0
        start_parse = False
        data_dict = {}
        data_list = []
        datasets_list = []

        for row in results_lines:  
        
         if "Begin Fly'm" in row: # Begin Fly'm occurs for each simulation
            flym_counter +=1
                
         if 'Ion(' in row:
            start_parse = True
            if data_dict: # If the dictionary is not empty, dump it into the list
                data_list.append(data_dict)
                data_dict = {} # Reinitialize dictionary
         if start_parse:
            matches = re.findall('(.*?)\\((.*?)\\)', row) # Regex match
            key = []
            value = []
            for match in matches:
                key = match[0].strip()
                value = match[1].strip()
                
                value_list = value.split(' ') # split value by space
                
                if len(value_list) >= 2 and digit_check(value_list[0]):
                    value = float(value_list[0])
                    unit = value_list[1]
                    key = f'{key}_{unit}' 

                value = value if key != "Event" else event_dict[value] # change Event to numeric value
                data_dict[key] = float(value)
         else:
            start_parse = False 
         
        # In case multiple simulations are appended to one results file, a list of datasets are created
        if flym_counter >= 0:
            datasets_list.append(data_list)
            data_list = []
                
    #print(data_list)
    # Will typically be a list of one (one simulation at a time)
    df_list = []
    for dataset in datasets_list:
        df = pd.DataFrame(dataset)
        df['Dataset_name'] = float(flym_counter)
        
        df_list.append(df)

    return df_list

#if __name__ == '__main__':
#    print(parse_results("C:\\SULI2024\\SIMION_files_2024\\full_mic_Coul_results.dart"))

def move_to_h5(h5, fly_file, v, ke_values, results = "C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\run_results.csv"): # dumps information from run_results.csv to h5 and clears the csv?
    df_list = parse_results(results)
    with h5py.File(h5, 'a') as hf:
        for df in df_list: # Each dataset is one simulation / element in df
            # voltages and ke are a list
            volt_str = str(v).replace(',','_').replace(' ','').replace('[','').replace(']','')
            ke_str = str(ke_values)
            dataset_str = 'v_' + volt_str + '_ke'+ ke_str + '_'+ timestamp_str
            # timestamp_str format is YYYYMMDD_HHMMSS
            print(volt_str)
            #print(ke_str)
            dataset_obj = hf.create_dataset(dataset_str, data = df)
            print('Dataset added.')
            fly_dict_list, fly_df = process_fly(fly_file)
            
            dict_counter = 0
            for dict in fly_dict_list:
                dict_counter += 1
                for k,v in dict.items():
                    dataset_obj.attrs[str(dict_counter)+ '_' + k] =  v
           
            
            
            
    #print(f'Added {len(df_list)} datasets.')
    