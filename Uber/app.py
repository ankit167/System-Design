class App(object):
	def __init__(self, drivers):
		self.drivers = drivers
		self.memcache = Memcache()

	def book_ride(user, source, destination):
		price = Pricing.calculate_price(source, destination)
		nearby_drivers = self.memcache.get(source)

		if not nearby_drivers:
			nearby_drivers = []
		    for driver in self.drivers:
			    if driver.current_ride is None and Location.check_proximity(source, driver.current_location):
				    nearby_drivers.append(driver)
				    self.memcache.set(source, driver)
			if len(nearby_drivers) == 0:
				print 'No cabs!'
				return None

		selected_driver = nearby_drivers[randint(0, len(nearby_drivers))]
		ride = Ride(user, selected_driver, source, destination, price)
		selected_driver.take_ride(ride)
		return ride

	def start_ride(ride):
		ride.ride_state = Ride_State.IN_PROGRESS

	def end_ride(ride):
		ride.ride_state = Ride_State.COMPLETE

	def cancel_ride(ride):
		ride.ride_state = Ride_State.CANCELLED
		ride.user.current_ride = None
		ride.driver.current_ride = None