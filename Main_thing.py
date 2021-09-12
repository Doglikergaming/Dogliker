import random
from Characters import characters
from Equipment import equipment
from Spending import spending
import Text

print("                   	    RPG 1")

input("             		Press Enter")			


# Assigning stats and characters

Character = input("Play as a mage [1] or knight [2].")

if Character == "1":
	hero = characters("Mage", 70, 70, 40, 40, 2, 10, -1, 2, 2, 5, 10, 0, 50, 1, 0)
	

elif Character == "2":
	hero = characters("Knight", 100, 100, 10, 10, 8, 2, 3, -1, 3, 5, 10, 0, 50, 1, 0)
	
	
elif Character == "XI - Justice":
	hero = characters("Miss Justice", 50, 50, 50, 50, 50, 50, 50, 50, 5, 50, 5, 0, 50, 1, 50)
	
	
elif Character == "0 - The Fool":
	hero = characters("Mr. Fool", 10000, 10000, 10000, 10000, 100, 1000, 1000, 10000, 20, 100, 333, 5000, 7500, 100, 100)
	
elif Character == "XXII - The World":
	hero = characters("Mr. Sparrow", 80, 80, 75, 75, 10, 10, 2, 1, 2, 10, 5, 0, 50, 1, 500)

weapon1 = equipment("Stick", 0, 0, 0, 0, 1, 0, 0)
armor1 = equipment("Shirt", 0, 0, 0, 0, 1, 0,0)
ring1 = equipment("Wooden ring", 0, 0, 0, 0, 1, 0, 0)
ring2 = equipment("Silver ring", 0, 0, 0, 0, 1, 0, 0)
		

xp = experience()
atk_choice = attack_choice()
stats = level_up_stats()
purchase = spending()
weapon_discarder = weapons()
armor_discarder = armors()
ring_discarder = rings()

weapon1.pickup_equipment(weapon1, "Stick", 0, 0, 0, 0, 1, 0, 0)
armor1.pickup_equipment(armor1, "Shirt", 0, 0, 0, 0, 1, 0, 0)
ring1.pickup_equipment(ring1, "Wooden ring", 0, 0, 0, 0, 1, 0, 0)
ring2.pickup_equipment(ring2, "Silver ring", 0, 0, 0, 0, 1, 0, 0)

# Assigning stats and characters


print("You chose the", hero.name,"so go now and save the world.")
print("")

input("A shady woman appears and behaves disgustingly, so she's    categorized as a pig. This is the perfect training prop for battle!")
print("")

enemy = character("Pig", 10, 10, 0, 0, 5, 0, 1, 0, 4, 1, 1, 0, 0, 0, 0)


# Fight against the pig

while enemy.hp > 0:

	print(hero)
	print(enemy)
	print("")
	choice = input(atk_choice)
	print("")
	
	
	dice = random.randint(1, 2)
	dice1 = random.randint(1, 2)
	
	
# Case of the enemy attacking first
	
	if enemy.agl > hero.agl or enemy.agl == hero.agl and dice == 1:
		
		if dice1 == 1 or enemy.mp - enemy.mp_cost < 0:
			enemy.attack(enemy, hero, enemy.str, hero.defe)
			
		if dice1 == 2 and enemy.mp - enemy.mp_cost >= 0:
			enemy.attack(enemy,hero,enemy.int, hero.res)
			enemy.mp_loss(enemy)
			
			
		if choice == "p" or choice == "1":
			hero.attack(hero, enemy, hero.str, enemy.defe)
			
			
		if choice == "m" or choice == "2":	
		
			if hero.mp - hero.mp_cost >= 0:
				hero.attack(hero, enemy, hero.int, enemy.res)
				hero.mp_loss(hero)
				
			else:
				hero.mp_ditch(hero)
				
