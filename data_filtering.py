import re

from input_messages import print_date_filters_input, print_airline_filters_input, \
    print_ask_columns, print_ask_operations, print_json_columns

def is_period_valid(start, end): 
    date_pattern = r"\b(19|20)\d\d[-](0[1-9]|1[0-2])[-](0[1-9]|[12][0-9]|3[01])\b"
    
    start_valid = re.match(date_pattern, start) 
    end_valid = re.match(date_pattern, end)

    return start_valid and end_valid


def wants_to_exit(user_input):
    return len(user_input) == 1 and user_input == "0"


def ask_operator():
    print_ask_operations() 
    while True: 
        operation = input("Please inform the operation: ").strip()
        
        if wants_to_exit(operation):
            print("Exiting the system. Goodbye!")
            exit()

        try:             
            if operation in ["eq", "ne", "lt", "gt"]:   
                break  

        except ValueError: 
            print(f"Invalid entry. Please select a valid operation.")

    return operation


def get_json_columns(dataframe, column): 
    print_json_columns(dataframe, column)

    column_desired = input("Please inform the column: ").strip()

    return column_desired
    

def ask_column_to_filter(dataframe): 
    print_ask_columns(dataframe)

    while True:         
        column = input("Please inform the column: ").strip()

        if wants_to_exit(column):
            print("Exiting the system. Goodbye!")
            exit()

        try:             
            if column in dataframe.columns:                   
                break  

        except ValueError: 
            print(f"Invalid entry. Please select a valid column.")

    return column


def ask_value(): 
    value = input("Please, informe the value you want to filter: ") 

    return value


def data_filtering(flight_data):
    """
    Asks what filters the user wants to provide. 
    Based on this, applies the filters in the csv.

    field: the field to be filtered. The available options
    are: 
        - date = flight date
        - origin = flight origin
        - destination = flight destination
        - airline = airline

    operator: the following operators are available for
    all the fields
        - eq = equals
        - ne = not equal
    
    for the flight date, these filters are available: 
        - gt = greater than
        - lt = less than 
    """
    json_columns = [
        "departure", 
        "arrival",
        "airline",
        "flight",
        "aircraft"
    ]

    operators = {
        "eq": lambda x, y: x == y,
        "ne": lambda x, y: x != y,
        "gt": lambda x, y: x > y,
        "lt": lambda x, y: x < y
    }
    
    column = ask_column_to_filter(flight_data)

    if column in json_columns: 
        json_value = get_json_columns(flight_data, column)
    else:
        json_value = None

    operator = ask_operator()
    value = ask_value()

    if json_value is not None: 
        filtered_df = flight_data[
            operators[operator](
                flight_data[column].apply(lambda x: x.get(json_value, None)), value
            )
        ]
    else: 
        filtered_df = flight_data[
            operators[operator](flight_data[column], value)
        ]    

    print(filtered_df.to_string(index=False))


def get_date_filters():
    while True:  
        print_date_filters_input()     
        
        period_input = input("Please inform the period: ").strip()

        if wants_to_exit(period_input):
            print("Exiting the system. Goodbye!")
            exit()

        try: 
            start, end = period_input.split(" ")
            
            if is_period_valid(start, end):  
                break  

        except ValueError: 
            print(f"Invalid entry. Please select a valid period.")

    return start, end


def get_airline_filter():
    while True:  
        print_airline_filters_input()     
        
        airline_input = input("Please inform the airline: ").strip()

        if wants_to_exit(airline_input):
            print("Exiting the system. Goodbye!")
            exit()

        airline = airline_input.title()

        return airline


def get_api_filters(): 
    """
    Gets the start and end date, and also the airline filters.
    """

    start, end = get_date_filters()
    airline = get_airline_filter()

    filters = { 
        "flight_date": start,
        "airline_name": airline
    }

    return filters

