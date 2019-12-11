"""
Mrcoulrophobia 2019
....................../´¯/)
....................,/¯../
.................../..../
............./´¯/'...'/´¯¯`·¸
........../'/.../..../......./¨¯\
........('(...´...´.... ¯~/'...')
.........\.................'...../
..........''...\.......... _.·´
............\..............(
..............\.............\...
"""
import cmd
import textwrap
import sys
import os
import time
from random import randint
from random import randrange
screen_width = 100
### PLAYER AND BAD GUY SETUP ###
class Player:
    def __init__(self):
        self.name = ""
        self.maxhp = 100
        self.maxmp = 100
        self.level = 1
        self.xp = 0
        self.hp = 100
        self.mana = randint(19,23)
        self.mp = 100
        self.special = self.mana * 2
        self.location = "Home"
        self.gameover = False
        self.player_gold = 25
        self.player_wep = "+1 sword"
        self.player_armor = "light armor"
        self.player_potions = []
        self.player_kills = 1
        self.player_kills2 = 1
        self.player_kills3 = 1
        self.player_kills4 = 1
        self.player_kills5 = 1
        self.plasyer_kills6 = 1
myPlayer = Player()
class Goblins:
    def __init__(self):
        self.name="Goblin"
        self.hp=50
        self.dmg=randint(10,14)
myGoblin = Goblins()
myGoblin2 = Goblins()
myGoblin3 = Goblins()
class Ogre:
    def __init__(self):
        self.name="Ogre"
        self.hp=250
        self.dmg=randint(22,26)
myOgre = Ogre()
class Giant_Spider:
    def __init__(self):
        self.name="Giant Spider"
        self.hp = 150
        self.dmg = randint(18,21)
mySpider = Giant_Spider()
mySpider2 = Giant_Spider()
mySpider3 = Giant_Spider()
mySpider4 = Giant_Spider()
class Lake_Monster:
    def __init__(self):
        self.name="Lake Monster"
        self.hp = 500
        self.dmg = randint(35,37)
myLakeMonster = Lake_Monster()
class Imp:
    def __init__(self):
        self.name="Imp"
        self.hp = 150
        self.dmg=randint(20,24)
myImp = Imp()
myImp2 = Imp()
myImp3 = Imp()
myImp4 = Imp()
myImp5 = Imp()
myImp6 = Imp()
class Wraith:
    def __init__(self):
        self.name="Wrait"
        self.hp=250
        self.dmg=randint(25,28)
myWraith = Wraith()
myWraith2 = Wraith()
myWraith3 = Wraith()
class Demon:
    def __init__(self):
        self.name="Demon"
        self.hp=1000
        self.dmg=randint(55,60)
myDemon = Demon()
#### TITLE SCREEN ###

def title_screen_selections():
    option = input("> ")
    if option.lower() == "play":
        setup_game() 
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ["play", "help", "quit"]:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == "play":
            setup_game() 
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()
def title_screen():
    os.system("clear")
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("Welcome to the Tyler's text based open world rpg!")
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("               -Play-                 ")
    print("               -Help-                 ")
    print("               -Quit-                 ")
    title_screen_selections()
def help_menu():
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("Help menu options: 'General Help', 'Battle Help', 'Storyline Tips', 'Quit Menu'")
    which_help = input("> ")
    if which_help.lower() == "general help" or which_help.lower() == "general":
        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print("Use up, down, left, right or north, south, east, west to move.")
        print("Type your commands to do them.")
        print("Use examine to interact with shops, locations, or to find clues.")
        print("You can purchase new items from various vendors in town when you obtain enough gold that will help you in your adventure.")
        print("You can display the zone map by using the map command.")
        print("You gain gold, items, and levels by defeating monsters.")
        print("If you die, the game is over.")
    elif which_help.lower() == 'battle help' or which_help.lower() == "battle":
        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print("Use your health potions as often as possible to stay alive! Remember, you have unlimited health potions.")
        print("Using your special attack results in doing double damage, at the cost of you MP.")
        print("MP is restored by using the rest command after battle, using MP potions, and by leveling.")
    elif which_help.lower() == "storyline tips" or which_help.lower() == "storyline":
        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print("You've heard rumors of a sinister evil stirring in the area.")
        print("Townspeople have been disappearing and many of the locals that are still around say the cave south west of town is responsible.")
        print("You fear there is a greater evil at hand than just what is to be found in the cave.")
        print("TIP: Start by making your way to the cave, and follow clues there-after to complete the main story.")
    print("Good luck and have fun!")
    title_screen()
    title_screen_selections()
def help_menu_started(action):
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("Help menu options: 'General Help', 'Battle Help', 'Storyline Tips', 'Quit Menu'")
    which_help = input("> ")
    if which_help.lower() == "general help" or which_help.lower() == "general":
        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print("Use up, down, left, right or north, south, east, west to move.")
        print("Type your commands to do them.")
        print("Use examine to interact with shops, locations, or to find clues.")
        print("You can purchase new items from various vendors in town when you obtain enough gold that will help you in your adventure.")
        print("You can display the zone map by using the map command.")
        print("You gain gold, items, and levels by defeating monsters.")
        print("If you die, the game is over.")
    elif which_help.lower() == 'battle help' or which_help.lower() == "battle":
        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print("Use your health potions as often as possible to stay alive! Remember, you have unlimited health potions.")
        print("Using your special attack results in doing double damage, at the cost of you MP.")
        print("MP is restored by using the rest command after battle, using MP potions, and by leveling.")
    elif which_help.lower() == "storyline tips" or which_help.lower() == "storyline":
        print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
        print("You've heard rumors of a sinister evil stirring in the area.")
        print("Townspeople have been disappearing and many of the locals that are still around say the cave south west of town is responsible.")
        print("You fear there is a greater evil at hand than just what is to be found in the cave.")
        print("TIP: Start by making your way to the cave, and follow clues there-after to complete the main story.")
    print("Good luck and have fun!")

###### MAP #######
ZONENAME = ""
DESCRIPTION = "description"
EXAMINATION = "examination"
SOLVED = False
UP = "up", "north"
DOWN = "down", "south"
LEFT = "left", "west"
RIGHT = "right", "east"
solved_places = {
        'Wall Top':False,'Wall Top 2':False, 'Wall Top 3':False, 'Wall Top 4':False,
        'Wall Left':False,'Town BlackSmith':False,'Town Entrance':False,'Town Potions Master':False,'Town Misc Vendor':False,'Wall Right':False,
        'Wall Left 2':False,'Forest Edge':False,'Home':False,'Forest Edge 2':False,'Lake':False,'Wall Right 2':False,
        'Wall Left 3':False,'Cave Entrance':False,'Deep Forest':False,'Deep Forest 2':False,'River':False,'Wall Right 3':False,
        'Wall Left 4':False,'Cave Tunnel':False,'Cave End':False,'Desert Entrance':False,'River 2':False,'Wall Right 4':False,
        'Wall Bottom':False,'Wall Bottom 2':False,'Wall Bottom 3':False,'Wall Bottom 4':False
                 }
def print_map(action):
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print("__________|____Wall Top___|___Wall Top2___|____Wall Top3______|____Wall Top4___|___________")
    print("Wall Left_|Town BlackSmith|_Town Entrance_|Town Potions Master|Town Misc Vendor|Wall Right ")
    print("Wall Left2|__Forest Edge__|______Home_____|____Forest Edge2___|______Lake______|Wall Right2")
    print("Wall Left3|_Cave Entrance_|__Deep Forest__|____Deep Forest2___|_____River______|Wall Right3")
    print("Wall Left4|__Cave Tunnel__|___Cave End____|__Desert Entrance__|____River2______|Wall Right4")
    print("__________|__Wall Bottom__|_Wall Bottom2__|____Wall Bottom3___|__Wall Bottom4__|___________")
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")

