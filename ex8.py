# We give the variable a value. The value here is a string with four objects.
formatter = "%r %r %r %r"

# We print four number - objects that are assigned as strings. 
print formatter % (1, 2, 3, 4)
# We print four objects that all are strings.
print formatter % ("one", "two", "three", "four")
# We print four objects.
print formatter % (True, False, False, True)
# We print the variable formatter four times.
print formatter % (formatter, formatter, formatter, formatter)

# We print four text - objects that gives us a text on the same line because of the commas.
# In the output of this print on the "But it didn't sing it prints with ", but on the other strings 
# it prints '. This is because in didn't there is a ', so it prints with " so the string doesn't
# end ad "didn't". 
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
