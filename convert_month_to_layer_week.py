# module to convert user input (monthly) to layer / weekly

from Defs import exit_app
from system_setup import *


class InputConvertion:
    # convertion of var inputs
    # output a list [min, mp, max, distr]


    def __init__(self, parameter):
        self.parameter = parameter
        self.one_million = 1000000

    def convert_to_list(self):

        if self.parameter.lower() == 'feed':
            feed = [None] * 4
            feed[0] = cost_setup["feed_cost_ton_mim"] / self.one_million

            feed[1] = cost_setup["feed_cost_ton_mp"] / self.one_million

            feed[2] = cost_setup["feed_cost_ton_max"] / self.one_million

            feed[3] = cost_setup["feed_cost_ton_distr"]
            return feed

        elif self.parameter.lower() == 'additive':
            additive = [None] * 4
            additive[0] = cost_setup["additive_cost_ton_mim"] / self.one_million
            additive[1] = cost_setup["additive_cost_ton_mp"] / self.one_million
            additive[2] = cost_setup["additive_cost_ton_max"] / self.one_million
            additive[3] = cost_setup["additive_cost_ton_distr"]
            return additive

        elif self.parameter.lower() == 'vet':
            vet = [None] * 4
            vet[0] = cost_setup["vet_cost_month_mim"] \
                     / app_setup_parameters['weeks_per_month'] \
                     / farm_setup['number_of_layers']
            vet[1] = cost_setup["vet_cost_month_mp"] \
                     / app_setup_parameters['weeks_per_month'] \
                     / farm_setup['number_of_layers']
            vet[2] = cost_setup["vet_cost_month_max"] \
                     / app_setup_parameters['weeks_per_month'] \
                     / farm_setup['number_of_layers']
            vet[3] = cost_setup["vet_cost_month_distr"]
            return vet

        elif self.parameter.lower() == 'other_cost':
            other_cost = [None] * 4
            other_cost[0] = cost_setup["other_cost_month_mim"] \
                       / app_setup_parameters['weeks_per_month'] \
                       / farm_setup['number_of_layers']
            other_cost[1] = cost_setup["other_cost_month_mp"] \
                       / app_setup_parameters['weeks_per_month'] \
                       / farm_setup['number_of_layers']
            other_cost[2] = cost_setup["other_cost_month_max"] \
                       / app_setup_parameters['weeks_per_month'] \
                       / farm_setup['number_of_layers']
            other_cost[3] = cost_setup["other_cost_month_distr"]
            return other_cost

        elif self.parameter.lower() == 'wegg':

            wegg = [None] * 4
            egg_kg = egg_market[ 'white_std_egg_weight_g'] / 1000 # convert egg weight to kg

            wegg[0] = (egg_market['white_std_egg_price_min'] \
                       / egg_market['sale_unit']) / egg_kg

            wegg[1] = egg_market['white_std_egg_price_mp'] \
                       / egg_market['sale_unit'] / egg_kg

            wegg[2] = egg_market['white_std_egg_price_max'] \
                       / egg_market['sale_unit'] / egg_kg

            wegg[3] = egg_market['white_std_egg_price_distr']
            return wegg

        elif self.parameter.lower() == 'begg':

            begg = [None] * 4
            egg_kg = egg_market[ 'brown_std_egg_weight_g'] / 1000 # convert egg weight to kg

            begg[0] = (egg_market['brown_std_egg_price_min'] \
                       / egg_market['sale_unit']) / egg_kg

            begg[1] = egg_market['brown_std_egg_price_mp'] \
                       / egg_market['sale_unit'] / egg_kg
 \
            begg[2] = egg_market['brown_std_egg_price_max'] \
                       / egg_market['sale_unit'] / egg_kg

            begg[3] = egg_market['brown_std_egg_price_distr']
            return begg

        elif self.parameter.lower() == 'other_earn':
            other_earn = [None] * 4
            other_earn[0] = egg_market["other_earning_month_min"] \
                            / app_setup_parameters['weeks_per_month'] \
                            / farm_setup['number_of_layers']
            other_earn[1] = egg_market["other_earning_month_mp"] \
                            / app_setup_parameters['weeks_per_month'] \
                            / farm_setup['number_of_layers']
            other_earn[2] = egg_market["other_earning_month_max"] \
                            / app_setup_parameters['weeks_per_month'] \
                            / farm_setup['number_of_layers']
            other_earn[3] = egg_market["other_earning_month_distr"]
            return other_earn

        else:

            exit_app('Error on convertion')

