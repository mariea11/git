""" 
"""

from random import randint
class GameRoom():
    def __init__(self):
            self.name = "GameRoom"
            
 
    def play_game (self, userName, low, high): 
        guess = 0
        guesses = 0 
        number = randint(low, high)
        PROMPT = "Please enter your guess, between " + str(low) + " and " + str(high) + ": "           
        # keep guessing until user gets it
        while guess != number:
            guess = input(PROMPT) 
            while guess < low or guess > high:
                print "Invalid guess."
                guess = input(PROMPT)
            guesses += 1
            if guess > number:
                print "My number is lower."
            elif guess < number:
                print "My number is higher."
            else:
                print "You got it!"
                print "Well done,", userName + ". You guessed it in", guesses, "guesses."
                if guesses < 6:
                    return 'Attick'
                else:
                    return 'Out'
         
        
    def set_game_limits (self):
        print "Setting Game Limits."
        print "Low must be 0 or greater."
        print "High must be greater the low."
            
        # keep guessing until user gets it
        lowBoundOk  = False;
        highBoundOk = False;
        while not lowBoundOk and not highBoundOk:
            #loop until low bound value is ok
            while not lowBoundOk:
                value = raw_input("Please enter a valid low bound integer :")
                while not value.isdigit():
                    value = raw_input("Please enter a valid low bound integer :")
                lowBoundOk = self.set_low_bound (value)
                
            #loop until high bound value is ok
            while not highBoundOk:  
                value = raw_input("Please enter a valid high bound integer :")
                while not value.isdigit():
                    value = raw_input("Please enter a valid high bound integer :")
                highBoundOk = self.set_high_bound (value)
                
                
    def save_to_file (self, userName, guesses, myFile):
        print "Saving high scores file ..."
        #open the file in append mode
        f = open(myFile, 'a') 
        saveLine=[];
        saveLine.append(userName);
        saveLine.append(", ");
        saveLine.append(str(guesses));
        f.write(("".join(saveLine))+"\n")  #write name and score as a separate line in the file 
        f.close()
      
    def view_high_scores (self, myFile):
        #open file for read only
        f = open(myFile, 'r')
        print "High Scores :"
        lines = f.readlines() #read each line from file 
        f.close();
        scoreList = []
        
        #loop over the file object and add each line to the list
        for line in lines:
            name,size=line.split(",")
            scoreList.append((name,int(size)))  # append each line in file to the list
            
        #sort the list by using lambda function to sort on item[1]
        scoreList.sort(key=lambda item:item[1])
        for line in scoreList:
            print "%7s %6s" % (line[0], line[1])
        
               
    def set_low_bound(self, value):
        #low value must be greater then 0
        if value > 0:
            #set to global, when we want to change LOW outside its space
            global LOW
            LOW = value
            print "Low bound is ", LOW
            return True
        else:
            return False 
    
    
    def set_high_bound (self, value):   
        #high value must be greater than low value
        if value > LOW:
            #set to global, when we want to change HIGH outside its space
            global HIGH
            HIGH = value
            print "High bound is ", HIGH
            return True
        else:
            return False 
                              
                
    def enter(self):
        LOW = 1
        HIGH = 42
        MENU = "Play Game\n I pick a number and you have to guess it.\n\
        Try and get it in as few guesses as possible. If you manage to guess the number \n\
		in less then 6 times you come to the last test in the Attick"
        
        print MENU
        
        self.play_game("Marie", int(LOW), int(HIGH))    
            
            
