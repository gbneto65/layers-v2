# layer project V2
# main module
# todo improvements on verification of the user inputs
# todo

import pandas as pd
import os
import numpy as np

from convert_month_to_layer_week import InputConvertion
from extract_df_info import ExtractDfInfo, df_indexing
from parameters import csv_file_name
from Defs import sound_error, exit_app
from random_numbers import CreateRndNumbers
from system_setup import error_msn, other_msn, cost_setup, n_repetitions
# open CSV file DF
from user_genetic_selection import UserGeneticSelection

# verify input data
from verify_input import VerifyUserInput, user_type_error

# verify input errors from 'system_setup.py'
user_type_error()

# call a class to convert monthly costs to weekly costs / bird

feed = InputConvertion('feed')
feed_cost_gr = feed.convert_to_list()

additive = InputConvertion('additive')
additive_cost_gr = additive.convert_to_list()

vet = InputConvertion('vet')
vet_cost_per_bird = vet.convert_to_list()

other_cost = InputConvertion('other_cost')
other_cost_per_bird = other_cost.convert_to_list()

wegg = InputConvertion('wegg')
white_egg_price_per_kg = wegg.convert_to_list()

begg = InputConvertion('begg')
brown_egg_price_per_kg = begg.convert_to_list()









pullet_cost = CreateRndNumbers\
            (
            cost_setup["pullet_cost_mim"],
            cost_setup["pullet_cost_mp"],
            cost_setup["pullet_cost_max"],
            cost_setup["pullet_cost_distr"],
            )
array_pullet_cost = pullet_cost.rnd_numbers()


feed_cost = CreateRndNumbers\
            (
            cost_setup["feed_cost_ton_mim"],
            cost_setup["feed_cost_ton_mp"],
            cost_setup["feed_cost_ton_max"],
            cost_setup["feed_cost_ton_distr"],
            )
array_feed_cost = feed_cost.rnd_numbers()

additive_cost = CreateRndNumbers\
            (
            cost_setup["additive_cost_ton_mim"],
            cost_setup["additive_cost_ton_mp"],
            cost_setup["additive_cost_ton_max"],
            cost_setup["additive_cost_ton_distr"],
            )
array_additive_cost = additive_cost.rnd_numbers()

vet_cost = CreateRndNumbers\
            (
            cost_setup["vet_cost_month_mim"],
            cost_setup["vet_cost_month_mp"],
            cost_setup["vet_cost_month_max"],
            cost_setup["vet_cost_month_distr"],

            )
array_vet_cost = vet_cost.rnd_numbers()
other_cost = CreateRndNumbers\
            (
            cost_setup["other_cost_month_mim"],
            cost_setup["other_cost_month_mp"],
            cost_setup["other_cost_month_max"],
            cost_setup["other_cost_month_distr"],
            )
array_other_cost = other_cost.rnd_numbers()




#print(array_feed_cost)






# read CSV file
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

# user input
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
#print(selected_df.head)






array = selected_df[['feed_intake_max', 'feed_intake_max']].to_numpy()

a = np.mean(array, axis=1).tolist
b = np.transpose(a)
c = np.hstack(array,b)

print(c)

#print(array)

# # costs parameters
# for i in range(total_prod_week):
#     a =selected_df.loc[[i + first_prod_week]]
#     b = a['feed_intake_min']
#     c = a['feed_intake_max']
#     d = (c+b)/2
#     print(f'{b}  {c}  {d}')
#





