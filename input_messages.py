import json

import pandas as pd 

def print_airline_filters_input():
    airline_filter_message = """
    ======================================
    Please, inform the desired airline.

    (e.g Tibet Airlines, American Airlines)
 
    Type 0 to exit the program.
    ======================================
    """

    print(airline_filter_message)


def print_date_filters_input():
    date_filter_message = """
    ======================================
    Please, inform the desired date period,
    separating the two date with a space,
    in the format YYYY-MM-DD YYYY-MM-DD.

    The first one will be the start date and 
    the last one will be the end date.  

    (e.g 2024-01-01 2024-02-01).

    Type 0 to exit the program.
    ======================================
    """

    print(date_filter_message)


def print_welcome(): 
    welcome_message = """
    ====================================
    Hello, welcome to Flight Analysis  
    - The system that will make you fly!!
    
    Do you want to filter some flight or
    just get a sample? (Type the number)

    1 - Sample
    2 - Filter

    0 - Exit

    ====================================
    """

    print(welcome_message)


def print_ask_columns(dataframe): 
    options = ",\n    ".join(dataframe.columns)

    columns_message = f""""
    ========================================
    Please, select one of the columns below
    to apply the filters. 

    {options}

    Type 0 to exit the program.
    ========================================
    """

    print(columns_message)


def print_ask_operations(): 
    operations = """
    ==============================================
    Please, inform the operation you want to apply
    in the column of your DataFrame: 

        - eq = equals
        - ne = not equal
        - gt = greater than
        - lt = less than 

    Type 0 to exit the program.
    =============================================
    """

    print(operations)


def extract_keys(dictionary):
    return list(dictionary.keys())


def print_json_columns(dataframe, column): 
    keys_column = list(dataframe[column].iloc[0].keys())

    json_cols_message = f"""
    ================================================
    The column that you select is a json, so could 
    you please, select the column you want to filter? 

    Options available: 
    {keys_column}
    ================================================
    """

    print(json_cols_message)