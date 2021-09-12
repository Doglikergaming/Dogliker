

class experience:
	
	def __init__(self):
		self = self
		
	def __str__(self):
		return "You gain %d xp. You now have (%d/%d) xp." % (hero.gain, hero.xp, hero.needed_xp)
	
	
# Class for choosing what attack to use
	
class attack_choice:
	
	def __init__(self):
		self = self
		
	def __str__(self):
		return "Attack physically (%d dmg) or magically (%d dmg, %d MP cost)?	Enter 1/p for physical or 2/m for magical." % (hero.str, hero.int, hero.mp_cost)
		
# Class for choosing what attack to use
	
	
# Class for displaying stats during level-        ups
	
class level_up_stats:
	
	def __init__(self):
		self = self
		
	def __str__(self):
		
		if hero.crit == 100:
			return " %d HP | %d MP | %d Str | %d Int | %d Def | %d Res" % (hero.max_hp, hero.max_mp, hero.str, hero.int, hero.defe, hero.res)
			
		else:	
			return " %d HP | %d MP | %d Str | %d Int | %d Def | %d Res | %d Crit ch." % (hero.max_hp, hero.max_mp, hero.str, hero.int, hero.defe, hero.res, hero.crit)
			
# Class for displaying stats during level-        ups


# Classes for questions whether and what     equipment to swap

class weapons:
	
	def __init__(self):
		self = self
		
	def __str__(self):
		return "Do you want to swap out your %s (%d str, %d int, %d def, %d res, %d mp cost multiplier, %d weight, %d crit chance) for this weapon? 		Enter y/1 to confirm or n/2 to deny." % (weapon1.name, weapon1.str, weapon1.int, weapon1.defe, weapon1.res, weapon1.cheap_mp, weapon1.weight, weapon1.crit)



class armors:
	
	def __init__(self):
		self = self
		
	def __str__(self):
		return "Do you want to swap out your %s (%d str, %d int, %d def, %d res, %d mp cost multiplier, %d weight, %d crit chance) for this armor? 		Enter y/1 to confirm or n/2 to deny." % (armor1.name, armor1.str, armor1.int, armor1.defe, armor1.res, armor1.cheap_mp, armor1.weight, armor1.crit)
		
		
		
class rings:
	
	def __init__(self):
		self = self
		
	def __str__(self):
		return "Do you want to swap the ring with %s (%d str, %d int, %d def, %d res, %d mp cost multiplier, %d weight, %d crit chance) or with %s (%d str, %d int, %d def, %d res, %d mp cost multiplier, %d weight, %d crit chance)? 		            Enter 1 for %s, 2 for %s or anything else to decline." % (ring1.name, ring1.str, ring1.int, ring1.defe, ring1.res, ring1.cheap_mp, ring1.weight, ring1.crit, ring2.name, ring2.str, ring2.int, ring2.defe, ring2.res, ring2.cheap_mp, ring2.weight, ring2.crit, ring1.name, ring2.name)
		
# Classes for questions whether and what     equipment to swap