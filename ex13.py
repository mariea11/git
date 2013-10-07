# The import command: how you add features to your script from the Python feature set.
# The argv is the argument variable
from sys import argv

# This line unpacks argv, so that rather than hold the variables, it gets assigned to four variables.
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# When I just write two arguments in my terminal I get an error-message that tells me
# that I need 3 values to unpack argv. 