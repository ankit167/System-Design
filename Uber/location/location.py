class Location(object):
    radius = 2

    def __init__(self, lat, lon):
        self.lat = lat
        self.long = lon
    
    @staticmethod
    def find_distance(source, destination):
        x = (source.lat - destination.lat)**2
        y = (source.long - destination.long)**2
        distance = int(math.sqrt(x+y))

        return distance
    
    @staticmethod
    def check_proximity(user_location, driver_location):
        distance = find_distance(user_location, driver_location)
        if distance <= self.radius:
            return True
        return False