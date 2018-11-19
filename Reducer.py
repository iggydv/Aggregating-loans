import pandas as pd
import util

class Reducer():
    # The Reducer class will be used to convert the data-frame data to required output:
    # The Aggregate loans by the tuple of Network, Product and Month with the total currency amounts and counts,
    # written into output file, Output.csv

    # __init__ function receives a data-frame which needs to be reduced
    def __init__(self, data_frame):
        self.data_frame = data_frame
        self.aggregate = None

    def reduce(self):
        """Aggregate loans by the tuple of Network, Product and Month with the total currency amounts and counts."""

        # Convert Date column from type string to type datetime
        self.data_frame = util.convert_column_to_datetime(self.data_frame, 'Date')

        grouped_by_month = self.data_frame.Date.dt.to_period("M")
        group_by_tuple = self.data_frame.groupby([grouped_by_month, 'Network', 'Product'])
        self.aggregate = group_by_tuple.sum()
        self.aggregate.rename(columns={'Amount': 'Aggregate'}, inplace=True)

        # use a dummy data-frame to count instances
        count_df = group_by_tuple.count()
        self.aggregate = self.aggregate.assign(Count=pd.Series(count_df[count_df.columns[-1]]))
        return self.aggregate

    def print_to_csv(self, output_path):
        """Output the aggregate data-frame into a file CSV file Output.csv"""
        self.aggregate.to_csv(output_path, sep=',')
