from Defs import exit_app
from system_setup import cost_setup, error_msn, egg_market


class VerifyUserInput:
    # verify data inputed by user - module system_setup
    def __init__(self, v_min, v_mp, v_max):
        self.min = v_min
        self.mp = v_mp
        self.max = v_max
        # self.distr = distr

    def var_input_check(self):
        # verify min mp & max input
        print('fui')
        print(self.min, self.mp, self.max)
        if self.mp < self.max:
            if self.min < self.mp:
                if self.min < self.max:
                    return True
                else:
                    return False
            return False
        return False


def user_type_error():
    test_feed = VerifyUserInput(
        cost_setup["feed_cost_ton_mim"],
        cost_setup["feed_cost_ton_mp"],
        cost_setup["feed_cost_ton_max"],
    )

    if not bool(test_feed.var_input_check()):
        exit_app(error_msn['input_err_feed_cost'])

    test_pullet = VerifyUserInput \
            (
            cost_setup["pullet_cost_mim"],
            cost_setup["pullet_cost_mp"],
            cost_setup["pullet_cost_max"],
        )

    if not bool(test_pullet.var_input_check()):
        exit_app(error_msn['input_err_pullet_cost'])

    test_additive = VerifyUserInput \
            (
            cost_setup["additive_cost_ton_mim"],
            cost_setup["additive_cost_ton_mp"],
            cost_setup["additive_cost_ton_max"],
        )

    if not bool(test_additive.var_input_check()):
        exit_app(error_msn['input_err_additive_cost'])

    test_vet = VerifyUserInput \
            (
            cost_setup["vet_cost_ton_mim"],
            cost_setup["vet_cost_ton_mp"],
            cost_setup["vet_cost_ton_max"],
        )

    if not bool(test_vet.var_input_check()):
        exit_app(error_msn['input_err_vet_cost'])

    test_wegg = VerifyUserInput \
            (
            egg_market['white_std_egg_unit_price_min'],
            egg_market['white_std_egg_unit_price_mp'],
            egg_market['white_std_egg_unit_price_max'],
        )

    if not bool(test_wegg.var_input_check()):
        exit_app(error_msn['input_err_wegg_price'])


