class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city_name, departure_airport_IATA_code, arrival_city,
                 name_arrival_airport_IATA_code, outbound_date, inbound_date):
        self.price = price
        self.departure_city_name = departure_city_name
        self.departure_airport_IATA_code = departure_airport_IATA_code
        self.arrival_city = arrival_city
        self.name_arrival_airport_IATA_code = name_arrival_airport_IATA_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date

    def create_sms(self):
        """Creates the formatted message to be sent"""
        message = (f"Low price alert!Only ${self.price} to fly from"
                   f" {self.departure_city_name}-{self.departure_airport_IATA_code} to "
                   f"{self.arrival_city}-{self.name_arrival_airport_IATA_code}"
                   f" from {self.outbound_date} to {self.inbound_date}")
        return message
