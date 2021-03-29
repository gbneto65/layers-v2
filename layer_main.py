# layer project V2
# main module
# todo improvements on verification of the user inputs
# todo

import pandas as pd
import os
import numpy as np

from convert_month_to_layer_week import InputConvertion
from create_array_parameters import CreateArraysFromParameters
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
# it returns a list with [min,mp,max,distr)

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

# generate rnd numbers for monte carlo simulation - random_numbers.py

feed_cost_gr_rnd = CreateRndNumbers(
    feed_cost_gr[0],
    feed_cost_gr[1],
    feed_cost_gr[2],
    feed_cost_gr[3],
)
rnd_feed_cost_gr = feed_cost_gr_rnd.rnd_numbers()

additive_rnd = CreateRndNumbers(
    additive_cost_gr[0],
    additive_cost_gr[1],
    additive_cost_gr[2],
    additive_cost_gr[3],
)
rnd_additive_cost_gr = additive_rnd.rnd_numbers()

vet_rnd = CreateRndNumbers(
    vet_cost_per_bird[0],
    vet_cost_per_bird[1],
    vet_cost_per_bird[2],
    vet_cost_per_bird[3],
)
rnd_vet_cost_per_bird = vet_rnd.rnd_numbers()

other_cost = CreateRndNumbers(
    other_cost_per_bird[0],
    other_cost_per_bird[1],
    other_cost_per_bird[2],
    other_cost_per_bird[3],
)
rnd_other_cost_per_bird = other_cost.rnd_numbers()

wegg = CreateRndNumbers(
    white_egg_price_per_kg[0],
    white_egg_price_per_kg[1],
    white_egg_price_per_kg[2],
    white_egg_price_per_kg[3],
)
rnd_white_egg_price_per_kg = wegg.rnd_numbers()

begg = CreateRndNumbers(
    brown_egg_price_per_kg[0],
    brown_egg_price_per_kg[1],
    brown_egg_price_per_kg[2],
    brown_egg_price_per_kg[3],
)
rnd_brown_egg_price_per_kg = begg.rnd_numbers()

pullet_cost = CreateRndNumbers \
        (
        cost_setup["pullet_cost_mim"],
        cost_setup["pullet_cost_mp"],
        cost_setup["pullet_cost_max"],
        cost_setup["pullet_cost_distr"],
    )
rnd_pullet_cost = pullet_cost.rnd_numbers()

#
print(rnd_feed_cost_gr)
# print(rnd_additive_cost_gr)
# print(rnd_vet_cost_per_bird)
# print(rnd_other_cost_per_bird)
# print(rnd_brown_egg_price_per_kg)
# print(rnd_pullet_cost)


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

# user input about layer breed (genetics)
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

print(f'\nTotal weeks of production: {total_prod_week}')
print(f'First weeks of production: {first_prod_week}')
print(f'Last weeks of production: {last_prod_week}\n')
# print(selected_df.head)

c = np.zeros([n_repetitions], dtype=float)
a = CreateArraysFromParameters \
        (
        selected_df,
        first_prod_week,
        last_prod_week,
        'cum_feed_hen',
        rnd_feed_cost_gr,
        )
array_feed_cost_week_hen = a.create_array_from_all_prod_weeks()

print(array_feed_cost_week_hen)


c = np.zeros([n_repetitions], dtype=float)
a = CreateArraysFromParameters \
        (
        selected_df,
        first_prod_week,
        last_prod_week,
        'cum_feed_hen',
        rnd_additive_cost_gr,
        )
array_additive_cost_week_hen = a.create_array_from_all_prod_weeks()

print(array_additive_cost_week_hen)

# todo pullet  matrix, other cost, earnings
# todo adj still not considered





