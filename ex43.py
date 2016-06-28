from sys import exit
from random import randint

class Scene(object):
    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    quips = ["You Died. You kinda suck at this.",
             "Your mom would be proud...if she were smarter.",
             "Such a luser.",
             "I have a small puppy that's better at this."
             ]

    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("Your action choices are as follows:->")
        print("shoot")
        print("dodge")
        print("tell a joke")
        print("CentralCorridor enter additionalLine1")
        print("\n")
        print("CentralCorridor enter additionalLine2")
        print("CentralCorridor enter additionalLine3")
        print("CentralCorridor enter additionalLine4")
        print("CentralCorridor enter additionalLine5")

        action = input("> ")

        if action == "shoot":
            print("CentralCorridor enter inside if shoot Line1")
            print("CentralCorridor enter inside if shoot Line2")
            print("CentralCorridor enter inside if shoot Line3")
            print("CentralCorridor enter inside if shoot Line4")
            print("CentralCorridor enter inside if shoot Line5")
            print("CentralCorridor enter inside if shoot Line6")
            return 'death'

        elif action == "dodge":
            print("CentralCorridor enter inside elif dodge Line1")
            print("CentralCorridor enter inside elif dodge Line2")
            print("CentralCorridor enter inside elif dodge Line3")
            print("CentralCorridor enter inside elif dodge Line4")
            print("CentralCorridor enter inside elif dodge Line5")
            print("CentralCorridor enter inside elif dodge Line6")
            return 'death'

        elif action == "tell a joke":
            print("CentralCorridor enter inside elif 'inside a joke' Line1")
            print("CentralCorridor enter inside elif 'inside a joke' Line2")
            print("CentralCorridor enter inside elif 'inside a joke' Line3")
            print("CentralCorridor enter inside elif 'inside a joke' Line4")
            print("CentralCorridor enter inside elif 'inside a joke' Line5")
            print("CentralCorridor enter inside elif 'inside a joke' Line6")
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print("LaserWeaponArmory enter Line1")
        print("LaserWeaponArmory enter Line2")
        print("LaserWeaponArmory enter Line3")
        print("LaserWeaponArmory enter Line4")
        print("LaserWeaponArmory enter Line5")
        print("LaserWeaponArmory enter Line6")
        print("LaserWeaponArmory enter 'please enter a 3 digit code:->' ")
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("LaserWeaponArmory enter inside if Line1")
            print("LaserWeaponArmory enter inside if Line2")
            print("LaserWeaponArmory enter inside if Line3")
            return 'the_bridge'
        else:
            print("LaserWeaponArmory enter inside else Line1")
            print("LaserWeaponArmory enter inside else Line2")
            print("LaserWeaponArmory enter inside else Line3")
            print("LaserWeaponArmory enter inside else Line4")
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print("TheBridge 'Your options are:->'")
        print("throw the bomb")
        print("slowly place the bomb")
        print("TheBridge enter additional Line1")
        print("TheBridge enter additional Line2")
        print("TheBridge enter additional Line3")

        action = input("> ")

        if action == "throw the bomb":
            print("TheBridge enter inside if Line1")
            print("TheBridge enter inside if Line2")
            print("TheBridge enter inside if Line3")
            print("TheBridge enter inside if Line4")
            print("TheBridge enter inside if Line5")
            print("TheBridge enter inside if Line6")
            return 'death'
        elif action == "slowly thorw the bomb":
            print("TheBridge enter inside elif Line1")
            print("TheBridge enter inside elif Line2")
            print("TheBridge enter inside elif Line3")
            print("TheBridge enter inside elif Line4")
            print("TheBridge enter inside elif Line5")
            print("TheBridge enter inside elif Line6")
            print("TheBridge enter inside elif Line7")
            print("TheBridge enter inside elif Line8")
            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE")
            return 'the_bridge'

class Escape_Pod(Scene):
    def enter(self):
        print("Escape_pod enter Line1")
        print("Escape_pod enter Line2")
        print("Escape_pod enter Line3")
        print("Escape_pod enter Line4")
        print("Escape_pod enter Line5")
        print("Escape_pod enter Line6")
        print("Escape_pod enter Line7 'Choose a pod from 5 pods:' ")

        good_pod = randint(1,5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("Escape_pod enter inside if %s pod:" % guess)
            print("Escape_pod enter inside if Line1")
            print("Escape_pod enter inside if Line2")
            print("Escape_pod enter inside if Line3")
            return 'death'
        else:
            print("Escape_pod enter inside else %s pod:" % guess)
            print("Escape_pod enter inside else Line1")
            print("Escape_pod enter inside else Line2")
            print("Escape_pod enter inside else Line3")
            print("Escape_pod enter inside else Line4")
            print("Escape_pod enter inside else 'You Won!' ")

            return 'finished'

class Map(object):
    scenes = {'central_corridor': CentralCorridor(),
              'laser_weapon_armory': LaserWeaponArmory(),
              'the_bridge': TheBridge(),
              'escape_pod': Escape_Pod(),
              'death': Death()
              }

    def __init__(self,start_scene):
        self.start_scene = start_scene
    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
