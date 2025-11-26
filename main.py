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
        
        
# Player Class
class Player(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)

# Enemy Class
class Enemy(Character):
    def __init__(self, name, health, strength, defense, crit):
        super().__init__(name, health, strength, defense, crit)

# Main 

print("----------------------------------")
print("Welcome to Arajen's Adventure Game!")
print("----------------------------------")
print("1. Create Save")
print("2. Load Save")
print("3. Settings")
print("4. Exit")
choice = input("Enter your choice: ")
