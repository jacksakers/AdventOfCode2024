import sys

def read_numbers_from_file(file_path):
    left_numbers = []
    right_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            numbers = line.split()
            # convert the numbers to integers
            numbers = [int(number) for number in numbers]
            left_numbers.append(numbers[0])
            right_numbers.append(numbers[1])
    return left_numbers, right_numbers

# order the left and right numbers
# pair the smallest number in the left with the smallest number in the right and so on
# calculate the difference between the pairs
# return the sum of the differences
def calculate_difference(left_numbers, right_numbers):
    left_numbers.sort()
    right_numbers.sort()
    differences = 0
    for i in range(len(left_numbers)):
        differences += abs(left_numbers[i] - right_numbers[i])
    return differences

# calculate how often the left_numbers appear in the right_numbers
# return a similarity score that adds up each number in the left_numbers multiplied by how many times it appears in the right_numbers
def calculate_similarity(left_numbers, right_numbers):
    similarity = 0
    for number in left_numbers:
        similarity += right_numbers.count(number) * number
    return similarity

def main():
    if len(sys.argv) != 2:
        print("Usage: python day1.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    left_numbers, right_numbers = read_numbers_from_file(file_path)
    # print(calculate_difference(left_numbers, right_numbers))
    print(calculate_similarity(left_numbers, right_numbers))

if __name__ == "__main__":
    main()