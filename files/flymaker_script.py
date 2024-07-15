import numpy as np

# Kinetic Energy
""""
single_value_input = ['any string', KE value]

gaussian_input = ['gaussian', KE value, FWHM]

lorentzian_input = ['lorentzian',KE value, FWHM]

"""
def set_KE(input_list):
    KE_str = ''
    
    if len(input_list) < 3:
        KE_str = '     ke = ' + str(input_list[1])
        
    if 'gauss' in input_list[0]:
        # add automatic std calculation
        KE_str = '     ke = gaussian_distribution { \n      mean = '+ str(input_list[1]) + ', \n      fwhm = ' + str(input_list[2])  + '\n     },'
        
    if 'lorentz' in input_list[0]:
        KE_str = '     ke = lorentzian_distribution { \n      median = ' + str(input_list[1]) + ', \n      fwhm = ' + str(input_list[2]) + '\n     },'
        
    return str(KE_str)

"""
Test KE function

one_value = ['', 350]
print(set_KE(one_value))

gauss = ['gaussian', 325, 10]
print(set_KE(gauss))

loren = ['lorentzian', 330, 5]
print(set_KE(loren))
    
"""

"""
Direction: Elevation

single_value = ['any string', angle]  

gaussian_input = ['gaussian', mean, stdev, fwhm]

arithmetic_sequence_input = ['arithmetic sequence', first, step, n]

uniform_dsitribution_input = ['uniform distribution', min, max]

"""
def set_elevation(input_list):
    el_str = ''
    
    if len(input_list) == 2:
        el_str = '    el = ' + str(input_list[1]) + ','
    
    if 'arithmetic sequence' in input_list[0]:
        el_str = '     el = arithmetic sequence { \n        first = ' + str(input_list[1]) + ', \n        step = ' + str(input_list[2]) + ', \n        n = ' + str(input_list[3]) + ' \n     },'
    
    if 'gaussian' in input_list[0]:
        el_str = '     el = gaussian distribution { \n        mean = ' + str(input_list[1]) + ', \n        stdev = ' + str(input_list[2]) + ', \n        fwhm = ' + str(input_list[3]) + ' \n     },'
        
    if 'uniform distribution' in input_list[0]:
        el_str = '     el = uniform_distribution { \n        min = ' + str(input_list[1]) + ', \n        max = ' + str(input_list[2]) + ' \n     },'
    
    #return print(el_str)
    return str(el_str)

"""
Test elvation function

single_value_input = ['single_vlaue or any string', 25]  
print(set_elevation(single_value_input))

gaussian_el = ['gaussian', 300, 10, 1]
print(set_elevation(gaussian_el))

arithmetic_sequence_input = ['arithmetic sequence', 30, 1, 40]
print(set_elevation(arithmetic_sequence_input))

uniform_dsitribution_input = ['uniform distribution', -30, 30]
print(set_elevation(uniform_dsitribution_input))  
    
"""
"""
Direction: Azimuthal

single_value = ['any string', angle]  

gaussian_input = ['gaussian', mean, stdev, fwhm]

arithmetic_sequence_input = ['arithmetic sequence', first, step, n]

uniform_dsitribution_input = ['uniform distribution', min, max]

"""
def set_azm(input_list):
    azm_str = ''
    
    if len(input_list) == 2:
        azm_str = '     az = ' + str(input_list[1]) + ','
    
    if 'arithmetic sequence' in input_list[0]:
        azm_str = '     az = arithmetic sequence { \n        first = ' + str(input_list[1]) + ', \n        step = ' + str(input_list[2]) + ', \n        n = ' + str(input_list[3]) + ' \n     },'
    
    if 'gaussian' in input_list[0]:
        azm_str = '     az = gaussian distribution { \n        mean = ' + str(input_list[1]) + ', \n       stdev = ' + str(input_list[2]) + ', \n        fwhm = ' + str(input_list[3]) + ' \n     },'
        
    if 'uniform distribution' in input_list[0]:
        azm_str = '     az = uniform_distribution { \n        min = ' + str(input_list[1]) + ', \n        max = ' + str(input_list[2]) + ' \n     },'
    
    #return print(azm_str)
    return str(azm_str)

"""
Test azimuthal function

single_value_azm = ['single_vlaue or any string', 25]  
print(set_azm(single_value_azm))

gaussian_azm= ['gaussian', 300, 10, 1]
print(set_azm(gaussian_azm))

arithmetic_sequence_azm = ['arithmetic sequence', 30, 1, 40]
print(set_azm(arithmetic_sequence_azm))

uniform_dsitribution_azm = ['uniform distribution', -30, 30]
print(set_azm(uniform_dsitribution_azm))

"""

