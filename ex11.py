# Here we print some text first and then we ask the user to give some inputs on the questions.
# The raw_input is given by the users input on the keyboard in the Terminal. 
print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# We print the text and the input from the user. 
print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

# I tried to write my own code to check if you could only have numbers. 
# It showed that the raw_input can be both numbers and text. 
print "What is your name?", 
name = raw_input()
print "What is 10 * 10?",
answer = raw_input()
print "Do you have a question?", 
question = raw_input() 

print "Your name is %r, your answer is %r and your question is: %r" % (
name, answer, question)
