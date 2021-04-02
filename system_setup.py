# layers v2
# module to store constants and parameters inputed by users
# Distributions letters
# T : Triangular
# F : fixed value (consider the mp value). However, the min and max should be imputed (not considered)
# U : uniform
import os
import datetime
now = datetime.datetime.now()
#print ("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))




case_identification_setup = {
        'id_name' : 'Sr Oscar',
        'Country' : ' Spain',

        }
farm_setup = {
        'number_of_layers': 1000000,
             }
# cost user input parameters
# implemented distributions : U = Uniform, T = Triangular, F = Fixed value
cost_setup = {
                "pullet_cost_mim" : 1,
                "pullet_cost_mp" : 5,
                "pullet_cost_max" : 6,
                "pullet_cost_distr": 'f',

                "feed_cost_ton_mim": 250,
                "feed_cost_ton_mp": 320,
                "feed_cost_ton_max": 350,
                "feed_cost_ton_distr": 'f',

                "additive_cost_ton_mim": 2,
                "additive_cost_ton_mp": 5,
                "additive_cost_ton_max": 6,
                "additive_cost_ton_distr": 'f',

# monthly cost should be converted by layer cost / week
                "vet_cost_month_mim": 20000,
                "vet_cost_month_mp": 30000,
                "vet_cost_month_max": 35000,
                "vet_cost_month_distr": 'f',

                "other_cost_month_mim": 30000,
                "other_cost_month_mp": 35000,
                "other_cost_month_max": 40000,
                "other_cost_month_distr": 'f',

             }

egg_market = {
                  'white_std_egg_price_min' : 83,
                  'white_std_egg_price_mp' : 96,
                  'white_std_egg_price_max' : 115,
                  'white_std_egg_price_distr' : 'F',

                  'white_std_egg_weight_g' : 65,

                  'brown_std_egg_price_min' : 83.91,
                  'brown_std_egg_price_mp' : 96.48,
                  'brown_std_egg_price_max' : 115.54,
                  'brown_std_egg_price_distr' : 't',

                  'brown_std_egg_weight_g' : 65,

                  'sale_unit' : 1538, # price refer to X eggs

                  'other_earning_month_min' : .001, # other potentialy earnings (feces, etc)
                  'other_earning_month_mp' : .01,
                  'other_earning_month_max' : .2,
                  'other_earning_month_distr' : 'f',


}

system_setup = {
                'round_decimals': 3
                }

adj_to_performance_data = {
# the values should be in percentual (ex: 0.01 = 1%, -.1 = -10%)

                        'adj_cum_feed_intake_by_hen' : 0,
                        # todo not implemented adjust below
                        # 'adj_cum_egg_by_hen' : 0,
                        # 'adj_cum_mort' : 0,
                        # 'adj_egg_weight' : 0,
                        # 'adj_egg_prod' : 0,

                          }
app_setup_parameters = {
                        'app_title' : f'Layer Performance Calculator - V2 - {now.strftime("%Y-%m-%d %H:%M:%S")}',
                        'weeks_per_month' : 4.34524,
                        'working_folder' : os.getcwd(),
                        }


error_msn =  {
              'file_not_found' : 'File not found in working directory. Please verify',
              'open_file_error' : 'A error occur when trying to open the file.',
              'wrong_selection' : 'wrong selection....',
              'abort_user' : '*** Aborted by user *** ',
              'abort_app' : '*** Aborted Process *** ',
              'input_err_feed_cost' : 'Input Error at Feed Cost / ton ',
              'input_err_pullet_cost' : 'Input Error at pullet Cost / ton ',
              'input_err_additive_cost' : 'Input Error at additiveCost / ton ',
              'input_err_vet_cost' : 'Input Error at vet Cost ',
              'input_err_white_egg_price' : 'Input Error at white egg price ',
              'input_err_brown_egg_price' : 'Input Error at brown egg price ',
              'input_err_other_earning' : 'Input Error at other earning ',
              'err_egg_sales' : 'Error found when trying calculate the earnings from sales - Verify egg color at DF (should be only white or brown) ',

              }

other_msn =  {
              'user_genetic_options_msn' : 'Input the number that correspond the genetic you want to work',


              }

n_repetitions = 4


table_user_input_cost_fields = [' ',
                           'Pullet Cost',
                           'Feed/ton',
                           'Additive/ton feed',
                           'Vet costs/month',
                           'Other Cost/month',

                           ]

table_user_input_earn_fields = [' ',
                           'Egg price (White)',
                           'Egg weight (White)',
                           'Egg price (brown)',
                           'Egg weight (brown)',
                                'Sale unit',
                           'Other earning / month',
                           ]

setup_chart_cost = {
                    'color_pullet_cost' : '#ffbaba',
                    'color_feed_cost' :   '#ee5455',
                    'color_additive_cost' : '#494c7d',
                    'color_vet_cost' : '#5c9a95',
                    'color_other_cost' : '#b3617b',

                    'color_egg_sales_earn' : '#73914f',
                    'color_other_earn' : '#00559b',

                    'color_total_cost' : '#ee5455',
                    'color_total_earn' : '#73914f',
                    'color_gross_margin' : '#6f7575',

                    'color_grid' : '#dcdcdc',
                    'grid_width' : 1,

                    'color_alpha_level_total_cost' : .7,
                    'color_alpha_level_total_earn' : .5,
                    'color_alpha_level' : .4,

                    'legend_font_size': 10,
                    'title_font_size': 20,
                    'x_label_font_size': 15,
                    'y_label_font_size': 15,


                    }
