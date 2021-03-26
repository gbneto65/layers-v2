# layer project V2
# main module

# todo continue to implement the module input verification

import pandas as pd
import os

from extract_df_info import ExtractDfInfo, df_indexing
from parameters import csv_file_name
from Defs import sound_error, exit_app
from system_setup import error_msn, other_msn, cost_setup
# open CSV file DF
from user_genetic_selection import UserGeneticSelection

# verify input data
from verify_input import VerifyUserInput, user_type_error

user_type_error() # verify user type error





try:
    layer_df = pd.read_csv(csv_file_name)  # main df
except FileNotFoundError:
    exit_app(error_msn['file_not_found'])
except Exception():
    exit_app(error_msn['open_file_error'])
else:
    print(f'CSV file {csv_file_name} was open\n')

print(layer_df.head)

# select the layer genetics from the DF
genetic_options = layer_df['genetic_ident'].unique()
print('\n' + other_msn['user_genetic_options_msn'])
for i in range(len(genetic_options)):
    print(f'Option [{i}] = {genetic_options[i]}')

select = int(input(' ? (type 10 to exit)'))

if select == 10:
    exit_app(error_msn['abort_user'])
elif select > len(genetic_options):
    exit_app(error_msn['wrong_selection'])
else:
    # create a subset of the original database base on user input (layer genetic)
    genetic_selection = UserGeneticSelection(layer_df, genetic_options[select])
    selected_df = genetic_selection.user_selection()

# indexing DF by production week
select_df = df_indexing(selected_df)

# get info about production weeks, first and last week from the DF
df_info = ExtractDfInfo(selected_df)
total_prod_week = df_info.get_total_production_week()
first_prod_week = df_info.get_first_production_week()
last_prod_week = df_info.get_last_production_week()

print(total_prod_week)
print(first_prod_week)
print(last_prod_week)

# costs parameters
