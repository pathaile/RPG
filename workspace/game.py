from player import Player
from enemy import Enemy
from item import Item
from weapon import Weapon
from armor import Armor
from quest import Quest
from npc import NPC

class Game:
    def __init__(self):
        self.player = Player()
        self.enemies = []
        self.items = []
        self.weapons = []
        self.armor = []
        self.quests = []
        self.npcs = []

    def start(self):
        print("Welcome to the RPG game!")
        self.create_world()
        self.play()

    def create_world(self):
        # Create enemies
        self.enemies.append(Enemy("Goblin", 10, 2))
        self.enemies.append(Enemy("Orc", 20, 5))
        self.enemies.append(Enemy("Dragon", 50, 10))

        # Create items
        self.items.append(Item("Health Potion", "Restores 20 health", 20))
        self.items.append(Item("Mana Potion", "Restores 20 mana", 20))

        # Create weapons
        self.weapons.append(Weapon("Sword", "A basic sword", 5))
        self.weapons.append(Weapon("Axe", "A basic axe", 7))

        # Create armor
        self.armor.append(Armor("Leather Armor", "Basic leather armor", 2))
        self.armor.append(Armor("Chainmail Armor", "Basic chainmail armor", 5))

        # Create quests
        self.quests.append(Quest("Save the Princess", "Rescue the princess from the evil sorcerer", 100))

        # Create NPCs
        self.npcs.append(NPC("King", "The king of the land", [self.quests[0]]))

    def play(self):
        while True:
            print("What would you like to do?")
            print("1. Move")
            print("2. Attack")
            print("3. Defend")
            print("4. Use Item")
            print("5. Equip Weapon")
            print("6. Equip Armor")
            print("7. Complete Quest")
            print("8. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.player.move()
            elif choice == "2":
                self.player.attack(self.enemies)
            elif choice == "3":
                self.player.defend()
            elif choice == "4":
                self.player.use_item(self.items)
            elif choice == "5":
                self.player.equip_weapon(self.weapons)
            elif choice == "6":
                self.player.equip_armor(self.armor)
            elif choice == "7":
                self.player.complete_quest(self.quests)
            elif choice == "8":
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please try again.")