zone_map = {
    'Wall Top':{
            ZONENAME:'Wall Top',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Top',
            DOWN:'Town BlackSmith',
            LEFT:'Wall Left',
            RIGHT:'Wall Top 2'
            },
    'Wall Top 2':{
            ZONENAME:'Wall Top 2',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Top 2',
            DOWN:'Town Entrance',
            LEFT:'Wall Top',
            RIGHT:'Wall Top 3'
            },
    'Wall Top 3':{
            ZONENAME:'Wall Top 3',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Top 3',
            DOWN:'Town Potions Master',
            LEFT:'Wall Top 2',
            RIGHT:'Wall Top 4'
            },
    'Wall Top 4':{
            ZONENAME:'Wall Top 4',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Top 4',
            DOWN:'Town Misc Vendor',
            LEFT:'Wall Top 3',
            RIGHT:'Wall Top 4'
            },
    'Wall Left':{
            ZONENAME:'Wall Left',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Top',
            DOWN:'Wall Left 2',
            LEFT:'Wall Left',
            RIGHT:'Town BlackSmith'
            },
    'Town BlackSmith':{
            ZONENAME:"Town BlackSmith",
            DESCRIPTION:"This vendor sells weapons and armor.",
            EXAMINATION:"This should trigger an event allowing for the player to purchase things",
            SOLVED:False,
            UP:"Wall top",
            DOWN:"Forest Edge",
            LEFT:"Wall Left",
            RIGHT:"Town Entrance"
            },
    'Town Entrance':{
            ZONENAME:"Town Entrance",
            DESCRIPTION:"This is the entrance to the town. Going south leads to your home, north is blocked by a mystical barrier,\n east leads to the towns potion vendor and west leads to the towns blacksmith.",
            EXAMINATION:"Oddly enough, it seems to be pretty empty. Being that this is your home-town, this seems unusual.\n The cave south-west of here must have something to do with it.",
            SOLVED:False,
            UP:"Wall Top 2",
            DOWN:"Home",
            LEFT:"Town BlackSmith",
            RIGHT:"Town Potions Master"
            },
    'Town Potions Master':{
            ZONENAME:"Town Potions Master",
            DESCRIPTION:"This vendor sells potions to help you through your adventure",
            EXAMINATION:"This should trigger an event allowing for the player to purchase things",
            SOLVED:False,
            UP:"Wall Top 3",
            DOWN:"Forest Edge 2",
            LEFT:"Town Entrance",
            RIGHT:"Town Misc Vendor"
            },
    'Town Misc Vendor':{
            ZONENAME:"Town Misc Vendor",
            DESCRIPTION:"This is your vendor for odds and ends.",
            EXAMINATION:"This should trigger an event allowing for the player to purchase things",
            SOLVED:False,
            UP:"Wall Top 4",
            DOWN:"Lake",
            LEFT:"Town Potions Master",
            RIGHT:"Wall Right",
            },
    'Wall Right':{
            ZONENAME:'Wall Right',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Top 4',
            DOWN:'Wall Right 2',
            LEFT:'Town Misc Vendor',
            RIGHT:'Wall Right'
            },
    'Wall Left 2':{
            ZONENAME:'Wall Left 2',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Left',
            DOWN:'Wall Left 3',
            LEFT:'Wall Left 2',
            RIGHT:'Forest Edge'
            },
    'Forest Edge':{
            ZONENAME:"Forest Edge",
            DESCRIPTION:"Located west of your home it borders the town as well as your home.\n Going further west will result in encountering a mystical barrier that cannot be crossed.",
            EXAMINATION:"You see a mystic barrier preventing anyone from going further west.\n To the north you see the town, west you see your home, and south seems to have a cave entrance",
            SOLVED:False,
            UP:"Town BlackSmith",
            DOWN:"Cave Entrance",
            LEFT:"Forest Edge",
            RIGHT:"Deep Forest",
            },
    'Home':{
            ZONENAME:"Home",
            DESCRIPTION:"Your home is located just outside of town near the forest edge.\nYou have a beautiful small family home. \nNorth leads to the town entrance. \nAll other directions lead deeper into the forest.",
            EXAMINATION:"Your home looks the same as always, nice and cozy.",
            SOLVED:False,
            UP:"Town Entrance",
            DOWN:"Deep Forest",
            LEFT:"Forest Edge",
            RIGHT:"Forest Edge 2",
            },
    'Forest Edge 2':{
            ZONENAME:"Forest Edge 2",
            DESCRIPTION:"You see giant trees towering overhead and lush forest floor lie below your boots. \nYour home is directly west. \nThe town is directly north from here. \nSouth leads deeper into the forest. \nEast leads directly to the Lake.",
            EXAMINATION:"",
            SOLVED:False,
            UP:"Town Potions Master",
            DOWN:"Deep Forest 2",
            LEFT:"Home",
            RIGHT:"Lake"
            },
    'Lake':{
            ZONENAME:"Lake",
            DESCRIPTION:"You see a small, familiar, yet beautiful lake positioned perfectly in an opening between the trees. \nA river flows into the lake from the south.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Town Misc Vendor",
            DOWN:"River",
            LEFT:"Forest Edge 2",
            RIGHT:"Lake"
            },
    'Wall Right 2':{
            ZONENAME:'Wall Right 2',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Right',
            DOWN:'Wall Right 3',
            LEFT:'Lake',
            RIGHT:'Wall Right 2'
            },
    'Wall Left 3':{
            ZONENAME:'Wall Left 3',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Left 2',
            DOWN:'Wall Left 4',
            LEFT:'Wall Left 3',
            RIGHT:'Cave Entrance'
            },
    'Cave Entrance':{
            ZONENAME:"Cave Entrance",
            DESCRIPTION: "You see a large opening leading to what must be a cave. \nThis must be the cave causing disappearances from the town. \nYou see 3 goblins huddling around a fire. \nThey have not yet noticed you.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Forest Edge",
            DOWN:"Cave Tunnel",
            LEFT:"Cave Entrance",
            RIGHT:"Deep Forest"
            },
    'Deep Forest':{
            ZONENAME:"Deep Forest",
            DESCRIPTION:"You see giant trees towering overhead and lush forest floor lie below your boots. \nNorth leads to your home. \nWest of here seems to be the entrance to a cave. \nEast continues deeper into the forest.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Home",
            DOWN:"Deep Forest",
            LEFT:"Cave Entrance",
            RIGHT:"Deep Forest 2"
            },
    'Deep Forest 2':{
            ZONENAME:"Deep Forest 2",
            DESCRIPTION:"You see giant trees towering overhead and lush forest floor lie below your boots. \nSouth you can see the a break in the wildlife and what looks like sand. \nEast you can see a river flowing from south to north.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Forest Edge 2",
            DOWN:"Desert Entrance",
            LEFT:"Deep Forest",
            RIGHT:"River"
            },
    'River':{
            ZONENAME:"River",
            DESCRIPTION:"You see a river leading to a Lake (north) and continuing south. \nYou cannot see where the river begins as there are too many trees blocking your view.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Lake",
            DOWN:"River 2",
            LEFT:"Deep Forest 2",
            RIGHT:"River"
            },
    'Wall Right 3':{
            ZONENAME:'Wall Right 3',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Right 2',
            DOWN:'Wall Right 4',
            LEFT:'River',
            RIGHT:'Wall Right 3'
            },
    'Wall Left 4':{
            ZONENAME:'Wall Left 4',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Left 3',
            DOWN:'Wall Bottom',
            LEFT:'Wall Left 4',
            RIGHT:'Cave Tunnel'
            },
    'Cave Tunnel':{
            ZONENAME:"Cave Tunnel",
            DESCRIPTION:"You enter a narrow but seemingly long tunnel. \nTowards the end ('east') you see an opening where light is brightly shining. ",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Cave Entrance",
            DOWN:"Cave Tunnel",
            LEFT:"Cave Tunnel",
            RIGHT:"Cave End"
            },
    'Cave End':{
            ZONENAME:"Cave End",
            DESCRIPTION:"You see a giant opening where countless bodies and skeletons lay scattered through-out the room. \nIn the center of the room is a massive fire with a humanoid corpse roasting over-top. \nSitting in a giant stone-made throne near the fire is a giant Ogre. \nCages lining the walls hold the remains of a few unlucky humanoids the Ogre used or uses as food.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Cave End",
            DOWN:"Cave End",
            LEFT:"Cave Tunnel",
            RIGHT:"Cave End"
            },
    'Desert Entrance':{
            ZONENAME:"Desert Entrance",
            DESCRIPTION:"You see the start of what seems to be a desert area. The lush forest surrounding's quickly fade to rolling hills of sand with little to no signs of life.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"Deep Forest 2",
            DOWN:"Desert Entrance",
            LEFT:"Cave End",
            RIGHT:"River 2"
            },
    'River 2':{
            ZONENAME:"River 2",
            DESCRIPTION:"You see a river leading to a lake (north) and continuing south. There are too many trees to see where the river begins.",
            EXAMINATION:"examination",
            SOLVED:False,
            UP:"River",
            DOWN:"River 2",
            LEFT:"Desert Entrance",
            RIGHT:"River 2"
            },
    'Wall Right 4':{
            ZONENAME:'Wall Right 4',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Wall Right 3',
            DOWN:'Wall Bottom 4',
            LEFT:'River 2',
            RIGHT:'Wall Right 4'
            },
    'Wall Bottom':{
            ZONENAME:'Wall Bottom',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Cave Tunnel',
            DOWN:'Wall Bottom',
            LEFT:'Wall Left 4',
            RIGHT:'Wall Bottom 2'
            },
    'Wall Bottom 2':{
            ZONENAME:'Wall Bottom 2',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Cave Tunnel',
            DOWN:'Wall Bottom 2',
            LEFT:'Wall Bottom',
            RIGHT:'Wall Bottom 3'            
            },
    'Wall Bottom 3':{
            ZONENAME:'Wall Bottom 3',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'Desert Entrance',
            DOWN:'Wall Bottom 3',
            LEFT:'Wall Bottom 2',
            RIGHT:'Wall Bottom 4'            
            },
    'Wall Bottom 4':{
            ZONENAME:'Wall Bottom 4',
            DESCRIPTION:'YOU SHALL NOT PASS',
            EXAMINATION:'YOU REALLY CANT GO FURTHER IN THIS DIRECTION',
            SOLVED:False,
            UP:'River 2',
            DOWN:'Wall Bottom 4',
            LEFT:'Wall Bottom 3',
            RIGHT:'Wall Bottom 4'            
            }
        }
        
   
