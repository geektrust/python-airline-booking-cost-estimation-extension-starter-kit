from booking import Booking


class Main:
    def __init__(self):
        self.booking = Booking()

    def handle(self, input_command: str):
        input_list = input_command.strip().split()
        command = input_list[0]

        if command == "PASSENGER":
            passenger_type = input_list[1]
            number_of_passengers = int(input_list[2])

            self.booking.set_passenger(
                passenger_type,
                number_of_passengers
            )

        elif command == "ADD_SERVICE":
            """
            Extension point.

            You should implement support for:
            SHUTTLE
            LOUNGE_ACCESS
            """
            pass

        elif command == "TOTAL_COST":
            print(
                f"Total Booking Cost: "
                f"{self.booking.calculate_flight_cost()}"
            )

        else:
            print("INVALID_COMMAND")