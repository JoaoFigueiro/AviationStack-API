import os
import requests
import pandas as pd 

from dotenv import load_dotenv
from input_messages import print_welcome
from data_filtering import get_api_filters


def get_flights_data(params={}):
    """
    Returns the flights with the given filters or a sample data 
    with one hundred flights if no filters were provided. 
    """

    load_dotenv()
    access_key = os.getenv("ACCESS_KEY")

    params["access_key"] = access_key

    try: 
        url = "https://api.aviationstack.com/v1/flights"

        api_result = requests.get(url, params)
        api_response = api_result.json()
    except: 
        print(f"Error during request!")    

    return api_response


def transform_json_to_dataframe(json):
    json = json.get("data")
    dataframe = pd.DataFrame(json)

    return dataframe


def get_flights():
    """
    Asks if the user want to filter flights or just
    get a sample. Also gets to filter
    """

    while True:  
        print_welcome()
        
        try:
            option = int(input("Please choose an option [0, 1, 2]: "))
            if option in [0, 1, 2]:  
                break  
            else:
                print("Invalid entry. Please select a valid option: 0, 1, or 2.")
        except ValueError:  
            print("Please, type a valid option [0, 1, 2] using numeric values.")

    if option == 0:
        print("Exiting the system. Goodbye!")
        exit()

    elif option == 1:
        print("Fetching a sample of flights...")
        flights_data = get_flights_data()

    elif option == 2:
        print("Entering the filter mode...")
        filters = get_api_filters()
        flights_data = get_flights_data(filters)

    flights_data = transform_json_to_dataframe(flights_data)

    return flights_data