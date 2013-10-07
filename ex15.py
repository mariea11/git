from sys import argv

script, filename = argv

# The command open. Open takes a parameter and returns a value that I set to my variable. Here
# we open a file.
txt = open(filename)

# Prints the file.
print "Here's your file %r:" % filename
# Here we call a function on txt. We give the file a command by using the ".". 
# Here we gave it the command "read" with no parameters.
print txt.read()

# We ask if the user can type the file name one more time
# After this we print the file again. 
print "Type the file name again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
