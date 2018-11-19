import dateutil

def convert_column_to_datetime(data, column_name):
    """Convert Date column from type String to type datetime"""
    try:
        data[column_name] = data[column_name].apply(dateutil.parser.parse, dayfirst=True)
        return data
    except KeyError:
        raise KeyError('Error, column_name does not exist')