import random


class Weapon:
    def __init__(self, name, damage):
        """
        This method initializes the attributes of the Weapon class.

        Args:
        name (str): Name of the weapon.
        damage (int): Amount of damage the weapon can inflict.
        """
        self.name = name
        self.damage = damage


class Armor:
    def __init__(self, name, defense):
        """
        This method initializes the attributes of the Armor class.

        Args:
        name (str): Name of the armor.
        defense (int): Defense value of the armor.
        """
        self.name = name
        self.defense = defense


class Gladiator:
    def __init__(self, name, weapon, armor, strength, luck):
        """
        This method initializes the attributes of the Gladiator class.

        Args:
        name (str): Name of the gladiator.
        weapon (Weapon): Weapon instance that the gladiator will use.
        armor (Armor): Armor instance that the gladiator will wear.
        strength (float): Strength of the gladiator, affecting the damage they deal in battle.
        luck (float): Luck of the gladiator, randomly affecting their attack and defense power.

        Note: Health, a class attribute, will also need to be initialized to 100.
        """
        self.name = name
        self.weapon = weapon
        self.armor = armor
        self.strength = strength
        self.luck = luck
        self.health = 100

    def attack(self):
        """
        This method calculates the damage dealt by the Gladiator when attacking.

        It considers both the Gladiator's strength and luck, the latter being randomly
        factored in each time the method is called.

        Returns:
        float: The amount of damage dealt by the Gladiator.
        """
        return float(self.weapon.damage * self.strength * random.uniform(1, 1 + self.luck))

    def defend(self, damage):
        """
        This method processes the damage received by the Gladiator when being attacked.

        It considers the Gladiator's Armor defense and luck, the latter being randomly
        factored in each time the method is called. The damage is subtracted from the Gladiator's health.

        Args:
        damage (float): The amount of damage to be defended against.
        """
        total_damage = damage - self.armor.defense * random.uniform(1, 1 + self.luck)
        if total_damage > 0:
            self.health -= total_damage


class Arena:
    def __init__(self, gladiator1, gladiator2):
        """
        This method initializes the attributes of the Arena class.

        Args:
        gladiator1 (Gladiator): The first gladiator in the arena.
        gladiator2 (Gladiator): The second gladiator in the arena.
        """
        self.gladiator1 = gladiator1
        self.gladiator2 = gladiator2

    def fight(self):
        """
        This method initiates a turn-based fight between the two Gladiators in the Arena.

        The Gladiators take turns attacking each other until one of them has no more health points
        (i.e., their `health` reaches 0 or below). The method prints out a message for each attack,
        showing who attacked whom and how much damage was dealt. Once a Gladiator's health points
        reach 0 or less, the fight ends, and the method prints out the name of the winner.
        """
        while True:
            damage1 = self.gladiator1.attack()
            self.gladiator2.defend(damage1)
            print("%s attacked %s and the damage was %f" % (self.gladiator1.name, self.gladiator2.name, damage1))
            damage2 = self.gladiator2.attack()
            self.gladiator1.defend(damage2)
            print("%s attacked %s and the damage was %f" % (self.gladiator2.name, self.gladiator1.name, damage2))

            if self.gladiator1.health < 0 and self.gladiator2.health < 0:
                if self.gladiator1.health < self.gladiator2.health:
                    print("%s won" % self.gladiator2.name)
                    break
                else:
                    print("%s won" % self.gladiator1.name)
                    break
            elif self.gladiator1.health < 0:
                print("%s won" % self.gladiator2.name)
                break
            elif self.gladiator2.health < 0:
                print("%s won" % self.gladiator1.name)
                break



def main():
    # 1.1 - Prepare your Armory
    pugio = Weapon("pugio", 2)
    spatha = Weapon("spatha", 10)
    fascina = Weapon("fascina", 12)

    # 1.2 - Prepare the armors
    cuirass = Armor("cuirass", 5)
    helmet = Armor("helmet", 2)

    # 2.1 Declare the gladiators
    spartacus = Gladiator("spartacus", spatha, cuirass, 1.5, 0.2)
    flamma = Gladiator("flamma", spatha, helmet, 1.6, 0.1)
    attilius = Gladiator("attilius", pugio, helmet, 1.1, 0.5)

    # 3. Time to fight in the arena
    colliseum = Arena(spartacus, flamma)
    colliseum.fight()


main()
