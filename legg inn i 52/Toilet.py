class Toilet():
    def __init__(self):
        self.name = "toilet"
    
    def enter(self):
        print "Here is your new task: "
        print "You need to clean your toilet, which three cleaning equipment do you use?"
        print "You can only choose three of them."
        print "Broom, mop, sponge, bucket, cleanser, bleach, rags, soap "
        print "towels, dishwashing liquid, duster, vacuum, furniture polish"
            
        action = raw_input("> ")

        if action == "sponge, bucket, soap":
            print "Very good, maybe you can be a maid??"
            print "Ok, your new task will take place in the Bacement"
            return 'Bacement'
            
        else:
            print "WRONG!!"
            return 'Out'