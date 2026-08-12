

class Booking:

    BASE_FARE = 5000

    def __init__(self):
        self.passenger_type = None
        self.passenger_count = 0

    def set_passenger(self, passenger_type: str, passenger_count: int):
        self.passenger_type = passenger_type
        self.passenger_count = passenger_count

    def calculate_flight_cost(self) -> int:
        if self.passenger_type == "ADULT":
            return self.passenger_count

        elif self.passenger_type == "CHILD":
            return self.passenger_count

        elif self.passenger_type == "SENIOR":
            return self.passenger_count

        return 0