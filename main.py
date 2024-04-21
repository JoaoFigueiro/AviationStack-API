import pandas as pd 

from load_data import get_flights
from storage_data import store_flights_data
from data_analysis import get_data_analysis
from data_filtering import data_filtering


def main(): 
    flights_data = get_flights()

    print(flights_data.head())
    
    if flights_data.empty: 
        print("Sorry, Empty Dataframe!")
        exit()

    store_flights_data(flights_data)

    filter = input("Do you want to apply filters? Y/N ")

    if filter == "Y": 
        data_filtering(flights_data)
        
    get_data_analysis(flights_data)
        

if __name__ == "__main__": 
    pd.set_option('display.max_columns', None)

    main()