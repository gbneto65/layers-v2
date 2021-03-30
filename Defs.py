from winsound import Beep
# module for functions used in layers project

import winsound

from prettytable import PrettyTable

from system_setup import error_msn, cost_setup, table_user_input_earn_fields, \
    table_user_input_cost_fields, egg_market, case_identification_setup, farm_setup


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

def create_intro_table():
    version = 'Version:xxxx'
    x = PrettyTable()
    x.field_names = ['    ', f'Layer Performance Calculator - {version}']
    x.align['    '] = "r"
    x.align[f'Layer Performance Calculator - {version}'] = "l"
    x.add_row(['', ''])
    x.add_row(['Id_Name: ', case_identification_setup['id_name']])
    x.add_row(['Country: ', case_identification_setup['Country']])
    x.add_row(['Number of Layers: ', farm_setup['number_of_layers']])
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
