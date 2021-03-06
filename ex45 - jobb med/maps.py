from random import randint

class Room(object):

    def __init__(self, name, description, pic):
        self.name = name
        self.description = description
        self.paths = {}
		self.pic = pic

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
			
Introduction = Room("Start",
"""
WELCOME to this fun game. In this game you will meet a lot of difficult tasks 
that you have to answer right if you want to win.
At the same time you find out if you can move out from your parents
or if you should stay at home.
You can choose between two rooms, the first is Livingroom and the second is
Kitchen.
""", "introduction.jpg")



LivingRoom = Room("Livingroom",
"""
This is just a little test for you to get warm and ready for the game.
This is easy, so you better get it right
When you want to use your livingroom, what do you do when you get home
from school, work, training etc?
Do you jump to the couch and take a nap?
Do you turn on the TV and watch your favourite program?
Do you clean all the mess you made the night before?
""", "livingroom.jpg")


Kitchen = Room("Kitchen",
"""
If you want to live by yourself, you have to know how to make pancakes.
I will give you some help by listing some of the ingredients.
Your task is to find the one that is missing from the recipe
Recipe:
	Flour
	Salt
	Milk
	Egg
If you can solve this, you are one step further to the goal
""", "kitchen.jpg")


Toilet = Room("Toilet",
"""
Here is your new task:
You need to clean your toilet, which three cleaning equipment do you use?
You can only choose three of them.
Broom, mop, sponge, bucket, cleanser, bleach, rags, soap
towels, dishwashing liquid, duster, vacuum, furniture polish.
""", "toilet.jpg")


Bacement = Room("Bacement",
"""
Oh no, you have a problem here
Your bacement have been intruded by rats and mice.
How will you get rid of them?
You can call your parents? They probably know what you can do.
Or you can set up some traps with cheese to catch them.
Or maybe you want to call some professional to do the job for you.
""", "bacement.jpg"
)


GameRoom = Room("Guess the Code",
"""
I will pick a number and you have to guess it.
Try and get it in as few guesses as possible. If you manage to guess the number
in less then 6 times you come to the last test in the Attick.
""", "code.JPG"
)


Attick = Room("Attick",
"""
If you can manage this hard task you have won the game and you can very
safely move away from your parents.
In the attick, you meet a huge monster with dark eyes, long black hair, and a
long white dress. You have 'the Grudge' in your attick.
What do you do?
Kill it?
Call home, friends or police?
You scare it back.
""", "attick.jpg"
)


generic_death = Room("out", "You couldn't do it!", "gameover.gif")

kitchen_out = Room("out",
"""
You are out of this game, if you made it - Congratulations, you are a true winner and you are qualified to 
move away from home.
If you lost this game you are probably too young to move away from home and stay by your self. You are qualified to live
home with your parents.
""", "gameover.gif")


toilet_out = Room("out",
"""
You are out of this game, if you made it - Congratulations, you are a true winner and you are qualified to 
move away from home.
If you lost this game you are probably too young to move away from home and stay by your self. You are qualified to live
home with your parents.
""", "gameover.gif")

bacement_out = Room("out",
"""
You are out of this game, if you made it - Congratulations, you are a true winner and you are qualified to 
move away from home.
If you lost this game you are probably too young to move away from home and stay by your self. You are qualified to live
home with your parents.
""", "gameover.gif")

GameRoom_out = Room("out",
"""
You are out of this game, if you made it - Congratulations, you are a true winner and you are qualified to 
move away from home.
If you lost this game you are probably too young to move away from home and stay by your self. You are qualified to live
home with your parents.
""", "gameover.gif")

attick_out = Room("out",
"""
You are out of this game, if you made it - Congratulations, you are a true winner and you are qualified to 
move away from home.
If you lost this game you are probably too young to move away from home and stay by your self. You are qualified to live
home with your parents.
""", "gameover.gif")


Introduction.add_paths({
    'kitchen': Kitchen,
    'livingroom': Livingroom
})

Livingroom.add_paths({
    'clean': Kitchen,
    'TV': Introduction,
	'nap': Introduction
})

Kitchen.add_paths({
    'Butter': Toilet,
    'Sugar': Out
})

Toilet.add_paths({
    'sponge, bucket, soap': Toilet
})

Bacement.add_paths({
    'call parents': Out,
	'traps': GameRoom,
    'call professionals': Out
})

GameRoom.add_paths({
    'guesses < 6': Attick,
    'guesses >=6 ': Out
})

Attick.add_paths({
    'kill': Out,
    'call': Out,
	'scare': Out
})

START = Introduction