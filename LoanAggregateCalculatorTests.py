import unittest
import Reducer
import Mapper
import pandas as pd
import datetime
import util



class MyTestCase(unittest.TestCase):

    # TODO: Remove BOM for csv file to display MSISDN

    test_dict = [{'Network': 'Network 1', 'Date': '12-Mar-2016', 'Product': 'Loan Product 1',
                  'Amount': 1000},
                 {'Network': 'Network 2', 'Date': '16-Mar-2016', 'Product': 'Loan Product 1',
                  'Amount': 1122},
                 {'Network': 'Network 3', 'Date': '17-Mar-2016', 'Product': 'Loan Product 2',
                  'Amount': 2084}]

    data_frame = pd.DataFrame(test_dict)

    def test_convert_column_to_datetime(self):
        data_frame = pd.DataFrame(self.test_dict)
        expected_date = datetime.datetime(2016, 3, 12)
        new_data_frame = util.convert_column_to_datetime(data_frame, 'Date')
        generated_date = new_data_frame.iat[0, 1]
        self.assertEqual(generated_date, expected_date)

    def test_convert_column_to_datetime_with_invalid_column_name(self):
        data_frame = pd.DataFrame(self.test_dict)
        with self.assertRaises(KeyError):
            util.convert_column_to_datetime(data_frame, 'Timestamp')

    def test_reduce(self):
        # TODO: Remove BOM for csv file to display MSISDN
        data_frame = pd.DataFrame(self.test_dict)
        test_reducer = Reducer.Reducer(data_frame)
        generated_reduced_data_frame = test_reducer.reduce()

        reduced_dict = [{'Date': datetime.datetime(2016, 3, 1), 'Network': 'Network 1', 'Product': 'Loan Product 1', 'Aggregate': 1000, 'Count': 1},
                        {'Date': datetime.datetime(2016, 3, 1), 'Network': 'Network 2', 'Product': 'Loan Product 1', 'Aggregate': 1122, 'Count': 1},
                        {'Date': datetime.datetime(2016, 3, 1), 'Network': 'Network 3', 'Product': 'Loan Product 2', 'Aggregate': 2084, 'Count': 1}]

        reduced_data_frame = pd.DataFrame(reduced_dict)
        grouped_by_month = reduced_data_frame.Date.dt.to_period("M")
        group_by_tuple = reduced_data_frame.groupby([grouped_by_month, 'Network', 'Product'])
        expected_reduced_data_frame = group_by_tuple.sum()

        assert generated_reduced_data_frame.equals(expected_reduced_data_frame)

    def test_data_frame(self):
        dictionary = self.test_dict
        test_mapper = Mapper.Mapper(dictionary)
        generated_data_frame = test_mapper.create_data_frame('dict')
        expected_data_frame = pd.DataFrame(self.test_dict)
        assert generated_data_frame.equals(expected_data_frame)

    def test_data_frame_with_invalid_mode(self):
        dictionary = self.test_dict
        test_mapper = Mapper.Mapper(dictionary)

        with self.assertRaises(ValueError):
            test_mapper.create_data_frame('csv')


    def test_data_frame_with_invalid_csv_file(self):
        test_mapper = Mapper.Mapper('te3st_loans.csv')

        with self.assertRaises(ValueError):
            test_mapper.create_data_frame('csv')

if __name__ == '__main__':
    unittest.main()
