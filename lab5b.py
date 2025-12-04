#!/usr/bin/env python3

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
	
def append_file_string(file_name, string_of_lines):
    # Appends the string_of_lines to the end of the file named file_name.
    file = open(file_name, "a")
    file.write(string_of_lines)
    file.close()
    
def write_file_list(file_name, list_of_lines):
    # Writes all items from list_of_lines to the file named file_name 
    # where each item is one line.

    file = open(file_name, "w")
    
    for line in list_of_lines:
        file.write(line + "\n")
    
    file.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Reads data from the file named file_name_read, writes that data
    # to the file named file_name_write.
    # Adds a line number to each line in the new file.

    original_list = read_file_list(file_name_read)

    file_to_write = open(file_name_write, "w")

    line_number = 1
    for line in original_list:
        with_number = str(line_number) + ":" + line + '\n'
        file_to_write.write(with_number)
        line_number = line_number + 1

    file_to_write.close()
	
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
