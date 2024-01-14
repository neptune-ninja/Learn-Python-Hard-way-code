from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying {from_file} to {to_file}")

open_file = open(from_file)
file_data = open_file.read()

#print(f"The input file is {len(file_data)} bytes long")

print(f"Does the output file exists {exists(to_file)}")
#print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input()

out_file = open(to_file,'w')
out_file.write(file_data)

print("Alright Done! ")

out_file.close()
open_file.close()



