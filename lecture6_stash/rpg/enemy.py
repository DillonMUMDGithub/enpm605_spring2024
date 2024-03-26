
class Enemy:

    def __init__(self, name="Enemy", health=50):
        self._name = name
        self._health = health

    @property
    def name(self):
        return self._name
    @property
    def health(self):
        return self.health
    @name.getter
    def _get_name(self):
        return self._name
    
    
    @health.getter
    def _get_health(self):
        return self._health
    
    @name.setter
    def _set_name(self, name):
        raise AttributeError("cannot change an ememies name")  
    #    if isinstance(name,str):
    #        self._name = name
    #    else:
    #        raise TypeError("Name must be a string")  
    @name.deleter
    def _del_name(self):
        del self.name
    #do not provide for user
    # @healt.setter
    # def set_health(self, health):
    #    if isinstance(health,int):
    #        self._health = health
    #    else:
    #        raise TypeError("Health must be an integer")     

    def __str__(self):
        return f"{self.name} has {self.health} health."


    def attack(self, player, damage):
        """
        Attack the player.

        Args:
            player (Player): The player to attack.
            damage (int): The amount of damage to deal.
        """
        print(f"🧟🗡️ {self.name} attacks {player.name}!")
        player.take_damage(damage)

    def take_damage(self, damage):
        """
        Take damage from the player.

        Args:
            damage (int): The amount of damage to take.
        """
        self.health -= damage
        if self.health <= 0:
            print(f"🧟💀 {self.name} has been defeated!")
        else:
            print(f"🧟💜 {self.name} has {self.health} health left.")
            
    # name = property(fget=_get_name,fset=_set_name,fdel = _del_name,doc="The name of the enemy")
    # health = property(fget=_get_health,doc = "The health of the enemy")
