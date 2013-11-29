class Introduction():
	def __init__(self):
		self.name = "Introduction"

	def enter(self):
		print "WELCOME to this fun game"
		print "In this game you will meet a lot of difficult tasks"
		print "that you have to answer right if you want to win."
		print "At the same time you find out if you can move out from your parents"
		print "or if you should stay at home."
		print "You can choose between two rooms, the first is Livingroom and the second is"
		print "Kitchen."
		
		action = raw_input("> ")

		if action == "Kitchen":
			print "Welcome to the kitchen."		
			return 'Kitchen'

		elif action == "Livingroom":
			print "Welcome to the livingroom."
			return 'LivingRoom'