######## GAME INTERACTIVITY ###############
def level_up():
    myPlayer.level += 1
    myPlayer.maxhp = myPlayer.maxhp + 50
    myPlayer.maxmp = myPlayer.maxmp + 50
    myPlayer.hp = myPlayer.maxhp
    myPlayer.mp = myPlayer.maxmp
    myPlayer.mana = myPlayer.mana + 4
    if myGoblin3.hp <= 0:
        myPlayer.player_kills += 1
    if myOgre.hp <= 0:
        myPlayer.player_kills2 += 1
def print_stats(action):
    print("Max HP: ")
    print(myPlayer.maxhp)
    print("Current HP: ")
    print(myPlayer.hp)
    print("Max MP: ")
    print(myPlayer.maxmp)
    print("Current MP: ")
    print(myPlayer.mp)
    print("Level: ")
    print(myPlayer.level)
    print("XP: ")
    print(myPlayer.xp)
    print("Damage: ")
    print(myPlayer.mana)
def print_inventory(action):
    print("Gold: ")
    print(myPlayer.player_gold)
    print("Weapon: ")
    print(myPlayer.player_wep)
    print("Armor: ")
    print(myPlayer.player_armor)
    print("Potions: ")
    print("HP potions: ")
    print("Unlimited")
    print("Other potions: ")
    print(myPlayer.player_potions)
def print_location():
    print("\n" + ("#"* (4 + len(myPlayer.location))))
    print("# " + myPlayer.location + " #")
    print("# " + zone_map[myPlayer.location][DESCRIPTION] + " #")
    print("\n" + ("#" * (4 + len(myPlayer.location))))
def prompt():
    if myPlayer.hp > 0:
        acceptable_actions = ["move", "examine", "quit", "map", "check inventory", "check stats", "help"]
        if myPlayer.level != 1:
            zone_map['Cave Entrance'][DESCRIPTION] = "The remains of the goblins you defeated earlier seem to have disappeared. \nEverything else remains oddly the same."
        if myPlayer.level != 2:
            zone_map['Cave End'][DESCRIPTION] = "The remains of the Ogre seem to have disappeared while the countless humanoid corpses still litter the cave floor."
        if myPlayer.location == "Cave Entrance":
            acceptable_actions.append("attack")
            acceptable_actions.append("special attack")
            if "dmg potion" in myPlayer.player_potions:
                if myGoblin.hp > 0:
                    acceptable_actions.append("dmg potion")
                elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                    acceptable_actions.append("dmg potion")
                elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                    acceptable_actions.append("dmg potion")
            if "dmg potion 2" in myPlayer.player_potions:
                if myGoblin.hp > 0:
                    acceptable_actions.append("dmg potion 2")
                elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                    acceptable_actions.append("dmg potion 2")
                elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                    acceptable_actions.append("dmg potion 2")
            if "dmg potion 3" in myPlayer.player_potions:
                if myGoblin.hp > 0:
                    acceptable_actions.append("dmg potion 3")
                elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                    acceptable_actions.append("dmg potion 3")
                elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                    acceptable_actions.append("dmg potion 3")
            if "max dmg potion" in myPlayer.player_potions:
                if myGoblin.hp > 0:
                    acceptable_actions.append("max dmg potion")
                elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                    acceptable_actions.append("max dmg potion")
                elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                    acceptable_actions.append("max dmg potion")
            if "max dmg potion 2" in myPlayer.player_potions:
                if myGoblin.hp > 0:
                    acceptable_actions.append("max dmg potion 2")
                elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                    acceptable_actions.append("max dmg potion 2")
                elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                    acceptable_actions.append("max dmg potion 2")
            if "max dmg potion 3" in myPlayer.player_potions:
                if myGoblin.hp > 0:
                    acceptable_actions.append("max dmg potion 3")
                elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                    acceptable_actions.append("max dmg potion 3")
                elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                    acceptable_actions.append("max dmg potion 3")
            if "mp potion" in myPlayer.player_potions and myPlayer.level == 1 and myPlayer.mp <= 50:
                acceptable_actions.append("mp potion")
            if "mp potion" in myPlayer.player_potions and myPlayer.level == 2 and myPlayer.mp <= 100:
                acceptable_actions.append("mp potion")
            if "mp potion" in myPlayer.player_potions and myPlayer.level == 3 and myPlayer.mp <= 150:
                acceptable_actions.append("mp potion")
            if "mp potion 2" in myPlayer.player_potions and myPlayer.level == 1 and myPlayer.mp <= 50:
                acceptable_actions.append("mp potion 2")
            if "mp potion 2" in myPlayer.player_potions and myPlayer.level == 2 and myPlayer.mp <= 100:
                acceptable_actions.append("mp potion 2")
            if "mp potion 2" in myPlayer.player_potions and myPlayer.level == 3 and myPlayer.mp <= 150:
                acceptable_actions.append("mp potion 2")
            if "mp potion 3" in myPlayer.player_potions and myPlayer.level == 1 and myPlayer.mp <= 50:
                acceptable_actions.append("mp potion 3")
            if "mp potion 3" in myPlayer.player_potions and myPlayer.level == 2 and myPlayer.mp <= 100:
                acceptable_actions.append("mp potion 3")
            if "mp potion 3" in myPlayer.player_potions and myPlayer.level == 3 and myPlayer.mp <= 150:
                acceptable_actions.append("mp potion 3")
            if myGoblin.hp > 0 or myGoblin2.hp > 0 or myGoblin3.hp > 0:
                acceptable_actions.remove("move")
            if myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0 and myPlayer.player_kills == 1:
                acceptable_actions.remove("attack")
                acceptable_actions.remove("special attack")
                level_up()
                myPlayer.player_gold += 25
                if myPlayer.player_wep == "+1 sword":
                    myPlayer.mana = myPlayer.mana + 2
                    myPlayer.player_wep = "+3 Sword"
                    print("You have looted and equipped a +3 sword!")
                print("You have defeated the group of goblins!")
                print("Congratulations! Your character has leveled!")
                print("25 gold has been added to your bag")
        if myPlayer.location == "Cave End":
            acceptable_actions.append("boss fight")
            acceptable_actions.append("boss fight special")
            if "dmg potion" in myPlayer.player_potions and myOgre.hp > 0:
                acceptable_actions.append("dmg potion")
            if "dmg potion 2" in myPlayer.player_potions and myOgre.hp > 0:
                acceptable_actions.append("dmg potion 2")
            if "dmg potion 3" in myPlayer.player_potions and myOgre.hp > 0:
                acceptable_actions.append("dmg potion 3")
            if "max dmg potion" in myPlayer.player_potions and myOgre.hp > 0:
                acceptable_actions.append("max dmg potion")
            if "max dmg potion 2" in myPlayer.player_potions and myOgre.hp > 0:
                acceptable_actions.append("max dmg potion 2")
            if "max dmg potion 3" in myPlayer.player_potions and myOgre.hp > 0:
                acceptable_actions.append("max dmg potion 3")
            if "mp potion" in myPlayer.player_potions and myPlayer.level == 1 and myPlayer.mp <= 50:
                acceptable_actions.append("mp potion")
            if "mp potion" in myPlayer.player_potions and myPlayer.level == 2 and myPlayer.mp <= 100:
                acceptable_actions.append("mp potion")
            if "mp potion" in myPlayer.player_potions and myPlayer.level == 3 and myPlayer.mp <= 150:
                acceptable_actions.append("mp potion")
            if "mp potion 2" in myPlayer.player_potions and myPlayer.level == 1 and myPlayer.mp <= 50:
                acceptable_actions.append("mp potion 2")
            if "mp potion 2" in myPlayer.player_potions and myPlayer.level == 2 and myPlayer.mp <= 100:
                acceptable_actions.append("mp potion 2")
            if "mp potion 2" in myPlayer.player_potions and myPlayer.level == 3 and myPlayer.mp <= 150:
                acceptable_actions.append("mp potion 2")
            if "mp potion 3" in myPlayer.player_potions and myPlayer.level == 1 and myPlayer.mp <= 50:
                acceptable_actions.append("mp potion 3")
            if "mp potion 3" in myPlayer.player_potions and myPlayer.level == 2 and myPlayer.mp <= 100:
                acceptable_actions.append("mp potion 3")
            if "mp potion 3" in myPlayer.player_potions and myPlayer.level == 3 and myPlayer.mp <= 150:
                acceptable_actions.append("mp potion 3")
            if myOgre.hp > 0:
                acceptable_actions.remove("move")
            if myPlayer.mp <= 25:
                acceptable_actions.remove("boss fight special")
            if myOgre.hp <= 0 and "boss fight special" in acceptable_actions:
                acceptable_actions.remove("boss fight")
                acceptable_actions.remove("boss fight special")
            if myOgre.hp <= 0 and not "boss fight special" in acceptable_actions and "boss fight" in acceptable_actions:
                acceptable_actions.remove("boss fight")
            if myOgre.hp <= 0 and myPlayer.player_kills2 == 1:
                level_up()
                myPlayer.player_gold += 150
                print("You have defeated the might Ogre!")
                print("Congratulations! Your character has leveled!")
                print("150 gold has been added to your bag")
        if myPlayer.level == 1 and myPlayer.hp <= 50:
            acceptable_actions.append("health potion")
        if myPlayer.level == 2 and myPlayer.hp <= 75:
            acceptable_actions.append("health potion")
        if myPlayer.hp <= 75 and not myPlayer.location == "Cave Entrance" and not myPlayer.location == "Cave End" and myPlayer.hp <= 75:
            acceptable_actions.append("rest")
