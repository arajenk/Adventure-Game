# Adventure Game 

# Character Class
class Character:
    def __init__(self, name, health, strength, defense, crit):
        self.name = name
        self.health = health
        self.strength = strength
        self.defense = defense
        self.crit = crit
    def is_alive(self): 
        return self.health > 0
    def calculate_damage(self, target): 
        if(self.strength > target.defense):
            return self.strength - target.defense
        else:
            return 0
    def take_damage(self, damage):  
        self.health -= damage
        if self.health < 0:
            self.health = 0
    def attack(self,target): 
        damage = self.calculate_damage(target)
        target.take_damage(damage)
        print(f'{self.name} dealt {damage} damage to {target.name}') 
        if not target.is_alive():
            print(f"{target.name} has been defeated!")
# Player Class
class Player(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)

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
        while self.player.is_alive() and self.enemy.is_alive():
            self.player.attack(self.enemy)
            if not self.enemy.is_alive():
                break
            self.enemy.attack(self.player)       
             
# Main 
print("----------------------------------")
print("Welcome to Arajen's Adventure Game!")
print("----------------------------------")
print("1. Create Save")
print("2. Load Save")
print("3. Settings")
print("4. Exit")
choice = input("Enter your choice: ")
