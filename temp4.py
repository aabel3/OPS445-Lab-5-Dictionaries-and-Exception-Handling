#!/usr/bin/env python3

try:
	print("5" + "10")
	print("Still inside try block")
except TypeError:
	print("At least one of the values is NOT an integer")

print("End of program")