"""
Direction

direction_list = [azm_list, el_list]

"""
def set_direction(direction_list):
    
    if len(direction_list) == 2: 
        direction_str = str(set_azm(direction_list[0])) + '\n' + str(set_elevation(direction_list[1])) 
    
    return str(direction_str)

"""
Test direction function

direction_test = [arithmetic_sequence_azm,gaussian_el]
print(set_direction(direction_test))

"""

"""
Source position

single_vector_input = ['single vector', X, Y, Z]

line_distribution_input = ['line distribution', first x, first y, first z, last x, last y, last z]

gaussian3d_dsitrbution_input = ['gaussian', mean x, mean y, mean z, stdev?] # to be completed

"""
def set_source_position(input_list):
    source_position_str = ''
    
    if 'single vector' in input_list[0]:
        source_position_str = '     position = vector(' + str(input_list[1]) + ', ' + str(input_list[2]) + ', ' + str(input_list[3]) +')'
        
    if 'line distribution' in input_list[0]:
        source_position_str = '     position = line_distribution { \n        first = vector(' + str(input_list[1]) + ', ' + str(input_list[2])+ ', ' + str(input_list[3]) +') \n        last = vector('  + str(input_list[1]) + ', ' + str(input_list[2])+ ', ' + str(input_list[3]) +') \n     }'
         
    if 'gaussian' in input_list[0]: # incomplete
        source_position_str = '      position = gaussian3d_distribution { \n        mean = vector('+ str(input_list[1]) + ', ' + str(input_list[2]) + ', ' + str(input_list[3]) +') \n        stdev = vector(' # to do 
        
    
    return str(source_position_str)

"""
Test source position function

single_vector_input = ['single vector', 20 , 0, 1]
print(set_source_position(single_vector_input))

line_distribution_input = ['line distribution', 25, 1, 0, 25, -1, 0]
print(set_source_position(line_distribution_input))

"""

"""
TOB (time of birth)

single_value_input = ['any string', tob value]

arithmetic_sequence_input = ['arithmetic sequence', first, step]

uniform_distribution_input = ['uniform distribution', min, max]
    
"""

def set_tob (input_list):
    tob_str =''
    
    if len(input_list) == 2:
        tob_str = '     tob = ' + str(input_list[1])
        
    if 'arithmetic sequence' in input_list[0]:
        tob_str = '     tob = arithmetic sequence { \n        first = ' + str(input_list[1]) + ', \n        step = ' + str(input_list[2]) + ' \n     },'
    
    if 'uniform distribution' in input_list[0]:
        tob_str = '     tob = uniform_distribution { \n         min = ' + str(input_list[1]) + ', \n       max = ' + str(input_list[2]) + ' \n     },'
    

    return str(tob_str)

"""
Test TOB function

single_value_tob= ['any string', 1]
print(set_tob(single_value_tob))

arithmetic_sequence_tob = ['arithmetic sequence', 0, 0.5]
print(set_tob(arithmetic_sequence_tob))

uniform_distribution_tob = ['uniform distribution', 0, 1.5]
type(set_tob(uniform_distribution_tob))

"""


# Creates a string for each new group of particles / anytime a paramter is changed
def get_group_string(tob_list, mass, charge, ke_list, direction_list, source_position_list):
    group_str = """
    standard_beam {
        n = 30 \n       """ + set_tob(tob_list) + """
            mass = """ + str(mass) + """
            charge = """ + str(charge) + '\n' + set_KE(ke_list) + '\n' + set_direction(direction_list) + """
            cwf = 1
            color = 1 \n""" + set_source_position(source_position_list) + """
            }"""
  
    return group_str

# Generate a param list. Need to call this.
def get_param_list(tob_list, ke_list, direction_list, source_position_list, mass = 0.0005485799, charge = -1):
    param_list = [tob_list, mass, charge, ke_list, direction_list, source_position_list]
    return param_list

# Combines all group strings and writes to the fly file. Need to call this.
def write_flyfile (file_name, param_list):
    
    group_str = ''
    for param in param_list:
        group_str = group_str + '\n' + get_group_string(param[0], param[1], param[2], param[3], param[4], param[5])
    
    with open(file_name, 'w') as file:
        file.write("""
            particles {
                coordinates = 0 
                """ + group_str + """
            }""")
