# import argument variable from system
from sys import argv

# Assigninig values to script and file_name
script, file_name = argv

#opening fine_name using open function
txt = open(file_name)

#after opening the file we have to read the file so we use read command
print(f"Here's your file {file_name}")
print(txt.read())

#now we are prompting the user to write the file name
print("Type the file name Again")
file_again = input('> ')

#opening the file 
txt_again = open(file_again)

#reading and printing the filen
print(txt_again.read())