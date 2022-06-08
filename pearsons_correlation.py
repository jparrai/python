# Class for defining an aggregate function
# to calculate the Pearson's correlation of the selected values in a sqlite query
# numpy as np has to be imported
# Will discard all NULL values in any of the columns
# Will return 0 if no valid values
# USAGE: sqliteConnection.create_aggregate("corr", 2, PearsonsCorr)
#        cursor.execute('SELECT corr(column1, column2) FROM data')
class PearsonsCorr:
    def __init__(self):
        self.values = []
        self.corrs = []

    def step(self, value, corr):
        print(value, corr)
        if value is not None and corr is not None:
            self.values.append(value)
            self.corrs.append(corr)

    def finalize(self):
        return np.corrcoef(self.values, self.corrs)[0, 1] if len(self.values) > 0 else 0
