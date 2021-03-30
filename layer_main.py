# layer project V2
# main module
# todo - change the field "egg_mass_kg" to "cum_egg_mass_kg"


import pandas as pd
import numpy as np
from convert_month_to_layer_week import InputConvertion
from create_array_parameters import CreateArraysFromParameters, CreateArraysFromParametersNotIncludedInDf
from extract_df_info import ExtractDfInfo, df_indexing
from parameters import csv_file_name
from Defs import exit_app, display_intro_and_user_inputs
from random_numbers import CreateRndNumbers
from system_setup import error_msn, other_msn, cost_setup, n_repetitions, table_user_input_cost_fields
from user_genetic_selection import UserGeneticSelection
from verify_input import VerifyUserInput, user_type_error



if __name__ == "__main__":

    # show intro on screen
    display_intro_and_user_inputs()

    # verify input errors from 'system_setup.py'
    user_type_error()

    # call a class to convert monthly costs to weekly costs / bird
    # it returns a list with [min,mp,max,distr)

    feed = InputConvertion('feed')
    feed_cost_gr_of_feed = feed.convert_to_list()

    additive = InputConvertion('additive')
    additive_cost_gr_of_feed = additive.convert_to_list()

    vet = InputConvertion('vet')
    vet_cost_per_bird = vet.convert_to_list()

    other_cost = InputConvertion('other_cost')
    other_cost_per_bird = other_cost.convert_to_list()

    wegg = InputConvertion('wegg')
    white_egg_price_per_kg = wegg.convert_to_list()

    begg = InputConvertion('begg')
    brown_egg_price_per_kg = begg.convert_to_list()


    # earnings
    other_earn = InputConvertion('other_earn')
    other_earn_per_bird = other_earn.convert_to_list()

    # display a table with conversion results



    # todo - display converted data




    # generate rnd numbers for monte carlo simulation - random_numbers.py
    # feed cost
    feed_cost_gr_of_feed_rnd = CreateRndNumbers(
        feed_cost_gr_of_feed[0],
        feed_cost_gr_of_feed[1],
        feed_cost_gr_of_feed[2],
        feed_cost_gr_of_feed[3],
    )
    rnd_feed_cost_gr_of_feed = feed_cost_gr_of_feed_rnd.rnd_numbers()

    # additive cost
    additive_rnd = CreateRndNumbers(
        feed_cost_gr_of_feed[0],
        feed_cost_gr_of_feed[1],
        feed_cost_gr_of_feed[2],
        feed_cost_gr_of_feed[3],
    )
    rnd_feed_cost_gr_of_feed = additive_rnd.rnd_numbers()

    # vet cost / therapy cost
    vet_rnd = CreateRndNumbers(
        vet_cost_per_bird[0],
        vet_cost_per_bird[1],
        vet_cost_per_bird[2],
        vet_cost_per_bird[3],
    )
    rnd_vet_cost_per_bird = vet_rnd.rnd_numbers()

    # other cost
    other_cost = CreateRndNumbers(
        other_cost_per_bird[0],
        other_cost_per_bird[1],
        other_cost_per_bird[2],
        other_cost_per_bird[3],
    )
    rnd_other_cost_per_bird = other_cost.rnd_numbers()

    # white egg
    wegg = CreateRndNumbers(
        white_egg_price_per_kg[0],
        white_egg_price_per_kg[1],
        white_egg_price_per_kg[2],
        white_egg_price_per_kg[3],
    )
    rnd_white_egg_price_per_kg = wegg.rnd_numbers()

    # brown egg
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

    # earnings


    other_earn = CreateRndNumbers(
        other_earn_per_bird[0],
        other_earn_per_bird[1],
        other_earn_per_bird[2],
        other_earn_per_bird[3],
    )
    rnd_other_earn_per_bird = other_earn.rnd_numbers()



    #print(rnd_feed_cost_gr_of_feed)
    # print(rnd_feed_cost_gr_of_feed)
    # print(rnd_vet_cost_per_bird)
    # print(rnd_other_cost_per_bird)
    # print(rnd_brown_egg_price_per_kg)
    # print(rnd_pullet_cost)
    # print(rnd_other_earn_per_bird)



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
    hen_egg_color = df_info.get_egg_color()

    print(f'\nTotal weeks of production: {total_prod_week}')
    print(f'First weeks of production: {first_prod_week}')
    print(f'Last weeks of production: {last_prod_week}\n')
    print(f'The eggs color for this genetics is: {hen_egg_color}\n')

    # todo - display general info about genetics data



    # print(selected_df.head)

    # generate a numpy array with rnd values with n_repetitions (define by user) and n production weeks (usually round 100)

    # cum_feed_hen_week
    c = np.zeros([n_repetitions], dtype=float)
    a = CreateArraysFromParameters \
            (
            selected_df,
            first_prod_week,
            last_prod_week,
            'cum_feed_hen',
            rnd_feed_cost_gr_of_feed,
            )
    array_feed_cost_week_hen = a.create_array_from_all_prod_weeks()

    # cum_additive_hen_week
    a = CreateArraysFromParameters \
            (
            selected_df,
            first_prod_week,
            last_prod_week,
            'cum_feed_hen',
            rnd_feed_cost_gr_of_feed,
            )
    array_additive_cost_week_hen = a.create_array_from_all_prod_weeks()

    # rnd_pullet_cost
    a = CreateArraysFromParametersNotIncludedInDf\
            (
            selected_df,
            first_prod_week,
            last_prod_week,
            rnd_pullet_cost,
            )

    array_pullet_cost = a.create_array_from_prod_not_df()


    # rnd_vet_cost_per_bird
    a = CreateArraysFromParametersNotIncludedInDf\
            (
            selected_df,
            first_prod_week,
            last_prod_week,
            rnd_vet_cost_per_bird,
            )

    array_rnd_vet_cost_per_bird = a.create_array_from_prod_not_df()


    # rnd_other_cost_per_bird
    a = CreateArraysFromParametersNotIncludedInDf\
            (
            selected_df,
            first_prod_week,
            last_prod_week,
            rnd_other_cost_per_bird,
            )

    array_rnd_other_cost_per_bird = a.create_array_from_prod_not_df()

    #print(len(array_rnd_other_cost_per_bird))
    #print(array_rnd_other_cost_per_bird)

    # earnings =========================================

    # rnd_other_cost_per_bird
    a = CreateArraysFromParametersNotIncludedInDf\
            (
            selected_df,
            first_prod_week,
            last_prod_week,
            rnd_other_earn_per_bird,
            )

    array_rnd_other_earn_per_bird = a.create_array_from_prod_not_df()
    #print(array_rnd_other_earn_per_bird)

    # earnings from egg sales
    # identify the egg color and get egg price according
    if hen_egg_color.lower() == 'white':
        a = CreateArraysFromParameters \
                (
                selected_df,
                first_prod_week,
                last_prod_week,
                'egg_mass_hen',
                rnd_white_egg_price_per_kg,
                )
        array_rnd_egg_sales_hen_week = a.create_array_from_all_prod_weeks()

    elif hen_egg_color.lower() == 'brown':

        a = CreateArraysFromParameters \
                (
                selected_df,
                first_prod_week,
                last_prod_week,
                'egg_mass_hen',
                rnd_brown_egg_price_per_kg,
            )
        array_rnd_egg_sales_hen_week = a.create_array_from_all_prod_weeks()

    else:
        exit_app(error_msn['err_egg_sales'])
    #print(array_rnd_egg_sales_hen_week)

    # total costs calculation
    array_total_costs = array_feed_cost_week_hen\
                        + array_additive_cost_week_hen\
                        + array_pullet_cost\
                        + array_rnd_vet_cost_per_bird\
                        + array_rnd_other_cost_per_bird

    # total earnings calculation
    array_total_earnings = array_rnd_egg_sales_hen_week\
                           + array_rnd_other_earn_per_bird


    print(array_total_costs)
    print(array_total_earnings)


    #print(len(array_total_earnings))






    # for i in range (1 + last_prod_week - first_prod_week):
    #     b = rnd_pullet_cost
    #     c = np.row_stack((c, b))
    #
    # c = np.delete(c, 0, 0)
    # print(len(c))
    # print(c)

    #print(array_pullet_cost_week_hen)

    #
    # todo adj still not considered





