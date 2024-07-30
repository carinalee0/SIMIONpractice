import h5py
import numpy as np
import pandas as pd

from parse_pa_and_fly_script import process_fly

from flymaker_script import write_flyfile
from flymaker_script import get_param_list
from flymaker_script import get_group_string

from SIMION_run_full_microscope import run_microscope
from parse_results import move_to_h5
from parse_results import dataset_to_df

fly_file = "C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\full_microscope.fly2"
db_file = "C:\\Users\\carina\\SULI2024\\test\\SIMIONdb"

# Generate list of parameters: vary KE
#ke_values = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]

v3_values = [14000]
voltages = [0,2500, None,2000,2500,5000,1100,338,2225,10,10,195,92,30,47] # Experimental voltages with extractor at 14keV

tob = ['',0]
ke_values = [300] #, 350]
ke = ['gaussian', ke_values, 5]
azm = ['',0]
el = ['arithmetic sequence', 30, -2, 31]
direction = [azm , el]

# Setting some y spread.
#source_y_pos = [-0.2, -0.1, 0, 0.1, 0.2]
source_position = ['single vector',20.001, 0, 0]

# Format inputs.
for v3 in v3_values:
    voltages[2] = v3
    
    for ke_value in ke_values:
        ke[1] = ke_value
        file_str = []
        
        file_str.append(get_param_list(tob_list = tob, ke_list = ke, direction_list = direction, source_position_list = source_position))

        # Write fly file.
        write_flyfile(file_name = fly_file, param_list = file_str)

        # Run simulation
        run_microscope(voltages)