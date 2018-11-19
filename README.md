Documentation:
================

-------------------------
LoanAggregateCalculator
-------------------------

The LoanAggregateCalculator class uses objects from the Mapper and Reducer classes,
to map and reduce data read from a csv file (Loans.csv) and creates an output csv file (default=Output.csv) 
with columns Date, Network, Product, Aggregate and Count.
LoanAggregateCalculator aggregates the loans by the tuple of Network, Product and Month with the total
currency amounts.

LoanAggregateCalculator class methods:
--------------------------------------

def __init__(self, input_path, output_path):

Initialise a LoanAggregateCalculator object, receive two inputs:
input_path - input file name
output_path - output file name

calculate_aggregate_loans(self):

Creates a Mapper object to map the data from the input file to a more usable format.
Creates a Reducer object to reduce the data to the required output, and writes to output file

-------------------------
LoanAggregateCalculator CLI
-------------------------

This class creates a small command line tool (CLI) using docopt (http://docopt.org/)

doctopt is a handy python library that allows you to create a clean CLI for your python application.

This CLI allows the user to specify the input file, which will be used to calculate
the loans aggregate and also an option to specify the output file to write to (default = Output.csv)

LoanAggregateCalculator.py --input=PATH_FILE [--output=PATH_FILE]
LoanAggregateCalculator.py -h | --help

Usage:
------
>> Python LoanAggregator_CLI.py --input=Loans.csv
>> Python LoanAggregator_CLI.py --input=Loans.csv --output=any_output_file.csv


-------------------------
Mapper
-------------------------
The Mapper class is used as an intermediate step for the data, to serve as input for
the reducer class. Python pandas are used to efficiently sort large data frames.
A Mapper object is created by the call - Mapper(csv_input)

Mapper class methods:
-------------------------
__init__(self, csv_input_dir)

Initialise a Mapper object, receive one input variable 'csv_input_dir' - file path
to the input loans.csv file.

create_data_frame(self, mode='csv')

*** The BOM character in the loans.csv caused some problems when creating a pandas data-frame. The MSISDN of
*** each entry is discarded during the reduce function, but as I assumed that the MSISDN information is irrelevant
*** when aggregating data by the tuple of Network, Product and Month.

Create a data frame, using pythonpandas, consisting of data read from:
mode = 'csv': an input .csv file.
mode = 'dict': an input python dictionary

-------------------------
Reducer
-------------------------
The Reducer class isused to convert the data-frame data to required output:
The Aggregate loans by the tuple of Network, Product and Month with the total
currency amounts and counts, written into output file, Output.csv

Reducer class methods:
-------------------------
__init__(self, data_frame)

Initialise a Reducer object, receive one input 'data_frame' - data frame, produced
by the Mapper.create_data_frame() function.

reduce(self)

The data-frame is then grouped by month and the aggregate loans for the
tuple of Month, Network and Product is calculated.
A seperate calculation counts the amount of loans for the tuple of Month,
Network and Product and is inserted into the aggregated data-frame.
The final necessary step is to rename the column 'Amount' to 'Aggregate'.
The data is now successfully reduced.

print_to_csv(self)

Python pandas are again used to easily write the reduced data-frame into an output file
in csv format.

-------------------------
util
-------------------------

util.py Contains utility functions, which can be used by other classes.

convert_column_to_datetime(data, column_name):

Convert the string date from 'data' found in 'column_name' to datetime format using dateutil



-------------------------
unittesting
-------------------------

To run the unittests, use the following command

>> Python LoanAggregateCalculatorTests.py




General:
=========

-------------------------
Why Python? (version 3.6)
-------------------------
According to Jeff Hammerbacher, Python's popularity for data science is largely due
to the strength of its core libraries (NumPy, SciPy, pandas, matplotlib and IPython),
high productivity for prototyping and building small reusable systems, and strength
as a general purpose programming language.

-------------------------
Python Pandas (version 0.19.2)
-------------------------
(http://pandas.pydata.org/)

pandas is an open source, BSD-licensed library providing high-performance,
easy-to-use data structures and data analysis tools for the Python programming
language.

pandas helps fill this gap, enabling you to carry out your entire data analysis workflow
in Python without having to switch to a more domain specific language like R.
Combined with the excellent IPython toolkit and other libraries, the environment for
doing data analysis in Python excels in performance, productivity, and the ability to collaborate.

Fast and efficient DataFrame object for data manipulation with integrated indexing
Tools for reading and writing data
Flexible reshaping and pivoting of data sets
Columns can be inserted and deleted from data structures for size mutability
Time series-functionality
Highly optimized for performance


-------------------------
Detail Performance
-------------------------
Assume pandas computational complexity for mapping and reducing is O(K+K)
where K is the number of entries in the csv file, therefore Big O(N)


-------------------------
Scaling Considerations
-------------------------
This implementation will work well for Large Data Frames, but it will be necessary to apply
caution when the Data Frames become very large, as pandas indexing drain's a lot
of the computational power.



Author:
========
Ignatius Thomas de Villiers

Contact details:
==================
Email: iggydv12@gmail.com
Cell: 064 651 6300






