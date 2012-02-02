cars = 100 # 100 cars
space_in_a_car = 4.0 # 4 spaces in a car, float.
drivers = 30 # 30 drivers
passengers = 90 # 90 passengers
cars_not_driven = cars - drivers # 100-30 = 70. 70 empty cars
cars_driven = drivers # 30 cars driven
carpool_capacity = cars_driven * space_in_a_car # 30*4.0 = 120.0 .
average_passengers_per_car = passengers / cars_driven # 90/30 = 3.
# The error that occured in line 8 when it was:
# average_passengers_per_car = car_pool_capacity / passenger
# is due to the fact car_pool_capacity does not exist.
# It is in fact carpool_capacity, as seen in line 7. An undefined variable was being called for an equation, due to the extra underscore between "car" and "pool".
# Additionally, there would still be an error, because the carpool capacity of 120 divided by the number of passengers, 90, would result
# in 1, which would be incorrect mathematics. And there is no "passenger" variable; only "passengers".


print "There are", cars, "cars available." # 100.
print "There are only", drivers, "drivers available." # 30
print "There will be", cars_not_driven, "empty cars today." # 70.
print "We can transport", carpool_capacity, "people today." # 120.0.
print "We have", passengers, "to carpool today." # 90.
print "We need to put about", average_passengers_per_car, "in each car." # 3.
