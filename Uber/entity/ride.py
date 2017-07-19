# Each ride can be in one of the following states
class Ride_State(object):
    READY = 0
    IN_PROGRESS = 1
    COMPLETE = 2
    CANCELLED = 3

class Ride(object):
    def __init__(self, user, driver, source, destination, price):
        # Default status of a new ride is READY
        self.ride_state = Ride_State.READY
        self.driver = driver
        self.user = user
        self.source = source
        self.destination = destination
        self.price = price
