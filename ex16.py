from sys import argv

script , file_name = argv

print(f"we are going to earase the {file_name}")
print("If you don't want to earase the file enter COMMANS+C")
print("Enter RETURN if you want to continue")

input("?")

print("Opening the file....")
target = open(file_name,'w')

print("Truncating the file , GoodBye")
target.truncate()

print("Now i will ask you to write three lines")

line1 = input("line1 :")
line2 = input("line2 :")
line3 = input("line3 :")

print("Now i am going to write these in file")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally we close it")
target.close()







