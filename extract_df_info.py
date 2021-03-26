
def df_indexing(df):
    # index DF by production week
    df = df.set_index('hen_week_age',
                          inplace=True)
    return df



class ExtractDfInfo:
    def __init__(self, df):
        self.df = df
    
    def get_total_production_week(self):
        return  len(self.df.index)

    def get_first_production_week(self):
        return self.df.first_valid_index()

    def get_last_production_week(self):
        return self.df.last_valid_index()