########### ACTIONS #############
        print("\n" + "==============================")
        print("What would you like to do?\n" + "Choose from the following options: ")
        for char in acceptable_actions:
            sys.stdout.write(char + "\n")
            sys.stdout.flush()
            time.sleep(0.01)
        action = input("> ")
        while action.lower() not in acceptable_actions:
            print("Unknown action, try again\n")
            action = input("> ")
        if action.lower() == "quit":
            sys.exit()
        elif action.lower() in ["move"]:
            player_move(action.lower())
        elif  action.lower() in ["examine"]:
            player_examine(action.lower())
        elif action.lower() in ["attack"]:
            player_fight(action.lower())
        elif action.lower() == "special attack":
            player_special(action.lower())
        elif action.lower() == "boss fight":
            boss_fight(action.lower())
        elif action.lower() == "boss fight special":
            boss_fight_special(action.lower())
        elif action.lower() == "map":
            print_map(action.lower())
        elif action.lower() == "check inventory":
            print_inventory(action.lower())
        elif action.lower() == "check stats":
            print_stats(action.lower())
        elif action.lower() == "help":
            help_menu_started(action.lower())
        elif action.lower() == "dmg potion":
            myPlayer.player_potions.remove("dmg potion")
            acceptable_actions.remove("dmg potion")
            print("You deal 50 points of damage to your target!")
            if myGoblin.hp > 0:
                myGoblin.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                myGoblin2.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                myGoblin3.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myOgre.hp > 0 and myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
                myOgre.hp -= 50
                print("Ogre's HP: ")
                print(myOgre.hp)
        elif action.lower() == "dmg potion 2":
            print("You deal 50 points of damage to your target!")
            myPlayer.player_potions.remove("dmg potion 2")
            acceptable_actions.remove("dmg potion 2")
            if myGoblin.hp > 0:
                myGoblin.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                myGoblin2.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                myGoblin3.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myOgre.hp > 0 and myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
                myOgre.hp -= 50
                print("Ogre's HP: ")
                print(myOgre.hp)
        elif action.lower() == "dmg potion 3":
            myPlayer.player_potions.remove("dmg potion 3")
            acceptable_actions.remove("dmg potion 3")
            print("You deal 50 points of damage to your target!")
            if myGoblin.hp > 0:
                myGoblin.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                myGoblin2.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                myGoblin3.hp -= 50
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myOgre.hp > 0 and myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
                myOgre.hp -= 50
                print("Ogre's HP: ")
                print(myOgre.hp)
        elif action.lower() == "max dmg potion":
            print("You deal 200 points of damage to your target!")
            myPlayer.player_potions.remove("max dmg potion")
            acceptable_actions.remove("max dmg potion")
            if myGoblin.hp > 0:
                myGoblin.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                myGoblin2.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                myGoblin3.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myOgre.hp > 0 and myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
                myOgre.hp -= 200
                print("Ogre's HP: ")
                print(myOgre.hp)
        elif action.lower() == "max dmg potion 2":
            print("You deal 200 points of damage to your target!")
            myPlayer.player_potions.remove("max dmg potion 2")
            acceptable_actions.remove("max dmg potion 2")
            if myGoblin.hp > 0:
                myGoblin.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                myGoblin2.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                myGoblin3.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myOgre.hp > 0 and myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
                myOgre.hp -= 200
                print("Ogre's HP: ")
                print(myOgre.hp)
        elif action.lower == "max dmg potion 3":
            print("You deal 200 points of damage to your target!")
            myPlayer.player_potions.remove("max dmg potion 3")
            acceptable_actions.remove("max dmg potion 3")
            if myGoblin.hp > 0:
                myGoblin.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp > 0:
                myGoblin2.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp > 0:
                myGoblin3.hp -= 200
                print("Goblin's HP: ")
                print(myGoblin.hp)
                print(myGoblin2.hp)
                print(myGoblin3.hp)
            elif myOgre.hp > 0 and myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
                myOgre.hp -= 200
                print("Ogre's HP: ")
                print(myOgre.hp)
        elif action.lower() == "mp potion":
            print("You have restored 50 mp!")
            myPlayer.mp += 50
            print("Current MP: ")
            print(myPlayer.mp)
            myPlayer.player_potions.remove("mp potion")
            acceptable_actions.remove("mp potion")
        elif action.lower() == "mp potion 2":
            print("You have restored 50 mp!")
            myPlayer.mp += 50
            print("Current MP: ")
            print(myPlayer.mp)
            myPlayer.player_potions.remove("mp potion 2")
            acceptable_actions.remove("mp potion 2")
        elif action.lower() == "mp potion 3":
            print("You have restored 50 mp!")
            myPlayer.mp += 50
            print("Current MP: ")
            print(myPlayer.mp)
            myPlayer.player_potions.remove("mp potion 3")
            acceptable_actions.remove("mp potion 3")
        elif action.lower() == "max mp potion":
            print("Your mp has been restored to full!")
            myPlayer.mp = myPlayer.maxmp
            print("Current MP:")
            print(myPlayer.mp)
            myPlayer.player_potions.remove("max mp potion")
            acceptable_actions.remove("max mp potion")
        elif action.lower() == "max mp potion 2":
            print("Your mp has been restored to full!")
            myPlayer.mp = myPlayer.maxmp
            print("Current MP:")
            print(myPlayer.mp)
            myPlayer.player_potions.remove("max mp potion 2")
            acceptable_actions.remove("max mp potion 2")
        elif action.lower() == "max mp potion 3":
            print("Your mp has been restored to full!")
            myPlayer.mp = myPlayer.maxmp
            print("Current MP:")
            print(myPlayer.mp)
            myPlayer.player_potions.remove("max mp potion 3")
            acceptable_actions.remove("max mp potion 3")
        if action.lower() == "rest":
            print("You rest, restoring your HP and MP to full")
            myPlayer.hp = myPlayer.maxhp
            myPlayer.mp = myPlayer.maxmp
            print("Your HP:")
            print(myPlayer.hp)
            print("Your MP:")
            print(myPlayer.mp)
        if action.lower() == "health potion":
            print("You drink a health potion, restoring up to 25 hp!")
            if myPlayer.hp <= 75:
                myPlayer.hp += 25
                print("Your HP:")
                print(myPlayer.hp)
            else:
                myPlayer.hp = myPlayer.maxhp
                print("Your HP:")
                print(myPlayer.hp)
    else:
        print("You have died!")
        myPlayer.gameover = True
