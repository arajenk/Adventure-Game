# Adventure Game - Arajen 
from character import Player 
from battle import Battle
from enemies import Goblin, Orc, Dragon
# Main 
def main():
    print("----------------------------------")
    print("Welcome to Arajen's Adventure Game!")
    print("----------------------------------")
    #Test
    player = Player("Arajen", 100, 15, 5, 20)
    enemy = Orc()  # Try Goblin(), Dragon(), etc.
    battle = Battle(player, enemy)
    battle.start_battle()

if __name__ == "__main__":
    main()


