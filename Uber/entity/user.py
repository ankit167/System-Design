class User(object):
	def __init__(self, user_id, user_name):
		self.user_id = user_id
		self.user_name = user_name
		self.current_ride = None

	def book_ride(self, source, destination):
		self.current_ride = App.book_ride(self, source, destination)

	def cancel_ride(self):
		if self.current_ride.ride_state = Ride_State.IN_PROGRESS:
			print "Ride started. Can't cancel!"
			return
		App.cancel_ride(self.current_ride)