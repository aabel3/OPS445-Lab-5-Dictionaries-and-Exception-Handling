#!/usr/bin/env python3
# OPS445 - Lab 5
# lab5a.py
# Author: Avraham Abel

def read_file_string(file_name):
    # Takes a filename string, returns a string of all lines in the file
    file = open(file_name, "r")
    file_contents = file.read()
    file.close()
    return file_contents

def read_file_list(file_name):
	# Takes a filename string, returns a list of lines without new-line characters
	file = open(file_name, "r")
	
	list_of_lines_with_newlines = list(file)
	
	list_of_lines = []
	for line in list_of_lines_with_newlines:
		list_of_lines.append(line.strip())
	
	file.close()
	return list_of_lines
	
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
