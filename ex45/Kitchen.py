class Kitchen():
    def __init__(self):
        self.name = "Kitchen"
        
    def enter(self):
        print "If you want to live by yourself, you have to know how to make pancakes."
        print "I will give you some help by listing some of the ingredients."
        print "Your task is to find the one that is missing from the recipe"
        print "Recipe: "
        print "  Flour"
        print "  Salt"
        print "  Milk"
        print "  Egg"
        print "If you can solve this, you are one step further to the goal"
        
        action = raw_input("> ")

        if action == "butter":
            print "Very good, are you a chef or something?"
            print "Making pancakes is easy, but remembering the recipe is difficult"
            print "You did good, but now the tasks will get more difficult, "
            print "Can you manage the stress?"  
            print "Ok, your new task will take place on the toilet."
            return 'Toilet'

        elif action == "Sugar":
            print "No, no, no, we don't use sugar in pancakes"
            print "When you live alone, it is much easier to get fat from all the fastfood"
            print "so we don't put sugar in pancakes as well."
            print "You should have thought about this"
            return 'Out'
            
        else:
            print "WRONG"
            return 'Out'   