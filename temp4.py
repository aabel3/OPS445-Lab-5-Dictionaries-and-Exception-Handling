#!/usr/bin/env python3
# OPS445 - Lab 5
# temp4.py
# Author: Avraham Abel

try:
	print("5" + "10")
	print("Still inside try block")
except TypeError:
	print("At least one of the values is NOT an integer")

print("End of program")
