#total number of cars
cars = 100
#space in each car
space_in_a_car = 4
#number of drivers
drivers = 30
#Total number of passengers
passengers = 90
#cars not driven
cars_not_driven = cars - drivers
#total cars driven
cars_driven = drivers
#Total carpool capacity
carpool_capacity = cars_driven * space_in_a_car


print("There are ",cars,"cars available. ")
print("There are only ", drivers , "drivers available")
print("there will be" , cars_not_driven , "cars not driven today")
print("we can transport ",carpool_capacity,"People today")
