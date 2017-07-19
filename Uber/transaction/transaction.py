class Transaction:
    paid_by_cash = 0
    paid_by_wallet = 0

    def __init__(self, ride):
        self.ride = ride
    
    @staticmethod
    def end_ride_transaction(self):
        '''
	Deduct the trip price from wallet money. If the wallet money
	is less than the calculated fare, the remaining amount after
	deduction from wallet is to be paid in cash. 
	'''
	user, price = self.ride.user, self.ride.price
	current_wallet_money = user.wallet.current_money()

	if current_wallet_money >= price:
	    user.wallet.deduct_money(price)
	    self.paid_by_wallet = price
	    return
        
        self.paid_by_wallet = current_wallet_money
	user.wallet.deduct_money(current_wallet_money)
	self.paid_by_cash = price - self.paid_by_wallet
