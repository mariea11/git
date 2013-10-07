
# In this section we give the numbers a variable. 
# Cars here, means 100. So when you write cars, it will show the number 100, or the number you give the 
# variable. 
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# In this section we can see how the variables are used. "There are 'cars' cars available" will show 
# that there are 100 cars available because the number 100 is sat to this variable. This number will
# change here automatically when we set another number to the variable in the section above. 
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
# Because space_in_a_car is with a floating point number, the answer will also come out as a floating point number.
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# What does this error message mean?
# Traceback (most recent call last):
# File "ex4.py", line 8, in <module>
# average_passengers_per_car = car_pool_capacity / passenger
# NameError: name 'car_pool_capacity' is not defined
# It means that we did not give car_pool_capacity number or a value.
