import sys
import os.path
folder = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(folder)
# Import your functions

from rpg.enemy import Enemy  # noqa: E402
from rpg.enemy import Skeleton  # noqa: E402

from rpg.player import Player  # noqa: E402

if __name__ == "__main__":
<<<<<<< HEAD
    # enemy = Enemy()
    # enemies = Enemy.create_enemies()
    # print(enemies)
    skeleton = Skeleton(5)
=======
    enemy = Enemy()
    print(enemy)
    print(enemy.name)
>>>>>>> bf824ab27f088bf3d249d3a6d9767ed2b97de424
