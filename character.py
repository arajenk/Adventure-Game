import random
# Character Class
class Character:
    def __init__(self, name, health, strength, defense, crit):
        self.name = name
        self.health = health
        self.max_health = health
        self.strength = strength
        self.defense = defense
        self.crit = crit
    def is_alive(self): 
        return self.health > 0
    def crit_chance(self):
        crit_randomizer = random.random()
        if (self.crit/100) > crit_randomizer:
            return True
        else:
            return False
    def calculate_damage(self, target): 
        if(self.strength > target.defense):
            damage = self.strength - target.defense
        else:
            damage = 0
        if self.crit_chance():
            return damage * 2, True # crit
        else:
            return damage, False # no crit
    def take_damage(self, damage):  
        self.health -= damage
        if self.health < 0:
            self.health = 0
    def attack(self,target): 
        damage, is_critical = self.calculate_damage(target)
        target.take_damage(damage)
        if is_critical:
            print("Critical Hit!")
        print(f'{self.name} dealt {damage} damage to {target.name}') 
        print(f"{target.name}'s health is now {target.health} HP")
        if not target.is_alive():
            print(f"{target.name} has been defeated!")
    def show_stats(self):
        print(f"\n{self.name} | Level {self.level}")
        print(f"HP: {self.health}/{self.max_health}")
        print(f"STR: {self.strength} | DEF: {self.defense} | CRIT: {self.crit}%")
    
# Player Class
class Player(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)
        self.level = 1
        self.xp = 0
        self.xp_to_level = 100 #xp needed to lvl up
    def heal(self):
        heal_amount = 15
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f'{self.name} healed for {heal_amount} HP!')
        print(f"{self.name}'s health is now {self.health}/{self.max_health} HP")
    def level_up(self):
        self.level +=1
        self.max_health +=10
        self.health = self.max_health #heals to full on lvl up
        self.strength += 2
        self.defense += 1
        self.crit +=1
        print(f"{self.name} leveled up to Level {self.level}!")
        print(f"Stats increased: +10 HP, +2 STR, +1 DEF, +1% CRIT")
# Enemy Class
class Enemy(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)
