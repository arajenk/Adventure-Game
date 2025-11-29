from character import Enemy
#Enemy Subclasses
class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 60, 10, 3 , 5)
        self.xp_reward = 25
class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 90, 15, 5, 10)
        self.xp_reward = 15
class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 200, 25, 10, 20)
        self.xp_reward = 60