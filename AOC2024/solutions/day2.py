import sys

def process_line(line):
    return list(map(int, line.split()))

# determine if a line is 'safe' by checking if:
# 1. the numbers are either all increasing or all decreasing
# 2. any two adjacent numbers only differ by at least 1 and at most 3
def is_safe(numbers):
    increasing = False
    decreasing = False
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            if increasing == True:
                return False
            decreasing = True
        elif numbers[i] > numbers[i - 1]:
            if decreasing == True:
                return False
            increasing = True
        difference = abs(numbers[i] - numbers[i - 1])
        if difference < 1 or difference > 3:
            return False
        if numbers[i] - numbers[i - 1] > 3:
            return False
    # print(numbers)
    return True

# a function that will remove a number from a list
def remove_number(numbers, index):
    return numbers[:index] + numbers[index + 1:]

def main(file_path):
    number_of_safe_arrays = 0
    with open(file_path, 'r') as file:
        for line in file:
            numbers = process_line(line.strip())
            # print the sum of how many arrays are 'safe'
            if is_safe(numbers):
                number_of_safe_arrays += 1
            else:
                for i in range(len(numbers)):
                    if is_safe(remove_number(numbers, i)):
                        number_of_safe_arrays += 1
                        break
    print(number_of_safe_arrays)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day2.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)