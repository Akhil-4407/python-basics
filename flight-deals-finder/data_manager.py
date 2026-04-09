import requests
import os
from requests.auth import HTTPBasicAuth
from flight_search import FlightSearch
from dotenv import load_dotenv
load_dotenv(".env")
class DataManager:
    def __init__(self):
        self.user = os.getenv("SHEETY_USERNAME")
        self.password = os.getenv("SHEETY_PASSWORD")
        self.flight_search  =FlightSearch()
    def update_sheets(self,data):
        update_config = {
            "price": {
                "iataCode": self.flight_search.get_code(data["city"])
            }
        }
        responce = requests.put(
            url=f"https://api.sheety.co/bb4701acf5e66b1faf9ee65777a1e0c7/flightDeals/prices/{data["id"]}",
            json=update_config,
            auth=(self.user,self.password)
        )


