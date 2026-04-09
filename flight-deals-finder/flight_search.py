import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData
import time
load_dotenv(".env")
class FlightSearch:
    #This class is responsible for talking to the Flight Search API. 
    def __init__(self):
        self.api_key = os.environ.get("SERPAPI_KEY")
        
    def get_code(self,city):
        pass
    def search(self,origin_code,dest_code,stay_duration):
        print(f"Starting 6-month scan for {dest_code}...")
        best_price = float('inf')
        best_flight = None
        current_date = datetime.now() + timedelta(days=1)
        for i in range(0,180,30):
            out_bound = current_date + timedelta(days=i)
            return_date = out_bound + timedelta(days=stay_duration)

            out_str = out_bound.strftime("%Y-%m-%d")
            ret_str = return_date.strftime("%Y-%m-%d")
        
            params = {
                "engine": "google_flights",
                "departure_id":origin_code,
                "arrival_id":dest_code,
                "currency":"USD",
                "type":"1",
                "api_key":self.api_key,
                "outbound_date":out_str,
                "return_date":ret_str,
                "deep_search":"true"
            }
            try:
                responce = requests.get(url="https://serpapi.com/search",params=params)
                responce.raise_for_status()
                flight_data = responce.json()
                all_flights= flight_data.get("best_flights",[]) + flight_data.get("other_flights",[])
                if all_flights:
                    daily_cheapest = min(all_flights, key=lambda f: f.get('price', float('inf')))
                    daily_price = daily_cheapest.get('price',float('inf'))
                    if daily_price<best_price:
                        best_price = daily_price
                        airline = daily_cheapest["flights"][0].get('airline','Unknown')
                        best_flight = FlightData(
                            price=best_price,
                            origin_airport = origin_code,
                            destination_airport = dest_code,
                            out_date = out_str,
                            return_date = ret_str,
                            airline = airline
                        )
            except requests.exceptions.RequestException as e:
                print(f"  API Error skipping date {out_str}: {e}")

            time.sleep(1)
        return best_flight

    