class Wallet:

    def __init__(self):
    	self.__money = 0
    
    # Add money to wallet
	def add_money(amount):
		self.__money += amount
    
    # Deduct money from wallet
	def deduct_money(amount):
		if self.__money >= amount:
		    self.__money -= amount
    
    # Return current money in wallet
	def current_money(amount):
		return self.__money