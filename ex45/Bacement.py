        
class Bacement():

    def __init__(self):
        self.name = "Bacement"

    def enter(self):
        print "Oh no, you have a problem here"
        print "Your bacement have been intruded by rats and mice."
        print "How will you get rid of them?"
        print "You can call your parents? They probably know what you can do."
        print "Or you can set up some traps with cheese to catch them."
        print "Or maybe you want to call some professional to do the job for you."

        action = raw_input("> ")

        if action == "call parents":
            print "Oh no, you came this far in the game and you actually thought you"
            print "you could call your parents?"
            print "Then you might as well stay home with your parents so your phone bill"
            print "don't get to large."
            return 'Out'


        elif action == "traps":
            print "Very good, when you live by yourself you have to solve problems by yourself."
            print "You are doing a good job, there is just one last task before you can move"
            print "away from your parents."
            return 'GameRoom'
            
        elif action == "call professional":
            print "You can manage this without professionals."
            return 'Out'
        
        else:
            print "This is not one of your options!"
            return "Bacement"