def player_move(myAction):
    ask = "Would you like to move North, South, East, or West?\n"
    dest = input(ask)
    if dest in ["up", "north"]:
        destination = zone_map[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ["left", "west"]:
        destination = zone_map[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ["right", "east"]:
        destination = zone_map[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ["down", "south"]:
        destination = zone_map[myPlayer.location][DOWN]
        movement_handler(destination)
    else:
        print("Invalid input please try another command")
        player_move(myAction)
def movement_handler(destination):
    print("You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()
########## EXAMINE #####################
def player_examine(action):
    if myPlayer.location == "Town Potions Master":
        print("The Town Potions Master offers a variety of potions, for a price. \nWould you like to view his inventory? \nEnter yes or no.")
        tps_action = input("> ")
        if tps_action.lower() == "yes":
            tps_inventory = ["mp potion", "max mp potion", "dmg potion", "max dmg potion", "exit shop"]
            print(tps_inventory)
            print("mp potions cost 50 gold each, \nmax mp potions cost 150 gold each, \ndmg potions cost 75 gold each and deal 50 damage to your targe, \nmax dmg potions cost 200 gold each and deal 200 damge to your targe")
            print("Enter the name of the item you would like to buy")
            tps_purchase = input("> ")
            if tps_purchase == "mp potion" and myPlayer.player_gold >= 50:
                print("Great! You can purchase and hold up to 3 potions of each type, how many would you like?")
                tps_amount1 = input("> ")
                if tps_amount1 == "one" or tps_amount1 == "1":
                    if "mp potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("mp potion")
                        print("You have purchased 1 mp potion!")
                        myPlayer.player_gold -= 50
                    elif "mp potion" in myPlayer.player_potions and "mp potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("mp potion 2")
                        print("You have purchased 1 mp potion!")
                        myPlayer.player_gold -= 50
                    elif "mp potion" in myPlayer.player_potions and "mp potion 2" in myPlayer.player_potions and "mp potion 3" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("mp potion 3")
                        print("You have purchased 1 mp potion!")
                        myPlayer.player_gold -= 50
                    elif "mp potion" in myPlayer.player_potions and "mp potion 3" in myPlayer.player_potions and "mp potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("mp potion 2")
                        myPlayer.player_gold -= 50
                        print("You have purchased 1 mp potion!")
                    elif "mp potion 2" in myPlayer.player_potions and "mp potion 3" in myPlayer.player_potions and "mp potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("mp potion")
                        myPlayer.player_gold -= 50
                        print("You have purchased 1 mp potion!")
                    elif "mp potion" in myPlayer.player_potions and "mp potion 2" in myPlayer.player_potions and "mp potion 3" in myPlayer.player_potions:
                        print("You cannot purchase anymore mp potions.")
                elif tps_amount1 == "one" or tps_amount1 == "1" and myPlayer.player_gold < 50:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount1 == "two" or tps_amount1 == "2" and myPlayer.player_gold >= 100:
                    if "mp potion" not in myPlayer.player_potions and "mp potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("mp potion")
                        myPlayer.player_potions.append("mp potion 2")
                        print("You have purchased 2 mp potions!")
                        myPlayer.player_gold -= 100
                    elif "mp potion" in myPlayer.player_potions and "mp potion 2" in myPlayer.player_potions or "mp potion" in myPlayer.player_potions and "mp potion 3" in myPlayer.player_potions or "mp potion 2" in myPlayer.player_potions and "mp potion 3" in myPlayer.player_potions: 
                        print("You are already carrying two potions, you can only purchase one more.")
                    elif "mp potion 2" not in myPlayer.player_potions and "mp potion 3" not in myPlayer.player_potions and "mp potion" in myPlayer.player_potions:
                        print("You have purchased 2 mp potions!")
                        myPlayer.player_gold -= 100
                        myPlayer.player_potions.append("mp potion 2")
                        myPlayer.player_potions.append("mp potion 3")
                    elif "mp potion" not in myPlayer.player_potions and "mp potion 3" not in myPlayer.player_potions and "mp potion 2" in myPlayer.player_potions:
                        print("You have purchased 2 mp potions!")
                        myPlayer.player_potions.append("mp potion")
                        myPlayer.player_potions.append("mp potion 3")
                        myPlayer.player_gold -= 100
                elif tps_amount1 == "two" or tps_amount1 == "2" and myPlayer.player_gold < 100:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount1 == "three" or tps_amount1 == "3" and myPlayer.player_gold >= 150:
                    if "mp potion" in myPlayer.player_potions or "mp potion 2" in myPlayer.player_potions or "mp potion 3" in myPlayer.player_potions:
                        print("You have one or more mp potions already. You can only hold 3 potions of each type at one time.")
                    elif "mp potion" not in myPlayer.player_potions and "mp potion 2" not in myPlayer.player_potions and "mp potion 3" not in myPlayer.player_potions:
                        print("You have purchased 3 mp potions")
                        myPlayer.player_potions.append("mp potion")
                        myPlayer.player_potions.append("mp potion 2")
                        myPlayer.player_potions.append("mp potion 3")
                        myPlayer.player_gold -= 150
                elif tps_amount1 == "three" or tps_amount1 == "3" and myPlayer.player_gold < 150:
                    print("You do not have enough gold to purchase these items.")
            elif tps_purchase == "mp potion" and myPlayer.player_gold < 50:
                print("You do not have enough gold to purchase that item.")
            elif tps_purchase == "max mp potion" and myPlayer.player_gold >= 150:
                print("Great! You can purchase and hold up to 3 potions of each type, how many would you like?")
                tps_amount2 = input("> ")
                if tps_amount2 == "one" or tps_amount2 == "1":
                    if "max mp potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max mp potion")
                        print("You have purchased 1 max mp potion!")
                        myPlayer.player_gold -= 150
                    elif "max mp potion" in myPlayer.player_potions and "max mp potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max mp potion 2")
                        print("You have purchased 1 max mp potion!")
                        myPlayer.player_gold -= 150
                    elif "max mp potion" in myPlayer.player_potions and "max mp potion 2" in myPlayer.player_potions and "max mp potion 3" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max mp potion 3")
                        print("You have purchased 1 max mp potion!")
                        myPlayer.player_gold -= 150
                    elif "max mp potion" in myPlayer.player_potions and "max mp potion 3" in myPlayer.player_potions and "max mp potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max mp potion 2")
                        myPlayer.player_gold -= 150
                        print("You have purchased 1 max mp potion!")
                    elif "max mp potion 2" in myPlayer.player_potions and "max mp potion 3" in myPlayer.player_potions and "max mp potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max mp potion")
                        myPlayer.player_gold -= 150
                        print("You have purchased 1 max mp potion!")
                    elif "max mp potion" in myPlayer.player_potions and "max mp potion 2" in myPlayer.player_potions and "max mp potion 3" in myPlayer.player_potions:
                        print("You cannot purchase anymore max mp potions.")
                elif tps_amount2 == "one" or tps_amount2 == "1" and myPlayer.player_gold < 150:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount2 == "two" or tps_amount2 == "2" and myPlayer.player_gold >= 300:
                    if "max mp potion" not in myPlayer.player_potions and "max mp potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max mp potion")
                        myPlayer.player_potions.append("max mp potion 2")
                        print("You have purchased 2 max mp potions!")
                        myPlayer.player_gold -= 100
                    elif "max mp potion" in myPlayer.player_potions and "max mp potion 2" in myPlayer.player_potions or "max mp potion" in myPlayer.player_potions and "max mp potion 3" in myPlayer.player_potions or "max mp potion 2" in myPlayer.player_potions and "max mp potion 3" in myPlayer.player_potions: 
                        print("You are already carrying two potions, you can only purchase one more.")
                    elif "max mp potion 2" not in myPlayer.player_potions and "max mp potion 3" not in myPlayer.player_potions and "max mp potion" in myPlayer.player_potions:
                        print("You have purchased 2 max mp potions!")
                        myPlayer.player_gold -= 100
                        myPlayer.player_potions.append("max mp potion 2")
                        myPlayer.player_potions.append("max mp potion 3")
                    elif "max mp potion" not in myPlayer.player_potions and "max mp potion 3" not in myPlayer.player_potions and "max mp potion 2" in myPlayer.player_potions:
                        print("You have purchased 2 max mp potions!")
                        myPlayer.player_potions.append("max mp potion")
                        myPlayer.player_potions.append("max mp potion 3")
                        myPlayer.player_gold -= 100
                elif tps_amount2 == "two" or tps_amount2 == "2" and myPlayer.player_gold < 300:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount2 == "three" or tps_amount2 == "3" and myPlayer.player_gold >= 450:
                    if "max mp potion" in myPlayer.player_potions or "max mp potion 2" in myPlayer.player_potions or "max mp potion 3" in myPlayer.player_potions:
                        print("You have one or more max mp potions already. You can only hold 3 potions of each type at one time.")
                    elif "max mp potion" not in myPlayer.player_potions and "max mp potion 2" not in myPlayer.player_potions and "max mp potion 3" not in myPlayer.player_potions:
                        print("You have purchased 3 max mp potions")
                        myPlayer.player_potions.append("max mp potion")
                        myPlayer.player_potions.append("max mp potion 2")
                        myPlayer.player_potions.append("max mp potion 3")
                        myPlayer.player_gold -= 150
                elif tps_amount2 == "three" or tps_amount2 == "3" and myPlayer.player_gold < 450:
                    print("You do not have enough gold to purchase these items.")
            elif tps_purchase == "max mp potion" and myPlayer.player_gold < 150:
                print("You do not have enough gold to purchase this item.")
            elif tps_purchase == "dmg potion" and myPlayer.player_gold >= 75:
                print("Great! You can purchase and hold up to 3 potions of each type, how many would you like?")
                tps_amount3 = input("> ")
                if tps_amount3 == "one" or tps_amount3 == "1":
                    if "dmg potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("dmg potion")
                        print("You have purchased 1 dmg potion!")
                        myPlayer.player_gold -= 75
                    elif "dmg potion" in myPlayer.player_potions and "dmg potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("dmg potion 2")
                        print("You have purchased 1 dmg potion!")
                        myPlayer.player_gold -= 75
                    elif "dmg potion" in myPlayer.player_potions and "dmg potion 2" in myPlayer.player_potions and "dmg potion 3" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("dmg potion 3")
                        print("You have purchased 1 dmg potion!")
                        myPlayer.player_gold -= 75
                    elif "dmg potion" in myPlayer.player_potions and "dmg potion 3" in myPlayer.player_potions and "dmg potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("dmg potion 2")
                        myPlayer.player_gold -= 75
                        print("You have purchased 1 dmg potion!")
                    elif "dmg potion 2" in myPlayer.player_potions and "dmg potion 3" in myPlayer.player_potions and "dmg potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("dmg potion")
                        myPlayer.player_gold -= 75
                        print("You have purchased 1 dmg potion!")
                    elif "dmg potion" in myPlayer.player_potions and "dmg potion 2" in myPlayer.player_potions and "dmg potion 3" in myPlayer.player_potions:
                        print("You cannot purchase anymore dmg potions.")
                elif tps_amount3 == "one" or tps_amount3 == "1" and myPlayer.player_gold < 75:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount3 == "two" or tps_amount3 == "2" and myPlayer.player_gold >= 150:
                    if "dmg potion" not in myPlayer.player_potions and "dmg potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("dmg potion")
                        myPlayer.player_potions.append("dmg potion 2")
                        print("You have purchased 2 dmg potions!")
                        myPlayer.player_gold -= 150
                    elif "dmg potion" in myPlayer.player_potions and "dmg potion 2" in myPlayer.player_potions or "dmg potion" in myPlayer.player_potions and "dmg potion 3" in myPlayer.player_potions or "dmg potion 2" in myPlayer.player_potions and "dmg potion 3" in myPlayer.player_potions: 
                        print("You are already carrying two potions, you can only purchase one more.")
                    elif "dmg potion 2" not in myPlayer.player_potions and "dmg potion 3" not in myPlayer.player_potions and "dmg potion" in myPlayer.player_potions:
                        print("You have purchased 2 dmg potions!")
                        myPlayer.player_gold -= 150
                        myPlayer.player_potions.append("dmg potion 2")
                        myPlayer.player_potions.append("dmg potion 3")
                    elif "dmg potion" not in myPlayer.player_potions and "dmg potion 3" not in myPlayer.player_potions and "dmg potion 2" in myPlayer.player_potions:
                        print("You have purchased 2 dmg potions!")
                        myPlayer.player_potions.append("dmg potion")
                        myPlayer.player_potions.append("dmg potion 3")
                        myPlayer.player_gold -= 150
                elif tps_amount3 == "two" or tps_amount3 == "2" and myPlayer.player_gold < 150:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount3 == "three" or tps_amount3 == "3" and myPlayer.player_gold >= 225:
                    if "dmg potion" in myPlayer.player_potions or "dmg potion 2" in myPlayer.player_potions or "dmg potion 3" in myPlayer.player_potions:
                        print("You have one or more dmg potions already. You can only hold 3 potions of each type at one time.")
                    elif "dmg potion" not in myPlayer.player_potions and "dmg potion 2" not in myPlayer.player_potions and "dmg potion 3" not in myPlayer.player_potions:
                        print("You have purchased 3 dmg potions")
                        myPlayer.player_potions.append("dmg potion")
                        myPlayer.player_potions.append("dmg potion 2")
                        myPlayer.player_potions.append("dmg potion 3")
                        myPlayer.player_gold -= 225
                elif tps_amount3 == "three" or tps_amount3 == "3" and myPlayer.player_gold < 225:
                    print("You do not have enough gold to purchase these items.")
            elif tps_purchase == "dmg potion" and myPlayer.player_gold < 75:
                print("You do not have enough gold to purchase this item.")
            elif tps_purchase == "max dmg potion" and myPlayer.player_gold >= 200:
                print("Great! You can purchase and hold up to 3 potions of each type, how many would you like?")
                tps_amount4 = input("> ")
                if tps_amount4 == "one" or tps_amount4 == "1":
                    if "max dmg potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max dmg potion")
                        print("You have purchased 1 max dmg potion!")
                        myPlayer.player_gold -= 200
                    elif "max dmg potion" in myPlayer.player_potions and "max dmg potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max dmg potion 2")
                        print("You have purchased 1 max dmg potion!")
                        myPlayer.player_gold -= 200
                    elif "max dmg potion" in myPlayer.player_potions and "max dmg potion 2" in myPlayer.player_potions and "max dmg potion 3" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max dmg potion 3")
                        print("You have purchased 1 max dmg potion!")
                        myPlayer.player_gold -= 200
                    elif "max dmg potion" in myPlayer.player_potions and "max dmg potion 3" in myPlayer.player_potions and "max dmg potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max dmg potion 2")
                        myPlayer.player_gold -= 200
                        print("You have purchased 1 max dmg potion!")
                    elif "max dmg potion 2" in myPlayer.player_potions and "max dmg potion 3" in myPlayer.player_potions and "max dmg potion" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max dmg potion")
                        myPlayer.player_gold -= 200
                        print("You have purchased 1 max dmg potion!")
                    elif "max dmg potion" in myPlayer.player_potions and "max dmg potion 2" in myPlayer.player_potions and "max dmg potion 3" in myPlayer.player_potions:
                        print("You cannot purchase anymore max dmg potions.")
                elif tps_amount4 == "one" or tps_amount4 == "1" and myPlayer.player_gold < 200:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount4 == "two" or tps_amount4 == "2" and myPlayer.player_gold >= 400:
                    if "max dmg potion" not in myPlayer.player_potions and "max dmg potion 2" not in myPlayer.player_potions:
                        myPlayer.player_potions.append("max dmg potion")
                        myPlayer.player_potions.append("max dmg potion 2")
                        print("You have purchased 2 max dmg potions!")
                        myPlayer.player_gold -= 400
                    elif "max dmg potion" in myPlayer.player_potions and "max dmg potion 2" in myPlayer.player_potions or "max dmg potion" in myPlayer.player_potions and "max dmg potion 3" in myPlayer.player_potions or "max dmg potion 2" in myPlayer.player_potions and "max dmg potion 3" in myPlayer.player_potions: 
                        print("You are already carrying two potions, you can only purchase one more.")
                    elif "max dmg potion 2" not in myPlayer.player_potions and "max dmg potion 3" not in myPlayer.player_potions and "max dmg potion" in myPlayer.player_potions:
                        print("You have purchased 2 max dmg potions!")
                        myPlayer.player_gold -= 400
                        myPlayer.player_potions.append("max dmg potion 2")
                        myPlayer.player_potions.append("max dmg potion 3")
                    elif "max dmg potion" not in myPlayer.player_potions and "max dmg potion 3" not in myPlayer.player_potions and "max dmg potion 2" in myPlayer.player_potions:
                        print("You have purchased 2 max dmg potions!")
                        myPlayer.player_potions.append("max dmg potion")
                        myPlayer.player_potions.append("max dmg potion 3")
                        myPlayer.player_gold -= 400
                elif tps_amount4 == "two" or tps_amount4 == "2" and myPlayer.player_gold < 400:
                    print("You do not have enough gold to purchase these items.")
                if tps_amount4 == "three" or tps_amount4 == "3" and myPlayer.player_gold >= 600:
                    if "max dmg potion" in myPlayer.player_potions or "max dmg potion 2" in myPlayer.player_potions or "max dmg potion 3" in myPlayer.player_potions:
                        print("You have one or more max dmg potions already. You can only hold 3 potions of each type at one time.")
                    elif "max dmg potion" not in myPlayer.player_potions and "max dmg potion 2" not in myPlayer.player_potions and "max dmg potion 3" not in myPlayer.player_potions:
                        print("You have purchased 3 max dmg potions")
                        myPlayer.player_potions.append("max dmg potion")
                        myPlayer.player_potions.append("max dmg potion 2")
                        myPlayer.player_potions.append("max dmg potion 3")
                        myPlayer.player_gold -= 600
                elif tps_amount4 == "three" or tps_amount4 == "3" and myPlayer.player_gold < 600:
                    print("You do not have enough gold to purchase these items.")
            elif tps_purchase == "max dmg potion" and myPlayer.player_gold < 200:
                print("You do not have enough gold to pruchase this item.")
        else:
            print("Thanks for stopping in!")
        while tps_action.lower() != "yes" and tps_action.lower() != "no":
            print("Please enter yes or no!")
            tps_action = input("> ")
    if myPlayer.location == "Town BlackSmith":
        print("The Town BlackSmith offers a variety of weapons and armor, for a price.")
        blacksmith_inventory = ["+5 sword", "+7 sword", "+15 sword", "medium armor", "heavy armor", "exit blacksmith"]
        print("Would you like to view his inventory? Enter yes or no.")
        purchase_bs = input("> ")
        if purchase_bs.lower() == 'yes':
            print(blacksmith_inventory)
            print("+5 sword costs 150 gold, \n+7 sword costs 250 gold, \n+15 sword costs 500 gold, \nmedium armor costs 200 gold, \nheavy armor costs 350 gold")
            print("Type in the name of what you would like to purchase")
            bs_action = input("> ")
            if bs_action.lower() == '+5 sword':
                if myPlayer.player_gold >= 150:
                    print("You have purchased and equipped your new +5 sword!")
                    myPlayer.player_wep = "+5 sword"
                    myPlayer.player_gold -= 150
                    if myPlayer.level == 1:
                        myPlayer.mana = randint(21,25)
                    if myPlayer.level == 2:
                        myPlayer.mana = randint(27,31)
                    if myPlayer.level == 3:
                        myPlayer.mana = randint(32,36)
                    if myPlayer.level == 4:
                        myPlayer.mana == randint(36,40)
                else:
                    print("You don't have enough gold to purchase that item!")
            if bs_action.lower() == "+7 sword":
                if myPlayer.player_gold >= 250:
                    print("You have purchased and equipped your new +7 sword!")
                    myPlayer.player_wep = "+7 sword"
                    myPlayer.player_gold -= 250
                    if myPlayer.level == 1:
                        myPlayer.mana = randint(23,27)
                    if myPlayer.level == 2:
                        myPlayer.mana = randint(29,33)
                    if myPlayer.level == 3:
                        myPlayer.mana = randint(34,38)
                    if myPlayer.level == 4:
                        myPlayer.level = randint(38,42)
                else:
                    print("You don't have enough gold to purchase that item!")
            if bs_action.lower() == "+15 sword":
                if myPlayer.player_gold >= 500:
                    print("You have purchased and equipped your new +15 sword!")
                    myPlayer.player_wep = "+15 sword"
                    myPlayer.player_gold -= 500
                    if myPlayer.level == 1:
                        myPlayer.mana = randint(31,35)
                    if myPlayer.level == 2:
                        myPlayer.mana = randint(37,41)
                    if myPlayer.level == 3:
                        myPlayer.mana = randint(42,46)
                    if myPlayer.level == 4:
                        myPlayer.mana = randint(46,50)
                else:
                    print("You don't have enough gold to purchase that item!")
            if bs_action.lower() == "medium armor":
                if myPlayer.player_gold >= 200:
                    print("You have purchased and equipped your new mediuma armor!")
                    myPlayer.player_armor = "medium armor"
                    myPlayer.player_gold -= 200
                    if myPlayer.level == 1:
                        myPlayer.maxhp = 150
                        myPlayer.hp = 150
                    if myPlayer.level == 2:
                        myPlayer.maxhp = 200
                        myPlayer.hp = 200
                    if myPlayer.level == 3:
                        myPlayer.maxhp = 250
                        myPlayer.hp = 250
                    if myPlayer.level == 4:
                        myPlayer.maxhp = 300
                        myPlayer.hp = 300
                else:
                    print("You don't have enough gold to purchase that item!")
            if bs_action.lower() == "heavy armor":
                if myPlayer.player_gold >= 350:
                    print("You have purchase and equipped your new heavy armor!")
                    myPlayer.player_armor = "heavy armor"
                    myPlayer.player_gold -= 350
                    if myPlayer.level == 1:
                        myPlayer.maxhp = 200
                        myPlayer.hp = 200
                    if myPlayer.level == 2:
                        myPlayer.maxhp = 250
                        myPlayer.hp = 250
                    if myPlayer.level == 3:
                        myPlayer.maxhp = 300
                        myPlayer.hp = 300
                    if myPlayer.level == 4:
                        myPlayer.maxhp = 350
                        myPlayer.hp = 350
                else:
                    print("You don't have enough gold to purchase that item!")
            if bs_action.lower() == "exit blacksmith":
                print("Thanks for stopping in!")
        else:
            print("Thanks for looking")
    if myPlayer.location == "Forest Edge":
        print("You see a mystic barrier preventing anyone from going further west.\n To the north you see the town, west you see your home, and south seems to have a cave entrance")
    if myPlayer.location == "Cave Entrance":
        print("Aside from the goblins and small campfire, this room is empty. \nYou see a tunnel leading further into the cave, to enter move south or down.")
    if myPlayer.location == "Cave End":
        print("There seems to be nothing special within this area aside from the many corpses and giant ogre. \nTo exit, you must go back the way you entered.")
    if myPlayer.location == "Cave Tunnel":
        print("You cannot go south or west from here. The Cave Tunnel is just that, a tunnel in a cave.")
        ###### WALLS ########
    if myPlayer.location == "Wall Top":
        print("You cannot go north from here. This is a mystical wall.")
    if myPlayer.location == "Wall Top 2":
        print("You cannot go north from here. This is a mystical wall.")
    if myPlayer.location == "Wall Top 3":
        print("You cannot go north from here. This is a mystical wall.")
    if myPlayer.location == "Wall Top 4":
        print("You cannot go north from here. This is a mystical wall.")
    if myPlayer.location == "Wall Left":
        print("You cannot go east from here. This is a mystical wall.")
    if myPlayer.location == "Wall Left 2":
        print("You cannot go east from here. This is a mystical wall.")
    if myPlayer.location == "Wall Left 3":
        print("You cannot go east from here. This is a mystical wall.")
    if myPlayer.location == "Wall Left 4":
        print("You cannot go east from here. This is a mystical wall.")
    if myPlayer.location == "Wall Right":
        print("You cannot go west from here. This is a mystical wall.")
    if myPlayer.location == "Wall Right 2":
        print("You cannot go west from here. This is a mystical wall.")
    if myPlayer.location == "Wall Right 3":
        print("You cannot go west from here. This is a mystical wall.")
    if myPlayer.location == "Wall Right 4":
        print("You cannot go west from here. This is a mystical wall.")
    if myPlayer.location == "Wall Bottom":
        print("You cannot go south from here. This is a mystical wall.")
    if myPlayer.location == "Wall Bottom 2":
        print("You cannot go south from here. This is a mystical wall.")
    if myPlayer.location == "Wall Bottom 3":
        print("You cannot go south from here. This is a mystical wall.")
    if myPlayer.location == "Wall Bottom 4":
        print("You cannot go south from here. This is a mystical wall.")
        
