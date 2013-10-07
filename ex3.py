print "I will now count my chickens:"

# 30/6 is the first operation, this number is then added with 25. 
print "Hens", 25 + 30 / 6

# I don't understand what the percent does, when I use my calculator the answer is 300?
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count eggs:"

# * and / are always calculated first, and then - and + is added.
print 3 + 2 + 1 -5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

# This is not true. 5 is greater than -2.
print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# What are floating point numbers?
# Why does / (divide) round down?
# It's not really rounding down; it's just dropping the fractional part after the decimal. 
# Try doing 7.0 / 4.0 and compare it to 7 / 4 and you'll see the difference.
# What does the % sign??
# Why is the % character a "modulus" and not a "percent"?
# Mostly that's just how the designers chose to use that symbol. 
# In normal writing you are correct to read it as a "percent."
# In programming this calculation is typically done with simple division and the / operator. The % modulus is a different operation that just happens to use the % symbol.
# How does % work?
# Another way to say it is, "X divided by Y with J remaining." For example, "100 divided by 16 with 4 remaining." 
# The result of % is the J part, or the remaining part.
