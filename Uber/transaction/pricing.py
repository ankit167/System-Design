class Pricing:
    price_rate = 10
    
    @staticmethod
    def calculate_price(source, destination):
        distance = Location.find_distance(source, destination)
        price = price_rate * distance
        return price
