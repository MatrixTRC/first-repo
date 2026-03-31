# function that returns the biggest number in a list and raises an error if the list is empty
def find_biggest_number_or_error(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    return max_number

if __name__ == "__main__":
    print(find_biggest_number_or_error([1, 2, 3]))

