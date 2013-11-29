class LivingRoom(): 
    def __init__(self):
        self.name = "LivingRoom"
        
    def enter(self):    
        print "This is just a little test for you to get warm and ready for the game"
        print "This is easy, so you better get it right"
        print "When you want to use your livingroom, what do you do when you get home"
        print "from school, work, training etc?"
        print "Do you jump to the couch and take a nap?"
        print "Do you turn on the TV and watch your favourite program?"
        print "Do you clean all the mess you made the night before?"

        action = raw_input("> ")

        if action == "clean":
            print "Very nice. You chose to clean the place. After this you can take a"
            print "nap or watch your favourite program, but first, you have some more tasks"
            print "before you win this game."        
            return 'Kitchen'

        elif action == "TV":
            print "You stupid pig, the livingroom needs to be clean if you want to watch TV."
            print "You get another chance, use it well."
            return 'Start'
            
        elif action == "nap":
            print "NO!!NO!!NO!! I understand you are tired, but you need to clean first"
            print "Rule number one, always clean first, nap after"
            print "You get another chance, use it well."
            return 'Start'
        
        else:
            print "This is not one of your options!"
            return "LivingRoom"
