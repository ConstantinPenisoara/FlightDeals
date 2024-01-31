#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_data_manager = DataManager()
city_flight_search = FlightSearch()
notification = NotificationManager()

sheet_data = flight_data_manager.get_data()

# Populate the sheet_data with the afferent IATA code
for entry in sheet_data:
    if entry['iataCode'] == "":
        city_flight_search.city_name = entry['city']
        entry['iataCode'] = city_flight_search.iata_search()
    else:
        continue

flight_data_manager.destination_data = sheet_data

# Populate Sheety Google sheet with the IATA codes
flight_data_manager.update_sheety()

city_flight_search.dest_data = sheet_data

# Searches for/ tries to find connections from origin (in this case London - fly_from) to each of the destinations in
# the sheet_data,  a connection is found, if the price is lower than the one specified in the data_sheet a sms message
# is being formatted and sent via Twilio. A SMS will be sent for each destination which meets the criteria.

for entry in sheet_data:
    city_flight_search.iata_code = entry['iataCode']
    try:
        trip_info = city_flight_search.connection_search()
        if entry['lowestPrice'] > trip_info['data'][0]['price']:
            formatted_flight_data = FlightData(trip_info['data'][0]['price'], trip_info['data'][0]['cityFrom'],
                                               trip_info['data'][0]['cityCodeFrom'], trip_info['data'][0]['cityTo'],
                                               trip_info['data'][0]['cityCodeTo'],
                                               trip_info['data'][0]['local_departure'].split("T")[0],
                                               trip_info['data'][0]['route'][1]['local_departure'].split("T")[0])
            sms_to_be_sent = formatted_flight_data.create_sms()
            notification = NotificationManager()
            notification.content = sms_to_be_sent
            notification.send_message()
        print(trip_info)
    except IndexError:
        print("No connection found for this destination")
