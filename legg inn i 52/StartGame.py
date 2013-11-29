from Toilet import Toilet
from Bacement import Bacement
from Attick import Attick
from Kitchen import Kitchen
from LivingRoom import LivingRoom
from GameRoom import GameRoom
from Introduction import Introduction
from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
                      
class Out():
    quips = [
        "You are out of this game",
         "You are not capable to live away from home.",
         "You can try to play the game one more time."   
    ]
    
    def enter(self):
        print Out.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Map(object):
    
    scenes = {
		'Introduction': Introduction(),
        'Kitchen': Kitchen(),
        'LivingRoom': LivingRoom(),
        'Toilet': Toilet(),
        'Bacement': Bacement(),
		'GameRoom': GameRoom(),
        'Attick': Attick(),
        'Out': Out()
    }
     
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
         
a_map = Map('Introduction')
a_game = Engine(a_map)
a_game.play()            
