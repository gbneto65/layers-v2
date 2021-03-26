#Layer Project V2
# module to define the parameters

import os
import datetime
from app_version import get_versions
import glob
from Defs import sound_error
from system_setup import app_setup_parameters

# input the setup parameters below
#working_directory = os.getcwd() # get current working path
print(app_setup_parameters['working_folder'])


# find a CSV file and take its name - it will be use to open the DF later
csv_file = glob.glob('*.csv')
print(csv_file)

if len(csv_file) == 0 : # CSV file not found in the working dir
    sound_error()
    error_exit('no *.CSV file found')
elif len(csv_file) >1 : # verify if more than one CSV file was found
    sound_error()
    error_exit('more than one *.CSV files - Verify')
else :
    csv_file_name = csv_file[0] # DF file name
    print(f'CSV file found: {csv_file_name} - assumed as DF file')

