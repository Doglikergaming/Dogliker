


# Class for applying equipment bonuses

class equipment:
	
	def __init__(self, name, str, int, defe, res, cheap_mp, weight, crit):
		self.name = name
		self.str = str
		self.int = int
		self.defe = defe
		self.res = res
		self.cheap_mp = cheap_mp
		self.weight = weight
		self.crit = crit
		
	def __str__(self):
		return "You picked up the %s." % (self.name)
		
	def pickup_equipment(self, equipment, name1, str1, int1, defe1, res1, cheap_mp1, weight1, crit1):
		
		if equipment == weapon1:
			discard = input(weapon_discarder)
		
		if equipment == armor1:
			discard = input(armor_discarder)
			
		if equipment == ring1:
			discard = input(ring_discarder)
		
		if discard == "1" or discard == "y" or equipment == ring1 and discard == "2" or equipment == ring2 and discard == "2":
			
			if equipment == ring1 and discard == "2":
				equipment = ring2
				
			hero.str -= equipment.str
			hero.int -= equipment.int
			hero.defe -= equipment.defe
			hero.res -= equipment.res
			hero.mp_cost /= equipment.cheap_mp
			hero.agl += equipment.weight
			hero.crit -= equipment.crit
			
			equipment.name = name1
			equipment.str = str1
			equipment.int = int1
			equipment.defe = defe1
			equipment.res = res1
			equipment.cheap_mp = cheap_mp1
			equipment.weight = weight1
			equipment.crit = crit1
			
			hero.str += equipment.str
			hero.int += equipment.int
			hero.defe += equipment.defe
			hero.res += equipment.res
			hero.mp_cost *= equipment.cheap_mp
			hero.agl -= equipment.weight
			hero.crit += equipment.crit
	
# Class for applying equiment bonuses