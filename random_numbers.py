# generate random numbers
from Defs import exit_app
from system_setup import *
import numpy as np


def generate_rnd_numbers_triangular(min, mp, max, n_repetitions):
    return np.random.triangular(min,mp,max,n_repetitions)

def generate_rnd_numbers_uniform(min, max, n_repetitions):
    return np.random.uniform(min, max,n_repetitions)


class CreateRndNumbers:
    def __init__(self, min, mp, max, distr):

        self.distr = distr
        self.min = min
        self.mp = mp
        self.max = max

    def rnd_numbers(self):

        if self.distr.upper() == 'T':
            rd = generate_rnd_numbers_triangular\
                    (
                self.min, self.mp, self.max, n_repetitions
                    )
            return rd

        elif self.distr.upper() == 'U':

            rd = generate_rnd_numbers_uniform \
                    (
                    self.min, self.max, n_repetitions
                    )
            return rd
        else:
            exit_app('error')

            return a



