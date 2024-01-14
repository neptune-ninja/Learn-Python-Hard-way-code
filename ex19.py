#this is a function which takes two input values
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print(f"You have {cheese_count} cheeses")
	print(f"You have {boxes_of_crackers} number of boxes")
	print("Man that's enough for a Party!")
	print("Get a blancket \n")


print("we can just give function names directyly")
#calling the function
cheese_and_crackers(20,30)

print("OR we can give variables from our script")
#initialising variables
number_of_cheese = 50
num_crackers = 100

#calling the functions
cheese_and_crackers(number_of_cheese,num_crackers)

print("we can even do math inside it")
#calling the function with math
cheese_and_crackers(10+2,30+29)

print("we can combine variables with integer")
cheese_and_crackers(number_of_cheese+10,num_crackers+100)



