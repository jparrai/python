# Class for defining an aggregate function to calculate 
# the geometric average of the selected values in a sqlite db
# Will discard all NULL or zero or negative values, there are other ways of treating this values
# Will return None if no positive values
# USAGE: sqliteConnection.create_aggregate("g_avg", 1, GeometricAvg)
#        cursor.execute('SELECT g_avg(value) FROM data')

class GeometricAvg:
    def __init__(self):
        self.counter = 0
        self.mean = 0.0

    def step(self, value):
        if type(value) == int or type(value) == float:
            if value is not None and value > 0:
                self.mean += np.log(value)
                self.counter += 1

    def finalize(self):
        if self.counter > 0:
            return np.exp(self.mean / self.counter)
        else:
            return None
