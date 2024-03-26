
import rpg.player 
from abc import ABC,abstractmethod
"""
This file contains the Enemy class.
"""

class Enemy(ABC):
    """
    A class representing an enemy in the game.

    Attributes:
        name (str): The name of the enemy.
        health (int): The health of the enemy.
    """

    def __init__(self, name="Enemy", health=50):
        self._name = name
        self._health = health
        
    @property
    def name(self):
        """
        str: The name of the enemy.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("The name must be a string.")

    def __str__(self):
        """
        Returns the string representation of the enemy.

        Returns:
            str: The string representation of the enemy.
        """
        return f"{self._name} has {self._health} health."
    
    def __repr__(self):
        """
        Returns the string representation of the enemy.

        Returns:
            str: The string representation of the enemy.
        """
        return f"{self._name} has {self._health} health."

    @abstractmethod
    def attack(self, player: rpg.player.Player, damage):
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
<<<<<<< HEAD
        pass
        # print(f"🧟🗡️ {self.name} attacks {player.name}!")
        # player.take_damage(damage)
    @abstractmethod
=======
        print(f"🧟🗡️ {self._name} attacks {player.name}!")
        player.take_damage(damage)

>>>>>>> bf824ab27f088bf3d249d3a6d9767ed2b97de424
    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
<<<<<<< HEAD
        pass
        # self.health -= damage
        # if self.health <= 0:
        #     print(f"🧟💀 {self.name} has been defeated!")
        # else:
        #     print(f"🧟💜 {self.name} has {self.health} health left.")
    @classmethod
    def create_enemies(cls):
        #cls is the same thing as calling the class -> Enemy("Goblin")
        """_summary_
        """
        return [cls("Goblin"),cls("Vampire")]
=======
        self._health -= damage
        if self._health <= 0:
            print(f"🧟💀 {self._name} has been defeated!")
        else:
            print(f"🧟💜 {self._name} has {self._health} health left.")

>>>>>>> bf824ab27f088bf3d249d3a6d9767ed2b97de424

class Skeleton(Enemy):
    """
    A class representing a skeleton enemy in the game. All skeletons have a shield power. The health of a skeleton is 50.
    
    Attributes:
        shield_power (int): The power of the skeleton's shield.
    """

    def __init__(self, shield_power, name="Skeleton"):
        super().__init__(name=name, health=50)
        self._shield_power = shield_power
        
    def attack(self, player: rpg.player.Player, damage):
        pass  
    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
        super().take_damage(damage - self._shield_power)
        
    # def terrify(self,player):
    #     player.Attack
        
class Dragon(Enemy):
    """
    A class representing a dragon enemy in the game. All dragons have a fire breath power. The health of a dragon is 200.
    
    Attributes:
        fire_breath_power (int): The power of the dragon's fire breath.
    """

    def __init__(self, fire_breath_power, name="Dragon"):
        super().__init__(name=name, health=80)
        self._fire_breath_power = fire_breath_power

    def attack(self, player: rpg.player.Player, damage):
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
        super().attack(player, damage + self._fire_breath_power)
    def use_tail_whip(player):
        pass
        
if __name__ == "__main__":
    print("Creating an enemy:")
    # enemy = Enemy()
    skeleton = Skeleton()
    # enemy.attack(rpg.player.Player(), 10)