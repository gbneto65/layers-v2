# create np arrays from random parameters
# generate a numpy array with rnd values with n_repetitions (define by user) and n production weeks (usually round 100)

from system_setup import n_repetitions
import numpy as np


class CreateArraysFromParameters:
    # read parameter name value (feed_intake, etc) from all production weeks (18,19,20) and multiply para
    # other parameters (cost, etc)

    def __init__(self, df, first_row, last_row, df_col_name, rnd_parameter_name):
        self.df_col_name = df_col_name
        self.df = df
        self.first_row = first_row
        self.last_row = last_row
        self.rnd_parameter_name = rnd_parameter_name  # rnd_...

    def create_array_from_all_prod_weeks(self):

        c = np.zeros([n_repetitions], dtype=float)

        for i in range(1 + self.last_row - self.first_row):
            b = self.df.iloc[i][self.df_col_name] * self.rnd_parameter_name
            c = np.row_stack((c, b))

        c = np.delete(c, 0, 0) # delete the first row (zeros only)

        return c

class CreateArraysFromParametersNotIncludedInDf:
    def __init__(self,df, first_row, last_row, rnd_parameter_name):

        self.df = df
        self.first_row = first_row
        self.last_row = last_row
        self.rnd_parameter_name = rnd_parameter_name  # rnd_...

    def create_array_from_prod_not_df(self):

        c = np.zeros([n_repetitions], dtype=float)

        for i in range (1 + self.last_row - self.first_row):
            b = self.rnd_parameter_name
            c = np.row_stack((c, b))

        c = np.delete(c, 0, 0)

        return c

    def create_array_from_prod_not_df_with_cumulative(self):

        c = np.zeros([n_repetitions], dtype=float)


        for i in range(1 + self.last_row - self.first_row):
            b = self.rnd_parameter_name
            c = np.row_stack((c, b))

        c = np.delete(c, 0, 0)
        d = np.cumsum(c, axis=0) # cumulative values

        return d
