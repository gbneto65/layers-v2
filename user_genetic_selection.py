from Defs import exit_app


class UserGeneticSelection():

    def __init__(self, df, user_input):
        self.df = df
        self.user_input = user_input

    def user_selection(self):
        # split DF according  the genetic line user selection
        try:
            selected_df = self.df[self.df['genetic_ident'] == self.user_input]
        except Exception():
            exit_app('Error creating selected DF - Aborted process')
        else:
            return selected_df
