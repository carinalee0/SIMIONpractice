from subprocess import call
import math
import numpy as np
import os
import matplotlib.pyplot as plt
import csv
import statistics

output_file = "run_results.csv"

simion_path = "C:\\Program Files\\SIMION-8.1\\simion.exe" # This is the correct path.
workbench_path = "C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\front_lens.iob"
simion_options = "--nogui"
fly_path = "C:\\SULI2024\\SIMION_files_2024\\front_lens.fly2"
#fly_path = "C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\300eV_origin20.fly2"

def run_microscope(voltages, output_file = output_file):
    try:
        os.remove(output_file) # Delete existing files with the same name
    except OSError:
        pass
    
    flight_options = ' --recording-output=' + output_file + ' --retain-trajectories=0 --restore-potentials=0'
    fastadj_options = 'C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\TOF_obj_17_high.PA0 1=' + str(voltages[0]) + ',2=' + str(voltages[1]) + ',3=' + str(voltages[2]) + ',4=' + str(voltages[3]) 
    
    fastadj_command = simion_path +' '+ simion_options + ' ' + 'fastadj' + fastadj_options
    call(fastadj_command)
    
    flymaker_command = 'python C:\\Users\\carina\\SULI2024\\SIMION_files_2024\\front_lens.fly2'
    call(flymaker_command)
    
    simion_command = simion_path + ' ' + simion_options + ' fly ' + flight_options + ' ' + workbench_path
    call(simion_command)
    
run_microscope([0,0,0,0])
