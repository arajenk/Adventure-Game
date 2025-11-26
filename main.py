# Adventure Game 
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
    
# Player Class
class Player(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)

    def heal(self):
        heal_amount = 15
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f'{self.name} healed for {heal_amount} HP!')
        print(f"{self.name}'s health is now {self.health}/{self.max_health} HP")
# Enemy Class
class Enemy(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)

#Battle Class
class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
    def start_battle(self):
        round_number = 1
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"\n--- Round {round_number} ---")

            print("\nChoose your action:")
            print("1. Attack")
            print("2. Heal")
            print("3. Run")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.player.attack(self.enemy)
            elif choice == "2":
                self.player.heal() 
            elif choice == "3":
                print(f"{self.player.name} ran away!")
                break
            if not self.enemy.is_alive():
                break
            self.enemy.attack(self.player)
            round_number+=1  
        if self.player.is_alive():
            print(f"{self.player.name} wins the battle!")
        else:
            print(f"{self.enemy.name} wins the battle...")     
# Main 
print("----------------------------------")
print("Welcome to Arajen's Adventure Game!")
print("----------------------------------")
print("1. Create Save")
print("2. Load Save")
print("3. Settings")
print("4. Exit")
choice = input("Enter your choice: ")

