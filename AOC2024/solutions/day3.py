import sys

def read_input(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return list(content)

# function that will search a char array for the chars 'm', 'u', 'l', '(', a number, ',' another number, and ')' only in that order
def search_for_mul(char_array):
    mul = ['m', 'u', 'l']
    left_parenthesis = '('
    right_parenthesis = ')'
    comma = ','
    first_number = 1
    second_number = 1
    for i in range(len(char_array)):
        if char_array[i] == mul[0]:
            if char_array[i + 1] == mul[1]:
                if char_array[i + 2] == mul[2]:
                    if char_array[i + 3] == left_parenthesis:
                        if isinstance(char_array[i + 4], int):
                            first_number = char_array[i + 4]
                            if char_array[i + 5] == comma:
                                if isinstance(char_array[i + 6], int):
                                    second_number = char_array[i + 6]
                                    if char_array[i + 7] == right_parenthesis:
                                        # print(first_number, second_number)
                                        return (first_number * second_number), (i+7)
    return False, float('inf')

# a function that searches a char array for the chars 'd', 'o', '(', and ')' only in that order
def search_for_do(char_array):
    do = ['d', 'o']
    left_parenthesis = '('
    right_parenthesis = ')'
    for i in range(len(char_array)):
        if char_array[i] == do[0]:
            if char_array[i + 1] == do[1]:
                if char_array[i + 2] == left_parenthesis:
                    if char_array[i + 3] == right_parenthesis:
                        return True, (i+3)
    return False, float('inf')

# a function that searches a char array for the chars 'd', 'o', 'n', '\'', 't', '(', and ')' only in that order
def search_for_dont(char_array):
    dont = ['d', 'o', 'n', '\'' ,'t']
    left_parenthesis = '('
    right_parenthesis = ')'
    for i in range(len(char_array)):
        if char_array[i] == dont[0]:
            if char_array[i + 1] == dont[1]:
                if char_array[i + 2] == dont[2]:
                    if char_array[i + 3] == dont[3]:
                        if char_array[i + 4] == dont[4]:
                            if char_array[i + 5] == left_parenthesis:
                                if char_array[i + 6] == right_parenthesis:
                                    return True, (i+6)
    return False, float('inf')

# a function that searches a char array for the next mul, do or dont operation
def search_for_next_operation(char_array):
    dont, dont_index = search_for_dont(char_array)
    do, do_index = search_for_do(char_array)
    product, product_index = search_for_mul(char_array)
    if (dont_index > 0) and (dont_index < do_index) and (dont_index < product_index):
        return "dont", dont_index
    elif (do_index > 0) and (do_index < dont_index) and (do_index < product_index):
        return "do", do_index
    elif (product > 0) and (product_index < dont_index) and (product_index < do_index):
        return product, product_index
    return False, float('inf')

# function that breaks an array of chars into groups of characters and multiple digit numbers
def break_array(char_array):
    broken_array = []
    i = 0
    while i < len(char_array):
        if char_array[i].isdigit():
            num = ''
            while i < len(char_array) and char_array[i].isdigit():
                num += char_array[i]
                i += 1
            broken_array.append(int(num))
        else:
            broken_array.append(char_array[i])
            i += 1
    return broken_array

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day3.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    char_array = read_input(input_file)
    broken_array = break_array(char_array)
    # loop through the char array to find the 'mul' operation and return the sum of all the products
    sum_of_products = 0
    while True:
        index = 0
        result, index = search_for_next_operation(broken_array)
        # print(result, index)
        if isinstance(result, int):
            sum_of_products += result
        elif result == "dont":
            result, index = search_for_do(broken_array)
        if (index + 7) >= len(broken_array):
            break
        broken_array = broken_array[index + 1:]
    print(sum_of_products)