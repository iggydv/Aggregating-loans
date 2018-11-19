import pandas as pd

class Mapper():
    # The Mapper class will be used as an intermediate step for the data, to serve as input for the Reducer class.
    # Python pandas are used to efficiently sort large data frames.

    # __init__ function receives a string with the directory of the csv file
    def __init__(self, csv_input):
        self.csv_input = csv_input
        if csv_input == '' or None:
            raise IOError('Please produce a csv file as input')

    def create_data_frame(self, mode='csv'):
        """Create a data frame, using pandas, consisting of data read from the input .csv file."""
        try:
            if mode == 'csv':
                data = pd.DataFrame.from_csv(self.csv_input)
            elif mode == 'dict':
                data = pd.DataFrame(self.csv_input)
            else:
                raise IOError('Invalid mode for create_data_frame selected')

            if data.empty:
                raise IOError('DataFrame is empty')

            return data
        except IOError:
            raise ValueError('Error occurred while loading dataframe {}'.format(mode))