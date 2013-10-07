# we set strings as values on every variable.
# x = 10, the first %s = is "binary" and the second %s is "don't.
# The %s means that there is a string variable and %d means that there is a signed integer decimal.
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# We print to variables.
# The print will show : There are 10 types of people. 
# Those who know binary and those who don't. 
print x
print y

# Here we can see that we print out %r (repr()) that means that we print a string and a object will show.
# And %x is to give us the decimal. 
print "I said: %r." % x

# We print out the %s strings and the %y shows the variables: binary and do_not.
print "I also said: '%s'." % y

# A new variable gets the value false.
hilarious = False
# This %r will give us the string false because it is the last string value before the command.
# It will print false if I put %s the as well, but if I put %d it shows 0. 
joke_evaluation = "Isn't that joke so funny?! %r"


# It prints the two variables values sat above.
print joke_evaluation % hilarious

# We give new values to some variables and print them out. 
w = "This is the left side of..."
e = "a string with a right side."

# prints the values of these variables. When we put the + sign between two variables we get a 
# long string. This is because there are two variables that is printed on the same line 
# instead of two seperate lines.
print w + e
