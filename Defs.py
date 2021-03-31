from winsound import Beep
# module for functions used in layers project

import winsound
import numpy as np
from prettytable import PrettyTable
from system_setup import error_msn, cost_setup, table_user_input_earn_fields, \
    table_user_input_cost_fields, egg_market, case_identification_setup, farm_setup, system_setup
import matplotlib.pyplot as plt

def sound_error():
    sd1 = [1500, 200]  # frequency, time mseg.
    sd2 = [2500, 200]
    winsound.Beep(sd1[0], sd1[1])
    winsound.Beep(sd2[0], sd2[1])
    return


def exit_app(msn):
    sound_error()
    print('\n' + msn + '\n')
    print('\n ' + error_msn['abort_app'])
    exit()


def create_user_input_cost_table():
    x0 = PrettyTable()
    x0.field_names = table_user_input_cost_fields
    x0.add_row \
            (
            ['Minimum:',
             cost_setup["pullet_cost_mim"],
             cost_setup["feed_cost_ton_mim"],
             cost_setup["additive_cost_ton_mim"],
             cost_setup["vet_cost_month_mim"],
             cost_setup["other_cost_month_mim"],

             ]
        )

    x0.add_row \
            (
            ['Most Prob.:',
             cost_setup["pullet_cost_mp"],
             cost_setup["feed_cost_ton_mp"],
             cost_setup["additive_cost_ton_mp"],
             cost_setup["vet_cost_month_mp"],
             cost_setup["other_cost_month_mp"],
             ]
        )
    x0.add_row \
            (
            ['Maximum.:',
             cost_setup["pullet_cost_max"],
             cost_setup["feed_cost_ton_max"],
             cost_setup["additive_cost_ton_max"],
             cost_setup["vet_cost_month_max"],
             cost_setup["other_cost_month_max"],
             ]
        )

    x0.add_row \
            (
            ['Distrib.:',
             cost_setup["pullet_cost_distr"].upper(),
             cost_setup["feed_cost_ton_distr"].upper(),
             cost_setup["additive_cost_ton_distr"].upper(),
             cost_setup["vet_cost_month_distr"].upper(),
             cost_setup["other_cost_month_distr"].upper(),
             ]
        )
    return x0


def create_user_input_earn_table():
    # Earnings table
    x1 = PrettyTable()
    x1.field_names = table_user_input_earn_fields
    x1.add_row \
            (
            ['Minimum:',
             egg_market['white_std_egg_price_min'],
             egg_market['white_std_egg_weight_g'],
             egg_market['brown_std_egg_price_min'],
             egg_market['brown_std_egg_weight_g'],
             egg_market['sale_unit'],
             egg_market['other_earning_month_min'],

             ]
        )

    x1.add_row \
            (
            ['Most Prob.:',
             egg_market['white_std_egg_price_mp'],
             egg_market['white_std_egg_weight_g'],
             egg_market['brown_std_egg_price_mp'],
             egg_market['brown_std_egg_weight_g'],
             egg_market['sale_unit'],
             egg_market["other_earning_month_mp"],
             ]
        )
    x1.add_row \
            (
            ['Maximum.:',
             egg_market['white_std_egg_price_max'],
             egg_market['white_std_egg_weight_g'],
             egg_market['brown_std_egg_price_max'],
             egg_market['brown_std_egg_weight_g'],
             egg_market['sale_unit'],
             egg_market["other_earning_month_max"],
             ]
        )

    x1.add_row \
            (
            ['Distrib.:',
             egg_market['white_std_egg_price_distr'].upper(),
             egg_market['white_std_egg_weight_g'],
             egg_market['brown_std_egg_price_distr'].upper(),
             egg_market['brown_std_egg_weight_g'],
             egg_market['sale_unit'],
             egg_market["other_earning_month_distr"].upper(),
             ]
        )

    return x1


# print(create_user_input_cost_table())
# print(create_user_input_earn_table())

def create_intro_table(user_genetic):
    version = 'Version:xxxx'
    x = PrettyTable()
    x.field_names = ['    ', f'Layer Performance Calculator - {version}']
    x.align['    '] = "r"
    x.align[f'Layer Performance Calculator - {version}'] = "l"
    x.add_row(['', ''])
    x.add_row(['Id_Name: ', case_identification_setup['id_name']])
    x.add_row(['Country: ', case_identification_setup['Country']])
    x.add_row(['Number of Layers: ', farm_setup['number_of_layers']])
    x.add_row(['Genetic : ', user_genetic.capitalize()])
    return x


def display_intro_and_user_inputs():
    # display introduction on screen
    print(create_intro_table())
    # display table with user inputed data
    print("\nUser input Costs\n")
    print(create_user_input_cost_table())
    print("\nUser input Earnings\n")
    print(create_user_input_earn_table())
    print('\n')


