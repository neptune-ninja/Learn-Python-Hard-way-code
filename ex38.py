ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait These are not 10 things in the list, Let's fix it up")

my_list = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

stuff = ten_things.split(' ')

while len(stuff) != 10:
	next_one = my_list.pop()
	print("Adding :", next_one)
	stuff.append(next_one)
	print(f"There are {len(stuff)} items now")

print("There we go ", stuff)

print("Let's do some things with the stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff))
print('#'.join(stuff[3:5]))