######### FIGHTING ##################
def player_fight(action):
    if myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
        print("The Goblins have been defeated!")
    if myPlayer.hp <= 0:
        print("You have died!")
        myPlayer.gameover = True
    if myGoblin.hp <= 0 and not myGoblin2.hp <= 0 and not myGoblin3.hp <= 0:
        print("One of the goblins have been defeated!")
        myGoblin2.hp -= myPlayer.mana
        myGoblin3.hp -= myPlayer.mana
        myPlayer.hp -= myGoblin2.dmg
        myPlayer.hp -= myGoblin3.dmg
        print("Your HP is: ")
        print(myPlayer.hp)
        print("The Goblin's HP is: ")
        print(myGoblin2.hp)
        print(myGoblin3.hp)
    elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and not myGoblin3.hp <= 0:
        print("Two of the goblins have been defeated!")
        myGoblin3.hp -= myPlayer.mana
        myPlayer.hp -= myGoblin3.dmg
        print("Your HP is: ")
        print(myPlayer.hp)
        print("The Goblin's HP is: ")
        print(myGoblin3.hp)
    elif myGoblin.hp > 0 and myGoblin2.hp > 0 and myGoblin3.hp > 0:
        print("You swing at all of the Goblins!")
        myGoblin.hp -= myPlayer.mana
        myGoblin2.hp -= myPlayer.mana
        myGoblin3.hp -= myPlayer.mana
        myPlayer.hp -= myGoblin.dmg
        myPlayer.hp -= myGoblin2.dmg
        myPlayer.hp -= myGoblin3.dmg
        print("Your HP is: ")
        print(myPlayer.hp)
        print("The Goblin's HP is:")
        print(myGoblin.hp)
        print(myGoblin2.hp)
        print(myGoblin3.hp)

