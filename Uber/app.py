#
# Central controller. Used to manage cab bookings.
#
class App(object):
    def __init__(self, drivers):
        self.drivers = drivers
        self.memcache = Cache()

    #
    # Books a nearby cab for an incoming request
    #
    def book_ride(user, source, destination):
        # calculate respective price
        price = Pricing.calculate_price(source, destination)

        # fetch nearby drivers from cache based on location
        nearby_drivers = self.memcache.get(source)

        #
        # If drivers set is not present in cache, query the drivers list.
        # Based on the driver availability and cab proximity to the source
        # location, book a relevant cab.
        #
        if not nearby_drivers:
            nearby_drivers = []
            for driver in self.drivers:
                if driver.current_ride is None and Location.check_proximity(source, driver.current_location):
                    nearby_drivers.append(driver)
                    self.memcache.set(source, driver)  # Adding enteries to cache
            if len(nearby_drivers) == 0:
                print 'No cabs!'
                return None

        # Select a random driver, from a list of nearby available drivers.
        selected_driver = nearby_drivers[randint(0, len(nearby_drivers))]

        # Create a ride instance
        ride = Ride(user, selected_driver, source, destination, price)

        # Sending request to the selected driver
        selected_driver.take_ride(ride)
        return ride

    def start_ride(ride):
        ride.ride_state = Ride_State.IN_PROGRESS

    def end_ride(ride):
        ride.ride_state = Ride_State.COMPLETE

    def cancel_ride(ride):
        ride.ride_state = Ride_State.CANCELLED
        # Once a ride is cancelled, both the user and the driver are free
        ride.user.current_ride = None
        ride.driver.current_ride = None