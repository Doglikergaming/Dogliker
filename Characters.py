

class characters:
		
# Class attributes to define stats
	
	def __init__(self, name, max_hp, hp, max_mp, mp, str, int, defe, res, agl, crit, mp_cost, xp, needed_xp, level, gold):
		self.name = name
		self.hp = hp
		self.max_hp = max_hp
		self.mp = mp
		self.max_mp = max_mp
		self.str = str
		self.int = int
		self.defe = defe
		self.res = res
		self.agl = agl
		self.crit = crit
		self.mp_cost = mp_cost
		self.xp = xp
		self.needed_xp = needed_xp
		self.level = level
		self.gold = gold
		
# Class attributes to define stats
	
	
# Attack handling
		
	def attack(self, attacker, target, damage, resdef):
		
		if attacker.name == enemy.name and attacker.hp > 0:
			
			if random.randint(0,99) + attacker.crit >= 100:
				
				while damage * 2 - resdef < 0:
					resdef -= 1
				
				target.hp -= damage * 2 - resdef
				print("Critical hit! You got attacked for",damage * 2 - resdef,"damage.")
		
			else:
				
				while damage - resdef < 0:
					resdef -= 1
				
				print("You got hit for",damage - resdef,"damage.")
				target.hp -= damage - resdef
				
			if hero.hp <= 0:
				print("You died")
				quit()
				
		elif attacker.name == hero.name:
			
			if random.randint(0,99) + attacker.crit >= 100:
				
				while damage * 2 - resdef < 0:
					resdef -= 1
					
				print("Critical hit! You dealt",damage * 2 - resdef,"damage.")
				target.hp -= damage * 2 - resdef
				
			else:
						
				while damage - resdef < 0:
					resdef -= 1
				
				print("You dealt",damage - resdef,"damage.")
				target.hp -= damage - resdef

# Attack handling
	
	
# MP handling
			
	def mp_loss(self, caster):
		self.caster = caster
		caster.mp -= caster.mp_cost
		
	def mp_ditch(self, dummy):
			dummy.mp += 10
			print("You don't have enough MP to do that but you get 10 back for trying anyways.")
			
# MP handling
	
				
	def __str__(self):
		return "%s (%d/%d HP)   (%d/%d MP)   %d Agl" % (self.name, self.hp, self.max_hp, self.mp, self.max_mp, self.agl)
		
		
# Getting gold

	def gold_gain(self, gain):
		self.gain = gain
		hero.gold += gain
		print("You got",gain,"gold. You now have",hero.gold,"gold.")
		
# Getting gold
		
# XP and level-ups
	
	def xp_gain(self, gain):
		self.gain = gain
		hero.xp += gain
		print(xp)
		print("")
		
		while hero.xp >= hero.needed_xp:
			levelling = 1
			hero.max_hp += 5
			hero.hp = hero.max_hp
			hero.max_mp += 5
			hero.mp = hero.max_mp
			hero.str += 1
			hero.int += 1
			hero.xp -= hero.needed_xp
			hero.needed_xp *= 1.3
			hero.level += 1
			
			if hero.level % 5 == 0:
				hero.agl += 1
				hero.defe += 1
				hero.res += 1
			
			print("")
			
			if hero.level == 2:
				print("Level up! You are now level",hero.level,"and can upgrade a stat of yourchoice. Max stats gain +5 per upgrade, the others +1. Each  level up also levels all except Crit chance and Agl, Def andRes once as well as a random one twice. Agl can only be up- graded automatically and it happens every 5 levels. Def and Res come in play when you attack physically or magically andwhen you get attacked. Def for physical attacks, Res for    magical ones. Def and Res also automatically upgrade once   every 5 levels. The crit chance is given in %, so it caps at100.")
				print("")
		
			else:
				print("Level up! You are now level",hero.level,"and can upgrade a stat of yourchoice.")
		
			print("")
			
			if hero.crit == 100:
				level_upping = random.randint(0,7)
			else:
				level_upping = random.randint(1,8)
			if level_upping == 1:
				hero.max_hp += 5
			if level_upping == 2:
				hero.max_mp += 5
			if level_upping == 3:
				hero.agl += 1
			if level_upping == 4:
				hero.str += 1
			if level_upping == 5:
				hero.int += 1
			if level_upping == 6:
				hero.defe += 1
			if level_upping == 7:
				hero.res += 1
			if level_upping == 8:
				hero.crit += 1
			
			print(stats)
			print("")
			
			if hero.crit >= 100:
				level_upping = input("Enter the number corresponding to the stat you with to up-   grade. (1 - 6, from left to right)")
			else:
				level_upping = input("Enter the number corresponding to the stat you wish to up-  grade. (1 - 7, from left ro right")
			print("")
			
			if level_upping == "1":
				hero.max_hp += 5
			if level_upping == "2":
				hero.max_mp += 5
			if level_upping == "3":
				hero.str += 1
			if level_upping == "4":
				hero.int += 1
			if level_upping == "5":
				hero.defe += 1
			if level_upping == "6":
				hero.res += 1
			if level_upping == "7" and hero.crit < 100:
				hero.crit += 1
			
			if hero.needed_xp > hero.xp:
				hero.hp = hero.max_hp
				hero.mp = hero.max_mp
				print("")
				print("Final stats")
				print("")
				print(stats)
				print("")
				print("")
				
# XP and level-ups