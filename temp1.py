#!/usr/bin/env python3
# OPS445 - Lab 5
# temp1.py
# Author: Avraham Abel

file = open("data.txt", "r")

# ~ file_contents = file.read()
# ~ list_of_lines = file_contents.split("\n")

# ~ list_of_lines = list(file)

list_of_lines = file.readlines()

print(list_of_lines)

file.close()
