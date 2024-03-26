import sys
import os.path
folder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(folder)
# Import your functions

from rpg.player import Player  # noqa: E402
# from rpg.item import Item
from rpg.enemy import Enemy  # noqa: E402
# import random  # noqa: E402
# from lecture6.rpg.enemy import Enemy
# from lecture6.rpg.maze import Maze
# from lecture6.rpg.item import Item

if __name__ == "__main__":
    # Create a player
    # arthur = Player("Arthur")
    # Arrow1 = Item("Arr1","The first arrow","Arrow")
    # Heart1 = Item("Heart1","The first Heart","Heart")
    # Key1 = Item("Key1","The first Heart","Key")
    # print(arthur.health)
    # # arthur.take_damage(50)
    # arthur.pickup(Arrow1)
    # print(arthur.health)
    # arthur.pickup(Heart1)
    # print(arthur.health)
    # print(arthur)
    # arthur.pickup(Key1)
    # print(arthur)
    enemy = Enemy()
    enemy.name = "Goblin"
    print(enemy.name)
    print(enemy.health)
    # enemy.health = 100
    # print(enemy.health.__doc__)
    # enemy.set_name("Goblin")
    # enemy.set_health(50)
    
    
    # gohan = Player(name="Gohan",health=150)
    # trunks = Player("Trunks")
    # print(gohan>trunks)
    # gotenks = gohan+trunks
    # print(gotenks)
    # super_gohan = gohan+100
    # print(super_gohan)
    # player = Player("Link", 150)
    # enemy = Enemy("Ganon")
    # game_action = [player.attack, enemy.attack]
    
    # while (player.health > 0) and (enemy.health >0):
    #     action = random.choice(game_action)
    #     if action == player.attack:
    #         action(enemy, 20)
    #     elif action == enemy.attack:
    #         action(player, 30)
    #     else:
    #         print("Invalid action")
    # player1 = Player("Player1")
    # player2 = Player("Player2")
    # print(player1)