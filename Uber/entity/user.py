class User(object):
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        # Indicates whether user is currently travelling or not.
        self.current_ride = None
        # Each user has a wallet
        self.wallet = Wallet()

    #
    # Accepts source and destination from the user, and calls App API
    # to book a ride.
    #
    def book_ride(self, source, destination):
        self.current_ride = App.book_ride(self, source, destination)

    #
    # User can cancel a booked ride. But, once a ride has started, he
    # cannot cancel the ride.
    #
    def cancel_ride(self):
        if self.current_ride.ride_state = Ride_State.IN_PROGRESS:
            print "Ride started. Can't cancel!"
            return
        App.cancel_ride(self.current_ride)