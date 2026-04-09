#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests 
from dotenv import load_dotenv
import os
load_dotenv(".env")
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
api_endpt = os.environ.get("SHEETY_PRICES_ENDPOINT")
username= os.environ.get("SHEETY_USERNAME")
password= os.environ.get("SHEETY_PASSWORD")

responce = requests.get(url=f"{api_endpt}",auth=(username,password))
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = responce.json()
sheet_data = sheet_data["prices"]
ORIGIN_CITY_IATA ="DEN"
STAY_IN_DAYS = 14
for destination in sheet_data:
    print(f"Check for {destination["city"]}...")
    flight = flight_search.search(
        origin_code=ORIGIN_CITY_IATA,
        dest_code=destination["iataCode"],
        stay_duration=STAY_IN_DAYS
    )
    if flight is None:
        print(f"No flights found for {destination["city"]}.")
        continue
    if flight.price<destination["lowestPrice"]:
        print(f"Fly to {flight.destination_airport} for ${flight.price} on {flight.airline}.")
        print(f"Departure: {flight.out_date} | Return: {flight.return_date}")
    else:
        print(f"Flight found for ${flight.price}, but your target is ${destination['lowestPrice']}.")