import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/06c3b9fc04295f6f34394921c1cee71b/flightDealsCostiPenisoara/prices"
SHEETY_BEARER = "Bearer 123456CostiPenisoara"
headers = {"Authorization": SHEETY_BEARER}


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        """Retrieves data from the Sheety Google sheet"""
        response = requests.get(url=SHEETY_ENDPOINT, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['prices']

    def update_sheety(self):
        """Updates the IATA codes in Sheety Google sheet"""
        for entry in self.destination_data:
            body = {
                "price": {
                    "iataCode": entry['iataCode'],
                }
            }

            sheety_response = requests.request(method="PUT",
                                               url=f"https://api.sheety.co/06c3b9fc04295f6f34394921c1cee71b/"
                                               f"flightDealsCostiPenisoara/prices/{entry['id']}",
                                               json=body,
                                               headers=headers)
            sheety_response.raise_for_status()
