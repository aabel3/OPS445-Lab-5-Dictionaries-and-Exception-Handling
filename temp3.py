#!/usr/bin/env python3
# OPS445 - Lab 5
# temp3.py
# Author: Avraham Abel

# ~file = open("file1.txt", "w")

# ~ file.write('Line1\nLine2 is a little longer \nLine3 is too\n')
# ~ file.write('Last line the file\n')

# ~file.close()

file3 = open("file3.txt", "w")

my_number = 1000
my_list = [1,2,3,4,5]

file3.write(str(my_number))
file3.write("\n")

for number in my_list:
	string = str(number)
	file3.write(string + "\n")

file3.close()

