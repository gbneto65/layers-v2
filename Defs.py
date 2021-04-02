from winsound import Beep
# module for functions used in layers project

import winsound
import numpy as np
from IPython.core.pylabtools import figsize
from prettytable import PrettyTable
from system_setup import error_msn, cost_setup, table_user_input_earn_fields, \
    table_user_input_cost_fields, egg_market, case_identification_setup, farm_setup, system_setup, \
    setup_chart_cost, app_setup_parameters
import matplotlib.pyplot as plt
import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')

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


def display_text_before_table(text, case_country, user_genetic):
    print(f'\n{text}\n Country: {case_country} - Layer breed: {user_genetic.capitalize()}')



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
        'Weeks of age',
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
        'Layer age (weeks)',
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


def display_delta_earn_cost_by_week(first_row, last_row, array_cost, array_earnings):
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
        'Layer age (weeks)',
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
            round(delta_earnings_cost_per_week / average_total_earnings_per_week * 100, system_setup['round_decimals']),
        ])

    return x


def built_charts(first_row, last_row, array_cost, array_earnings, user_genetic):
    mpl.style.use('classic')
    # costs
    array_feed_cost_week_hen = array_cost[0]
    array_additive_cost_week_hen = array_cost[1]
    array_pullet_cost = array_cost[2]
    array_rnd_vet_cost_per_bird = array_cost[3]
    array_rnd_other_cost_per_bird = array_cost[4]

    # earnings
    array_rnd_egg_sales_hen_week = array_earnings[0]
    array_rnd_other_earn_per_bird = array_earnings[1]

    weeks_axis = np.arange(first_row, 1 + last_row, 1) # create the x axis

    # initialization of numpy array
    z1 = np.zeros(1, dtype=float)
    z2 = np.zeros(1, dtype=float)
    z3 = np.zeros(1, dtype=float)
    z4 = np.zeros(1, dtype=float)
    z5 = np.zeros(1, dtype=float)

    z6 = np.zeros(1, dtype=float)
    z7 = np.zeros(1, dtype=float)

    z8 = np.zeros(1, dtype=float)
    z9 = np.zeros(1, dtype=float)

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

        # earning from egg sales
        f = np.average(array_rnd_egg_sales_hen_week[i, :])
        z6 = np.row_stack((z6, f))

        # other earnings
        g = np.average(array_rnd_other_earn_per_bird[i, :])
        z7 = np.row_stack((z7, g))

        # Delta - Earnings vs Cost
        h = np.average(array_rnd_other_cost_per_bird[i, :]) \
            + np.average(array_rnd_vet_cost_per_bird[i, :]) \
            + np.average(array_pullet_cost[i, :]) \
            + np.average(array_additive_cost_week_hen[i, :]) \
            + np.average(array_feed_cost_week_hen[i, :])

        z8 = np.row_stack((z8, h))

        # Delta - Earnings - Cost
        j = np.average(array_rnd_other_earn_per_bird[i, :]) \
            + np.average(array_rnd_egg_sales_hen_week[i, :])

        z9 = np.row_stack((z9, j))



    # delete first [0] row of the np.array
    feed = np.delete(z1, 0)
    addi = np.delete(z2, 0)
    pull = np.delete(z3, 0)
    vet = np.delete(z4, 0)
    other = np.delete(z5, 0)
    egg_sales = np.delete(z6, 0)
    other_earning = np.delete(z7, 0)

    total_cost = np.delete(z8, 0)
    total_earning = np.delete(z9, 0)

    gross_margin = (total_earning - total_cost) / total_earning * 100
    max_gross_margin = np.amax(gross_margin)

    max_gm = np.where(gross_margin == max_gross_margin)
    week_of_max_gross_margin = (max_gm[0] + first_row)

    breakeven_week = np.where(gross_margin > 0)
    week_of_breakeven = (breakeven_week[0] + first_row)

    #print(week_of_breakeven[0])


    all_cost = [pull, feed, addi, vet, other]
    all_earn = [egg_sales, other_earning]

    cost_and_earn = [total_cost, total_earning]

    # perc_of_feed_on_total_cost = np.average(feed)[breakeven_week + first_row] / np.average(total_cost + first_row)[breakeven_week]
    # print(perc_of_feed_on_total_cost)
    # perc_of_addi_on_total_cost = addi / total_cost
    # perc_of_pull_on_total_cost = pull / total_cost
    # perc_of_vet_on_total_cost = vet / total_cost
    # perc_of_other_on_total_cost = other / total_cost
    #
    # cost_rate_split_by_category = [perc_of_feed_on_total_cost,
    #                                perc_of_addi_on_total_cost,
    #                                perc_of_pull_on_total_cost,
    #                                perc_of_vet_on_total_cost,
    #                                perc_of_other_on_total_cost,
    #                                ]
    #
    # perc_of_egg_on_total_earn = egg_sales / total_cost
    # perc_of_other_on_total_earn = other_earning / total_cost
    #
    # earning_rate_split_by_category = [perc_of_egg_on_total_earn,
    #                                   perc_of_other_on_total_earn,
    #                                   ]
    #
    # print(perc_of_feed_on_total_cost)

    # built the charts

    plt.style.use('classic')
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
    fig.suptitle('Cumulative Cost & Earnings',
                 fontsize =20,
                 )

    ax1.stackplot(weeks_axis, all_cost,
                  labels=['Pullet', 'Feed', 'Additive', 'Vet', 'other'],
                  colors=[
                      setup_chart_cost['color_pullet_cost'],
                      setup_chart_cost['color_feed_cost'],
                      setup_chart_cost['color_additive_cost'],
                      setup_chart_cost['color_vet_cost'],
                      setup_chart_cost['color_other_cost'],
                  ],
                  alpha=setup_chart_cost['color_alpha_level'],
                  )

    ax1.legend(loc='upper left',
               fontsize=setup_chart_cost['legend_font_size'],
               )
    ax1.set_title('cost',
                  fontsize=setup_chart_cost['title_font_size'],
                  )
    ax1.set_xlabel('Layer age (weeks)',
                   fontsize=setup_chart_cost['x_label_font_size'])
    ax1.set_ylabel('Value ($)',
                   fontsize=setup_chart_cost['x_label_font_size'])
    ax1.set_xlim(xmin=first_row)

    ax1.grid(color=setup_chart_cost['color_grid'],
             linewidth=setup_chart_cost['grid_width'],
             )


    ax2.stackplot(weeks_axis, all_earn,
                  labels=['Egg Sales', 'Other Sales'],
                  alpha=setup_chart_cost['color_alpha_level'],
                  colors=[
                         setup_chart_cost['color_egg_sales_earn'],
                         setup_chart_cost['color_other_earn'],
                         ],
                  )

    ax2.legend(loc='upper left',
               fontsize=setup_chart_cost['legend_font_size'],
               )
    ax2.set_title('Earnings',
                  fontsize=setup_chart_cost['title_font_size'],
                  )
    ax2.set_xlabel('Layer age (weeks)',
                   fontsize=setup_chart_cost['x_label_font_size'])
    ax2.set_ylabel('Value ($)',
                   fontsize=setup_chart_cost['x_label_font_size'])
    ax2.set_xlim(xmin=first_row)

    ax2.grid(color=setup_chart_cost['color_grid'],
                    linewidth=setup_chart_cost['grid_width'],
             )

    plt.figtext(.7, .005,
                app_setup_parameters['app_title'],
                fontsize=9,
                alpha=.8)

    plt.figtext(0.12, .01,
                case_identification_setup['id_name']
                + ' - ' + case_identification_setup['Country']
                + ' - Layer breed: ' + user_genetic.capitalize(),
                fontsize=8,
                alpha=.8)

    plt.show()




    plt.style.use('classic')
    # plt.style.use('bmh')
    fig, (ax3) = plt.subplots(1, figsize=(8, 4))
    fig.suptitle('Cumulative Cost & Earnings',
                 fontsize=15,
                 )
    # costs
    ax3.stackplot(weeks_axis, cost_and_earn[0],
                  labels=['Cost'],
                  colors=[setup_chart_cost['color_total_cost']],
                  alpha=setup_chart_cost['color_alpha_level_total_cost'],
                  )

    # earnings
    ax3.stackplot(weeks_axis, cost_and_earn[1],
                  labels=['Earning'],
                  colors=[setup_chart_cost['color_vet_cost']],
                  alpha=setup_chart_cost['color_alpha_level_total_earn'],
                  )
    ax3.legend(loc='upper left',
               fontsize=setup_chart_cost['legend_font_size'] + 10)
    ax3.set_xlabel('Layer age (weeks)',
                   fontsize=setup_chart_cost['x_label_font_size'] + 10)
    ax3.set_ylabel('Value ($)',
                   fontsize=setup_chart_cost['y_label_font_size'] + 12)

    ax3.grid(color=setup_chart_cost['color_grid'],
             linewidth=setup_chart_cost['grid_width'],
             )
    ax3.set_xlim(xmin=first_row)
    plt.figtext(.7, .005,
                app_setup_parameters['app_title'],
                fontsize=9,
                alpha=.8)

    plt.figtext(0.12, .01,
                case_identification_setup['id_name']
                + ' - ' + case_identification_setup['Country']
                + ' - Layer breed: ' + user_genetic.capitalize(),
                fontsize=8,
                alpha=.8)

    plt.show()

    # Gross margin plot

    plt.style.use('classic')
    fig, (ax4) = plt.subplots(1, figsize=(8, 4))
    fig.suptitle('Egg Production Gross Margin (GM)',
                 fontsize=20,
                 )
    # costs
    ax4.stackplot(weeks_axis, gross_margin,
                  labels=['gross Margin (%)'],
                  colors=[setup_chart_cost['color_gross_margin']],
                  alpha=setup_chart_cost['color_alpha_level'],
                  )
        #
    # ax4.legend(loc='upper left',
    #            fontsize=setup_chart_cost['legend_font_size'] + 10)
    ax4.set_xlabel('Layer age (weeks)',
                   fontsize=setup_chart_cost['x_label_font_size'] + 10)
    ax4.set_ylabel('Gross Margin (%)',
                   fontsize=setup_chart_cost['y_label_font_size'] + 12)

    ax4.grid(color=setup_chart_cost['color_grid'],
             linewidth=setup_chart_cost['grid_width'],
             )

    ax4.set_ylim(ymin=-20)
    ax4.set_ylim(ymax=max_gross_margin + 10)
    ax4.set_xlim(xmin=first_row)

    plt.hlines(max_gross_margin,
                xmin = 0,
                xmax = week_of_max_gross_margin,
                linestyle='dashed',
                label='Max GM',
                color='#869493',
                linewidth=1,
                )

    plt.vlines(week_of_max_gross_margin,
                ymin=0,
                ymax=max_gross_margin,
                linestyle='dashed',
                label='Max GM',
                color='#869493',
                linewidth = 1,
                )
    plt.vlines(week_of_breakeven[0],
               ymin=-20,
               ymax=0,
               linestyle='dashed',
               label='Max GM',
               color='#869493',
               linewidth=1,
               )

    ax4.annotate('GM max.: ' + str(round(max_gross_margin,2)) + '%' + ' at ' + str(week_of_max_gross_margin) + ' weeks',
                 xy=(40, max_gross_margin), xytext=(40, max_gross_margin+.5),
                 fontsize=12,
                 alpha = .5
                 )

    ax4.annotate(f'Breakeven week\n({week_of_breakeven[0]} weeks of age)',
                xy=(week_of_breakeven[0], 0), xycoords='data',
                xytext=(0.86, 0.3), textcoords='axes fraction',
                arrowprops=dict(facecolor='gray', shrink=0.05, width=.01, headwidth=4),
                horizontalalignment='right', verticalalignment='top',
                )

    plt.figtext(.7, .005,
                app_setup_parameters['app_title'],
                fontsize=9,
                alpha = .8)

    plt.figtext(0.12, .005,
                case_identification_setup['id_name']
                + ' - ' + case_identification_setup['Country']
                + ' - Layer breed: ' + user_genetic.capitalize(),
                fontsize=8,
                alpha=.8)

    plt.show()


    # pie chart
    # todo pie chart