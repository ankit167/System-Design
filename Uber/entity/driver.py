class Driver(object):
    def __init__(self, driver_id, driver_name, current_location):
        self.driver_id = driver_id
        self.driver_name = driver_name

        # TO DO- The current location needs to be updated in real time.
        self.current_location = current_location

        # To check availability of a driver
        self.current_ride = None

    # Assign a ride to a driver
    def take_ride(self, ride):
        self.current_ride = ride

    def cancel_ride(self):
        App.cancel_ride(self.current_ride)

    def start_ride(self):
        App.start_ride(self.current_ride)

    def end_ride(self):
        App.end_ride(self.current_ride)