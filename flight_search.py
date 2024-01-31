import requests
from datetime import datetime as dt
from datetime import timedelta

TEQUILA_APIKEY = "bR_f2mepYWhTRzKKoaY2bI-9T96oLyxQ"
TEQUILA_URL = "https://api.tequila.kiwi.com/locations/query"
TEQUILA_SEARCH_URL = "https://api.tequila.kiwi.com/v2/search"
header = {"apikey": TEQUILA_APIKEY}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.city_name = ""
        self.dest_data = {}
        self.iata_code = ""

    def iata_search(self):
        """Searches for the IATA code of the city"""
        params = {
            "term": self.city_name,
        }
        kiwi_response = requests.get(url=TEQUILA_URL, params=params, headers=header)
        kiwi_response.raise_for_status()
        data = kiwi_response.json()
        iata_code = data['locations'][0]['code']
        return iata_code

    def connection_search(self):
        """Searches for flight to each city in the google sheet"""
        tomorrow = dt.now() + timedelta(days=1)
        tomorrow_str = tomorrow.strftime('%d/%m/%Y')
        date_to = tomorrow + timedelta(days=180)
        date_to_str = date_to.strftime('%d/%m/%Y')

        params = {
                "fly_from": "LON",
                "fly_to": self.iata_code,
                "date_from": tomorrow_str,
                "date_to": date_to_str,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "ret_from_diff_city": "false",
                "ret_to_diff_city": "false",
                "one_for_city": 1,
                "curr": "USD",
                "locale": "en",
                "max_stopovers": 0,

        }
        response = requests.get(url=TEQUILA_SEARCH_URL, params=params, headers=header)
        response.raise_for_status()
        data = response.json()
        return data
