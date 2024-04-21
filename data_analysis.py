import pandas as pd 
import matplotlib.pyplot as plt


def get_total_flights(dataframe): 
    total_flights = len(dataframe.index)
    return total_flights   


def get_avarage_flight_duration(dataframe): 
    dataframe['arrival_time'] = pd.to_datetime(dataframe["arrival"].apply(lambda x: x.get('scheduled')))
    dataframe['departure_time'] = pd.to_datetime(dataframe["departure"].apply(lambda x: x.get('scheduled'))) 
    
    flight_duration = dataframe['arrival_time'] - dataframe['departure_time']
    
    error_msg = "Null or Incorret values in flight duration:\n"
    print(error_msg, flight_duration[flight_duration <= pd.Timedelta(0)])
    
    avg_flight_duration = flight_duration.mean()
    
    return avg_flight_duration


def get_flights_per_airline(dataframe): 
    dataframe['airline_name'] = dataframe['airline'].apply(
        lambda x: x['name'] if isinstance(x, dict) and 'name' in x else None
    )
    flights_per_airline = dataframe.groupby('airline_name').size()
    return flights_per_airline


def get_data_charts(data, kind, name=None): 
    """
    Generate visualizations to display the results of analysis.
    """
    if kind == "num": 
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.text(0.5, 0.5, str(data), fontsize=45, ha='center')
        ax.axis('off')
        ax.set_title(name, fontsize=16)
    else: 
        plt.figure(figsize=(12, 8))
        data.plot(kind='bar')
        plt.title('Flights per Airline')
        plt.xlabel('Airline')
        plt.ylabel('Number of flights')
        plt.xticks(rotation=90) 
        plt.tight_layout()

    plt.show()


def get_data_analysis(dataframe): 
    """
    Performs a basic analysis of the data obtained, such as total number
    of flights, average flight duration, number of flights per airline.
    """
    total_flights = get_total_flights(dataframe)
    flights_per_airline = get_flights_per_airline(dataframe)
    avg_flight_duration = get_avarage_flight_duration(dataframe)

    print(f"Total flights: {total_flights}")
    print(f"Avarage Flight Duration: {avg_flight_duration}")
    print(f"Flights Per Airline: {flights_per_airline}")

    get_data_charts(total_flights, "num", "Total Flights")
    get_data_charts(avg_flight_duration, "num", "Mean Flight Duration")
    get_data_charts(flights_per_airline, "hist")
