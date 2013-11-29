class Attick ():
	def __init__(self):
		self.name = "Attick"
        
	def enter(self):
		print "If you can manage this hard task you have won the game and you can very"
		print "safely move away from your parents."
		print "In the attick, you meet a huge monster with dark eyes, long black hair, and a"
		print "long white dress. You have 'the Grudge' in your attick."
		print "What do you do?"
		print "Kill it?"
		print "Call home, friends or police?"
		print "You scare it back."

		action = raw_input("> ")

		if action == "kill":
			print "You can't kill a monster."
			print "Monster only exist in your mind"
			print "Too bad, you lose."
			return 'Out'

		elif action == "call":
			print "Do you really want to call someone, at this moment you don't have time to call."
			print "You lose the game and have to stay home with your parents."
			return 'Out'
            
		elif action == "scare":
			print "YOU MADE IT"
			print "You take care of your own problems, and will manage to stay away from"
			print "your parents very well."
			return 'Out'
        
		else:
			print "This is not one of your options!"
			return "Attick"