def display_converted_data():
    pass


def display_cost_by_week(first_row, last_row, array_cost):
    # array_cost = [
    #     array_feed_cost_week_hen,
    #     array_additive_cost_week_hen,
    #     array_pullet_cost,
    #     array_rnd_vet_cost_per_bird,
    #     array_rnd_other_cost_per_bird,
    # ]
    # basics statistics for table
    array_feed_cost_week_hen = array_cost[0]
    array_additive_cost_week_hen = array_cost[1]
    array_pullet_cost = array_cost[2]
    array_rnd_vet_cost_per_bird = array_cost[3]
    array_rnd_other_cost_per_bird = array_cost[4]

    x = PrettyTable()

    x.field_names = [
        'Week',
        'Pullet cost',
        'Pullet (%)',
        'feed cost',
        'Feed (%)',
        'Additive cost',
        'Additive (%) ',
        'Health cost',
        'Health (%)',
        'Other cost',
        'Other (%)',
        'Total cost',
    ]

    for i in range(1 + last_row - first_row):
        average_feed_cost_week_hen = np.average(array_feed_cost_week_hen[i, :])
        average_pullet_cost = np.average(array_pullet_cost[i, :])
        average_additive_cost_week_hen = np.average(array_additive_cost_week_hen[i, :])
        average_vet_cost_per_bird = np.average(array_rnd_vet_cost_per_bird[i, :])
        average_other_cost_per_bird = np.average(array_rnd_other_cost_per_bird[i, :])

        average_total_cost_per_week = average_feed_cost_week_hen \
                                      + average_pullet_cost \
                                      + average_additive_cost_week_hen \
                                      + average_vet_cost_per_bird \
                                      + average_other_cost_per_bird

        rel_average_pullet_cost_week = average_pullet_cost / average_total_cost_per_week * 100
        rel_average_feed_cost_week_hen = average_feed_cost_week_hen / average_total_cost_per_week * 100
        rel_average_additive_cost_week_hen = average_additive_cost_week_hen / average_total_cost_per_week * 100
        rel_average_vet_cost_per_bird = average_vet_cost_per_bird / average_total_cost_per_week * 100
        rel_average_other_cost_per_week_hen = average_other_cost_per_bird / average_total_cost_per_week * 100

        x.add_row([
            i + first_row,

            round(average_pullet_cost, system_setup['round_decimals']),
            round(rel_average_pullet_cost_week, system_setup['round_decimals']),

            round(average_feed_cost_week_hen, system_setup['round_decimals']),
            round(rel_average_feed_cost_week_hen, system_setup['round_decimals']),

            round(average_additive_cost_week_hen, system_setup['round_decimals']),
            round(rel_average_additive_cost_week_hen, system_setup['round_decimals']),

            round(average_vet_cost_per_bird, system_setup['round_decimals']),
            round(rel_average_vet_cost_per_bird, system_setup['round_decimals']),

            round(average_other_cost_per_bird, system_setup['round_decimals']),
            round(rel_average_other_cost_per_week_hen, system_setup['round_decimals']),

            round(average_total_cost_per_week, system_setup['round_decimals']),

        ])

    return x


def display_earn_by_week(first_row, last_row, array_earnings):
    # array_earnings = [
    #     array_rnd_egg_sales_hen_week,
    #     array_rnd_other_earn_per_bird,
    # ]

    # basics statistics for table
    array_rnd_egg_sales_hen_week = array_earnings[0]
    array_rnd_other_earn_per_bird = array_earnings[1]

    x = PrettyTable()
    x.field_names = [
        'Week',
        'Egg sales',
        'Egg sales (%)',
        'Other earnings',
        'Other earnings (%)',

        'Total earnings',
    ]

    for i in range(1 + last_row - first_row):
        average_array_rnd_egg_sales_hen_week = np.average(array_rnd_egg_sales_hen_week[i, :])
        average_array_rnd_other_earn_per_bird = np.average(array_rnd_other_earn_per_bird[i, :])

        average_total_earnings_per_week = average_array_rnd_egg_sales_hen_week \
                                          + average_array_rnd_other_earn_per_bird

        rel_average_array_rnd_egg_sales_hen_week = average_array_rnd_egg_sales_hen_week / average_total_earnings_per_week * 100
        rel_average_array_rnd_other_earn_per_bird = average_array_rnd_other_earn_per_bird / average_total_earnings_per_week * 100

        x.add_row([
            i + first_row,

            round(average_array_rnd_egg_sales_hen_week, system_setup['round_decimals']),
            round(rel_average_array_rnd_egg_sales_hen_week, system_setup['round_decimals']),

            round(average_array_rnd_other_earn_per_bird, system_setup['round_decimals']),
            round(rel_average_array_rnd_other_earn_per_bird, system_setup['round_decimals']),

            round(average_total_earnings_per_week, system_setup['round_decimals']),

        ])

    return x