# Case of the enemy attacking first
	
	
# Case of the hero attacking first
				
	else:
		
		
		if choice == "p" or choice == "1":
			hero.attack(hero, enemy, hero.str, enemy.defe)
			
			
		if choice == "m" or choice == "2":	
		
			if hero.mp - hero.mp_cost >= 0:
				hero.attack(hero, enemy, hero.int, enemy.res)
				hero.mp_loss(hero)
				
			else:
				hero.mp_ditch(hero)
		
		
		if dice1 == 1 or enemy.mp - enemy.mp_cost < 0:
			enemy.attack(enemy, hero, enemy.str, hero.defe)
			
		if dice1 == 2 and enemy.mp - enemy.mp_cost >= 0:
			enemy.attack(enemy, hero, enemy.int, hero.res)
			enemy.mp_loss(enemy)
		
# Case of hero attacking first
	
		
	print("")
print("You win")
purchase.gold_gain(10)
hero.xp_gain(20, hero)

# Fight against the pig
	
	
chest = input("You find a treasure chest. Do you want to approach it?      Press y/1 to approach or n/2 to ignore it.")

if chest == "y" or chest == "1":
	print("A giant appears in your way. Fight!")
	print("")
	
	
# Fight against the giant
	
	enemy = character("Giant", 50, 50, 5, 5, 10, 3, 3, -2, 1, 7, 5, 0, 0, 0, 0)
	
while enemy.hp > 0:

	print(hero)
	print(enemy)
	print("")
	choice = input(atk_choice)
	print("")
	
	
	dice = random.randint(1, 2)
	dice1 = random.randint(1, 2)
	

# Case of the enemy attacking first
	
	if enemy.agl > hero.agl or enemy.agl == hero.agl and dice == 1:
		
		if dice1 == 1 or enemy.mp - enemy.mp_cost < 0:
			enemy.attack(enemy, hero, enemy.str, hero.defe)
			
		if dice1 == 2 and enemy.mp - enemy.mp_cost >= 0:
			enemy.attack(enemy, hero, enemy.int, hero.res)
			enemy.mp_loss(enemy)
			
			
		if choice == "p" or choice == "1":
			hero.attack(hero, enemy, hero.str, enemy.defe)
			
			
		if choice == "m" or choice == "2":	
		
			if hero.mp - hero.mp_cost >= 0:
				hero.attack(hero, enemy, hero.int, enemy.res)
				hero.mp_loss(hero)
				
			else:
				hero.mp_ditch(hero)
				
# Case of the enemy attacking first
	
	
# Case of the hero attacking first
				
	else:
		
		
		if choice == "p" or choice == "1":
			hero.attack(hero, enemy, hero.str, enemy.defe)
			
			
		if choice == "m" or choice == "2":	
		
			if hero.mp - hero.mp_cost >= 0:
				hero.attack(hero, enemy, hero.int, enemy.res)
				hero.mp_loss(hero)
				
			else:
				hero.mp_ditch(hero)
				
		if dice1 == 1 or enemy.mp - enemy.mp_cost < 0:
			enemy.attack(enemy, hero, enemy.str, hero.defe)
			
		if dice1 == 2 and enemy.mp - enemy.mp_cost >= 0:
			enemy.attack(enemy, hero, enemy.int, hero.res)
			enemy.mp_loss(enemy)
		
# Case of the hero attacking first

		
	print("")
	
# Fight against the giant
	
	
# Treasure chest and weapons

if chest == "y" or chest == "1":
	print("You win")
	purchase.gold_gain(100)
	hero.xp_gain(200)
	
	Weapon = input("After defeating the giant, you open the chest. There's a    sword in it, that will give you 3 str but -1 int. The giant groans and offers you a magic wand if you give up on the    sword. That magic wand will give you 2 int and 1 str. Enter [1] to decline the giant and grab the sword or [2] to       accept the giant's offer and receive the wand.")

	if Weapon == "1":
		weapon1.pickup_equipment(weapon1, "Wooden sword", 3, -1, 0, 0, 1, -1, 0)
		
	if Weapon == "2":
		weapon1.pickup_equipment(weapon1, "Wand of Lochria", 1, 2, 0, 0, 1, -1, 0)

# Treasure chest and weapons

if chest == "n" or chest == "2":
	print("You pass on the chest but doubt lingers in your mind.")

print("")
print("You encounter a merchant. He offers you a leather armor     which will increase your Def and Res by 1 point each.")
print("")
purchase.spend(25, armor1, "Leather armor", 2, 0, 0, 1, 1, 1, 0, 0)