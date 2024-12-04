import sys
import re

# function that reads the input file as an array of rows
def read_input_as_rows(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    # return the forward lines and the reversed lines
    return lines, [line[::-1] for line in lines]

# function that reads the input file as an array of columns
def read_input_as_columns(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    columns = []
    for i in range(len(lines[0])):
        column = []
        for j in range(len(lines)):
            column.append(lines[j][i])
        columns.append(column)
    # turn the columns into strings
    columns = [''.join(column) for column in columns]
    # return the forward columns and the reversed columns
    return columns, [column[::-1] for column in columns]

# function that reads the input file as a list of diagonals from left to right
def read_input_as_diagonalsLR(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    diagonals = []
    for i in range(len(lines[0])):
        diagonal = []
        for j in range(len(lines)):
            if i + j < len(lines[0]):
                diagonal.append(lines[j][i + j])
        diagonals.append(diagonal)
    for i in range(1, len(lines)):
        diagonal = []
        for j in range(len(lines)):
            if i + j < len(lines):
                diagonal.append(lines[i + j][j])
        diagonals.append(diagonal)
    # turn the diagonals into strings
    diagonals = [''.join(diagonal) for diagonal in diagonals]
    # return the forward diagonals and the reversed diagonals
    return diagonals, [diagonal[::-1] for diagonal in diagonals]

# function that reads the input file as a list of diagonals from right to left
def read_input_as_diagonalsRL(file_path):
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()
    diagonals = []
    for i in range(len(lines[0])):
        diagonal = []
        for j in range(len(lines)):
            if i - j >= 0:
                diagonal.append(lines[j][i - j])
        diagonals.append(diagonal)
    for i in range(1, len(lines)):
        diagonal = []
        for j in range(len(lines)):
            if i + j < len(lines):
                diagonal.append(lines[i + j][len(lines[0]) - 1 - j])
        diagonals.append(diagonal)
    # turn the diagonals into strings
    diagonals = [''.join(diagonal) for diagonal in diagonals]
    # return the forward diagonals and the reversed diagonals
    return diagonals, [diagonal[::-1] for diagonal in diagonals]

# function that will search a char array for the chars 'X', 'M', 'A', 'S' only in that order
def search_for_xmas(char_array):
    occurences = re.findall(r'XMAS', char_array)
    # if (len(occurences) > 0):
    #     print(char_array)
    return occurences

# a function that places a . at every spot in the string that is not in an occurance of 'XMAS'
def hide_xmas(char_array):
    occurences = re.finditer(r'XMAS', char_array)
    # occurences = re.finditer(r'^(?!.*XMAS).+$', char_array)
    new_string = ''
    last_index = 0
    for occurence in occurences:
        new_string += char_array[last_index:occurence.start()]
        new_string += '.' * (occurence.end() - occurence.start())
        last_index = occurence.end()
    new_string += char_array[last_index:]
    return new_string

def main():
    if len(sys.argv) != 2:
        print("Usage: python day4.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    forward_rows, reversed_rows = read_input_as_rows(input_file)
    forward_columns, reversed_columns = read_input_as_columns(input_file)
    forward_diagonalsLR, reversed_diagonalsLR = read_input_as_diagonalsLR(input_file)
    forward_diagonalsRL, reversed_diagonalsRL = read_input_as_diagonalsRL(input_file)

    total_xmas = 0

    for row in forward_rows:
        total_xmas += len(search_for_xmas(row))
    for row in reversed_rows:
        total_xmas += len(search_for_xmas(row))
    for column in forward_columns:
        total_xmas += len(search_for_xmas(column))
    for column in reversed_columns:
        total_xmas += len(search_for_xmas(column))
    for diagonal in forward_diagonalsLR:
        total_xmas += len(search_for_xmas(diagonal))
    for diagonal in reversed_diagonalsLR:
        total_xmas += len(search_for_xmas(diagonal))
    for diagonal in forward_diagonalsRL:
        total_xmas += len(search_for_xmas(diagonal))
    for diagonal in reversed_diagonalsRL:
        total_xmas += len(search_for_xmas(diagonal))

    print(total_xmas)


if __name__ == "__main__":
    main()