def player_special(action):
    if myGoblin.hp <= 0 and myGoblin2.hp <= 0 and myGoblin3.hp <= 0:
        print("The Goblins have been slaughtered!")
    if myPlayer.hp <= 0:
        print("You have died!")
        myPlayer.gameover = True
    if myGoblin.hp <= 0 and not myGoblin2.hp <= 0 and not myGoblin3.hp <= 0:
        print("One of the goblins have been defeated!")
        myGoblin2.hp -= myPlayer.special
        myGoblin3.hp -= myPlayer.special
        myPlayer.hp -= myGoblin2.dmg
        myPlayer.hp -= myGoblin3.dmg
        print("Your HP is: ")
        print(myPlayer.hp)
        print("The Goblin's HP is: ")
        print(myGoblin2.hp)
        print(myGoblin3.hp)
    elif myGoblin.hp <= 0 and myGoblin2.hp <= 0 and not myGoblin3.hp <=0:
        print("Two of the goblins have been defeated!")
        myGoblin3.hp -= myPlayer.special
        myPlayer.hp -= myGoblin3.dmg
        print("Your HP: ")
        print(myPlayer.hp)
        print("Goblins HP: ")
        print(myGoblin3.hp)
    elif myGoblin.hp > 0 and myGoblin2.hp > 0 and myGoblin3.hp > 0 and myPlayer.hp > 0:
        print("You swing your sword at a 180 degree arc")
        myGoblin.hp -= myPlayer.special
        myGoblin2.hp -= myPlayer.special
        myGoblin3.hp -= myPlayer.special
        myPlayer.hp -= myGoblin.dmg
        myPlayer.hp -= myGoblin2.dmg
        myPlayer.hp -= myGoblin3.dmg
        myPlayer.mp -= 50
        print("Goblins hp:")
        print(myGoblin.hp)
        print(myGoblin2.hp)
        print(myGoblin3.hp)
        print("Your HP:")
        print(myPlayer.hp)
        print("Your MP:")
        print(myPlayer.mp)
