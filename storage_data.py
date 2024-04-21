import json 
import psycopg2

from sqlalchemy import create_engine, types

def save_data_in_csv(flight_data):
    """
    Saves data in CSV file.
    """
    try: 
        flight_data.to_csv('flights_data.csv')
    except: 
        print("Save ata in CSV Error!")

def save_data_in_postgres(flight_data):
    """
    Saves data in a localhost postgres database.
    """

    conn = psycopg2.connect(
        dbname="flights_data",
        user="postgres",
        password="postgres",
        host="localhost"
    )

    engine = create_engine(
        "postgresql://postgres:postgres@localhost/flights_data"
    )

    flight_data['departure'] = flight_data['departure'].apply(json.dumps)
    flight_data['arrival'] = flight_data['arrival'].apply(json.dumps)
    flight_data['airline'] = flight_data['airline'].apply(json.dumps)
    flight_data['flight'] = flight_data['flight'].apply(json.dumps)
    flight_data['aircraft'] = flight_data['aircraft'].apply(json.dumps)
    

    flight_data.to_sql(
        "flights_data", 
        engine, 
        if_exists="replace", 
        index=False
    )

    conn.close()


def store_flights_data(flight_data): 
    """
    Stores the flight data in a CSV file and in a Postgres Database.
    """

    save_data_in_csv(flight_data)
    #save_data_in_postgres(flight_data)