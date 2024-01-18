i = 0
numbers = []

while i > 6:
	print(f"At the top of i is {i}")
	numbers.append(i)

	i += 1
	print(f"Number now : {i}")
	
	print(f"At the bottom of i is {i}")

print("Print numbers :")

for i in numbers:
	print(i)