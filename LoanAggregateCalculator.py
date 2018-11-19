"""
Loan Aggregate Calculator

Usage:
  LoanAggregateCalculator.py --input=PATH_FILE [--output=PATH_FILE]
  LoanAggregateCalculator.py -h | --help

Options:
    -h,--help               : show this help message
    --input=PATH_FILE       : specify input file
    --output=PATH_FILE      : specify output file [default: Output.csv]

"""
import docopt
import Mapper
import Reducer

class LoanAggregateCalculator():
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def calculate_aggregate_loans(self):
        # Mapper object
        aggregator_map = Mapper.Mapper(self.input_path)
        data = aggregator_map.create_data_frame()

        # Reducer object
        reducer = Reducer.Reducer(data)
        reducer.reduce()
        reducer.print_to_csv(self.output_path)



# TODO: Initialise logger here

if __name__ == '__main__':
    arguments = docopt.docopt(__doc__, version='0.1')

    input_path = arguments['--input']
    output_path = arguments['--output']

    L = LoanAggregateCalculator(input_path, output_path)
    L.calculate_aggregate_loans()
    print(input_path+' successfully reduced and aggregated to '+output_path)


