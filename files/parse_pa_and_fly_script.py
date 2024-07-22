import numpy as np
import pandas as pd
import re

def parse_pa (pa_file): # seperates header and field information
    pa_list =[]
    
    with open(pa_file, 'r') as file:
        lines = file.readlines()
        
        is_header = False
        is_body = False
        pa_header_list = []
        pa_field_list = []
        
        for line in lines:
            if 'begin_header' in line:
                is_header = True
                continue
            if'end_header' in line:
                is_header = False
                continue
            if is_header:
                pa_header_list.append(line.strip())
    
            #field information
            if 'begin_points' in line:
                is_body = True
                continue
            if 'end_points' in line:
                is_body = False
                continue
            if is_body: #strips each line, then seperates by spaces giving a list of lists
                pa_field_list.append(line.strip().split(' '))              
  
            
    pa_list = [pa_header_list, pa_field_list]
    
    return pa_list



def process_pa(pa_list): # keeps the header as a list and converts the field as a df
    processed_pa_list = []
    
    if len(pa_list) == 2:
        processed_pa_list.append(pa_list[0])
        pa_field_df = pd.DataFrame(pa_list[1], columns = ['x','y','z','is_electrode','field_x','field_y', 'field_z'])
        processed_pa_list.append(pa_field_df)
    
    return processed_pa_list


def process_fly(fly_file): # converts fly file to a dataframe
    
    with open(fly_file, 'r') as file:
        lines = file.readlines()
        
        counter = 0
        start_parse = False
        
        data_dict ={}
        data_list = []
        nested = False
        parent_key=''
        
        for line in lines:
            if 'standard_beam' in line:
                counter +=1
                start_parse = True
                if data_dict:
                    data_list.append(data_dict)
                    data_dict = {}
                continue
            elif start_parse:
                data = line.split(' = ')
                
                if len(data) >= 2:
                    key = data[0].strip()
                    values = data[1].replace(',\n','').strip()
                    
                #Special cases (nested)
                if '{' in line:
                    nested = True
                    parent_key = key
                    continue
                if nested:
                    key = f'{parent_key}_{key}'
                if '}' in line:
                    nested = False
                    parent_key = ''
                    continue
                
                data_dict[key] = values
            else:
                start_parse = False
        
        #Append the last chunk
        if counter == 1 + len(data_list):
            data_list.append(data_dict)
            
    fly_df = pd.DataFrame(data_list)
    
    return data_list, fly_df
