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
            xp_gain = self.enemy.xp_reward
            self.player.xp += xp_gain
            print(f'{self.player.name} gained 25 XP')
            if self.player.xp >= self.player.xp_to_level:
                self.player.level_up()
                self.player.xp -= self.player.xp_to_level
        else:
            print(f"{self.enemy.name} wins the battle...")     