def display_delta_earn_cost_by_week (first_row, last_row, array_cost, array_earnings):
    # display the delta from earnings and cost

    # costs
    array_feed_cost_week_hen = array_cost[0]
    array_additive_cost_week_hen = array_cost[1]
    array_pullet_cost = array_cost[2]
    array_rnd_vet_cost_per_bird = array_cost[3]
    array_rnd_other_cost_per_bird = array_cost[4]

    # earnings
    array_rnd_egg_sales_hen_week = array_earnings[0]
    array_rnd_other_earn_per_bird = array_earnings[1]

    x = PrettyTable()
    x.field_names = [
                'Week',
                'Costs',
                'Earnings',
                'Delta',
                'Gross Margem (%)',
                          ]


    for i in range(1 + last_row - first_row):

        average_feed_cost_week_hen = np.average(array_feed_cost_week_hen[i, :])
        average_pullet_cost = np.average(array_pullet_cost[i, :])
        average_additive_cost_week_hen = np.average(array_additive_cost_week_hen[i, :])
        average_vet_cost_per_bird = np.average(array_rnd_vet_cost_per_bird[i, :])
        average_other_cost_per_bird = np.average(array_rnd_other_cost_per_bird[i, :])

        average_total_cost_per_week = average_feed_cost_week_hen \
                                      + average_pullet_cost \
                                      + average_additive_cost_week_hen \
                                      + average_vet_cost_per_bird \
                                      + average_other_cost_per_bird


        average_array_rnd_egg_sales_hen_week = np.average(array_rnd_egg_sales_hen_week[i, :])
        average_array_rnd_other_earn_per_bird = np.average(array_rnd_other_earn_per_bird[i, :])

        average_total_earnings_per_week = average_array_rnd_egg_sales_hen_week \
                                          + average_array_rnd_other_earn_per_bird \

        delta_earnings_cost_per_week = average_total_earnings_per_week - average_total_cost_per_week

        x.add_row([
            i + first_row,
            round(average_total_cost_per_week, system_setup['round_decimals']),
            round(average_total_earnings_per_week, system_setup['round_decimals']),
            # delta earnings / cost
            round(delta_earnings_cost_per_week, system_setup['round_decimals']),
            # Gross margem
            round(delta_earnings_cost_per_week / average_total_earnings_per_week *100, system_setup['round_decimals']),
                ])


    return x


def built_charts(first_row, last_row, array_cost, array_earnings):
    # costs
    array_feed_cost_week_hen = array_cost[0]
    array_additive_cost_week_hen = array_cost[1]
    array_pullet_cost = array_cost[2]
    array_rnd_vet_cost_per_bird = array_cost[3]
    array_rnd_other_cost_per_bird = array_cost[4]

    # earnings
    array_rnd_egg_sales_hen_week = array_earnings[0]
    array_rnd_other_earn_per_bird = array_earnings[1]

    #feed_cost = np.zeros([1 + last_row - first_row], dtype = float)

    weeks_axis = np.arange(first_row, 1 + last_row, 1)

    # initialization of numpy array
    z1 = np.zeros(1, dtype=float)
    z2 = np.zeros(1, dtype=float)
    z3 = np.zeros(1, dtype=float)
    z4 = np.zeros(1, dtype=float)
    z5 = np.zeros(1, dtype=float)

    for i in range(1 + last_row - first_row):
        # feed
        a = np.average(array_feed_cost_week_hen[i, :])
        z1 = np.row_stack((z1, a))

        # additive_cost
        b = np.average(array_additive_cost_week_hen[i, :])
        z2 = np.row_stack((z2, b))

        # pullet_cost
        c = np.average(array_pullet_cost[i, :])
        z3 = np.row_stack((z3, c))

        # vet_cost
        d = np.average(array_rnd_vet_cost_per_bird[i, :])
        z4 = np.row_stack((z4, d))

        # other cost
        e = np.average(array_rnd_other_cost_per_bird[i, :])
        z5 = np.row_stack((z5, e))

    # delete first [0] row of the np.array
    feed = np.delete(z1,0)
    addi = np.delete(z2,0)
    pull = np.delete(z3,0)
    vet = np.delete(z4,0)
    other = np.delete(z5,0)

    all_cost = [pull, feed, addi, vet, other]

    plt.style.use('bmh')

    fig, ax = plt.subplots()
    ax.stackplot(weeks_axis, all_cost,
                 labels=['Pullet', 'Feed', 'Additive', 'Vet', 'other'],
                 )
    ax.legend(loc='upper left')
    ax.set_title('Cumulative weekly cost')
    ax.set_xlabel('Production week')
    ax.set_ylabel('Value ($)')

    plt.show()

