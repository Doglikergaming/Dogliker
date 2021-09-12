


# Class for business

class spending:

	def __init__(self):
		self = self
		
	def spend(self, price, type, name, str, int, defe, res, cheap_mp, weight, crit):
		print("")
		self.price = price
		self.type = type
		self.name = name
		self.str = str
		self.int = int
		self.defe = defe
		self.res = res
		self.cheap_mp = cheap_mp
		self.weight = weight
		self.crit = crit
		
		buy = input(purchase)
		
		if hero.gold >= self.price and buy == "1" or hero.gold >= self.price and buy == "y":
			hero.gold -= self.price
			print("You bought the",self.name,"for",self.price,"gold.")
			print("")
			equipment.pickup(self.name, self.type, self.str, self.int, self.defe, self.res, self.cheap_mp, self.weight, self.crit)
			
		elif buy == "1" or buy == "y":
			print("You don't have enough gold to buy",self.name,"so you just go on.")
	
		else:
			print("You didn't buy the",self.name)
			
	def __str__(self):
		return "Do you want to buy %s for %d gold?				 Enter 1/y to confirm or 2/n to deny." % (self.name, self.price)

# Class for business