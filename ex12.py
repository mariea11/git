# The changes from ex11 and this one is that instead of using print to show the user what we want 
# in the raw_input, we can write it inside the parenthesis. 
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)

# Pydoc is a documentation module for the programming language Python. Pydoc allows Python
# programmers to access Python's documentation help files, 
# generate HTML pages with documentation specifics, and find the appropriate module for a particular job.