def boss_fight(action):
    if myOgre.hp <=0:
        print("The Ogre has been defeated!")
    if myPlayer.hp <= 0:
        print("You have died!")
        myPlayer.gameover = True
    if myOgre.hp > 0 and myPlayer.hp > 0:
        print("You slice the Ogre, drawing significant blood!")
        myOgre.hp -= myPlayer.mana
        myPlayer.hp -= myOgre.dmg
        print("Ogre's HP:")
        print(myOgre.hp)
        print("Your HP:")
        print(myPlayer.hp)
def boss_fight_special(action):
    if myOgre.hp <=0:
        print("The Ogre has been defeated!")
    if myPlayer.hp <= 0:
        print("You have died!")
        myPlayer.gameover = True
    if myOgre.hp > 0 and myPlayer.hp > 0:
        print("You swing your sword with furious strength!")
        myOgre.hp -= myPlayer.special
        myPlayer.hp -= myOgre.dmg
        myPlayer.mp -= 25
        print("Ogre's HP:")
        print(myOgre.hp)
        print("Your HP:")
        print(myPlayer.hp)
        print("Your MP:")
        print(myPlayer.mp)
##### GAME FUNCTIONALITY#####
    

def main_game_loop():
    while myPlayer.gameover == False:
        prompt()
    #here handle if puzzles solved, boss defeated, etc

def setup_game():
    os.system('clear')
    ## NAME COLLECTING
    question1 = "Hello!, What's your name?\n"
    # These for loops print each character with a delay to make it look more realistic. It could've just been a print statement
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name
    '''
    question2 = "What role would you like to play?\n"
    question2added = "(You can play as a Warrior, Mage, or Priest)\n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_job = ["warrior", "mage", "priest"]
    if player_job.lower() in valid_job:
        myPlayer.job = player_job
        print("You are now a " + player_job + ".\n")
    while player_job.lower() not in valid_job:
        print("Please enter the name of the role in which you'd like to play")
        player_job = input("> ")
        if player_job.lower() in valid_job:
            myPlayer.job = player_job
            print("You are now a " + player_job + ".\n")
    '''
    '''
    if myPlayer.job == "warrior":
        hp = 250
        mana = 10
    elif myPlayer.job == "mage":
        hp = 150
        mana = 20
    elif myPlayer.job == "priest":
        hp = 200
        mana = 20
    '''
    question3 = "Welcome, " + player_name + " to this fantasy world!\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    speech2 = "In this game you will encounter dangerous monsters of all types.\nYou will build your character from level 1 and work your way to saving your home town from an unknown threat only revealed by killing various beasts through out the land.\n"
    speech3 = "Just make sure you don't wind up... dead\n"
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    os.system('clear')
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    print(" ----Let's start the game!---- ")
    print("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")
    speech4 = "You wake up to a loud knock on the front door of your home.\n"
    speech5 = "Half awake and hardly clothed, you stumble out of bed making sure to grab your sword and check the potential threat.\n"
    speech6 = "Upon opening the door you see a group of nearly half the townspeople gathered around your home.\n"
    speech7 = "Instantly, the head councilman of the town speaks up: \n"
    speech8 = '"' + player_name + ' this cannot go on any longer! You must save our town! \nWe have heard the tales of your family aiding in the extinction of the demons who rose from the darkest corners of earth and know you are capable of the same. We are tasking you with finding out why so many of our townspeople are disappearing and what the nearby cave has to do with it."\n'
    speech9 = '"Now go, ' + player_name + ' save our town!"\n'
    speech10 = "You head back inside, get dressed, sheath your sword and hurry back outside, ready to embark on the quest laid before you."
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech5:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech6:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech7:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech8:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech9:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in speech10:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    main_game_loop()

title_screen()