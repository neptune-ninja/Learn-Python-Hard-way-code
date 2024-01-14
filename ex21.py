def add(a,b):
	print(f"Adding {a} + {b}")
	return a+b
def subtract(a,b):
	print(f"Subtraction {a} - {b}")
	return a-b
def multiply(a,b):
	print(f"multiplying {a} * {b}")
	return a*b
def divide(a,b):
	print(f"dividing {a} / {b}")
	return a/b

age = add(30,5)
height = subtract(400,300)
weight = multiply(5,10)
iq = divide(500,10)

print(f"Age : {age}  Height : {height}  Weight : {weight}  IQ : {iq}")

# a puzzle for extra credit
print("Here is a puzzle")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print("That becomes", what , "can your do it by hand")










