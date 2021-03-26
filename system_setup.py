# layers v2
# module to store constants and parameters inputed by users
# Distributions letters
# T : Triangular
# F : fixed value (consider the mp value)
# U : uniform
import os


# cost user input parameters
cost_setup = {
                "pullet_cost_mim" : 1,
                "pullet_cost_mp" : 2,
                "pullet_cost_max" : 3,
                "pullet_cost_distr": 'T',

                "feed_cost_ton_mim": 250,
                "feed_cost_ton_mp": 300,
                "feed_cost_ton_max": 350,
                "feed_cost_ton_distr": 'T',

                "additiv_cost_ton_mim": 250,
                "additiv_cost_ton_mp": 300,
                "additiv_cost_ton_max": 350,
                "additiv_cost_ton_distr": 'T',

# monthly cost should be converted by layer cost / week
                "vet_cost_month_mim": 250,
                "vet_cost_month_mp": 300,
                "vet_cost_month_max": 350,
                "vet_cost_month_distr": 'T',

                "other_cost_month_mim": 250,
                "other_cost_month_mp": 300,
                "other_cost_month_max": 350,
                "other_cost_month_distr": 'T',

             }


adj_to_performance_data = {
# the values should be in percentual (ex: 0.01 = 1%, -.1 = 10%)

                        'adj_daily_feed_intake_by_hen' : 0,
                        'adj_weekly_cum_egg_by_hen' : 0,
                        'adj_weekly_cum_mort' : 0,
                        'adj_egg_weight' : 0,

                          }
app_setup_parameters = {
                        'app_title' : 'Layer Performance Calculator',
                        'weeks_per_month' : 4.34524,
                        'working_folder' : os.getcwd(),
                        }


error_msn =  {
              'file_not_found' : 'File not found in working directory. Please verify',
              'open_file_error' : 'A error occur when trying to open the file.',
              'wrong_selection' : 'wrong selection....',
              'abort_user' : '*** Aborted by user *** ',
              'abort_app' : '*** Aborted Process *** ',
              }

other_msn =  {
              'user_genetic_options_msn' : 'Input the number that correspond the genetic you want to work',


              }



