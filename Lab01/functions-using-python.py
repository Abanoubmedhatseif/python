def validateNumber():
    while True:
        try:
            number = float(input("Enter a number: ")) 
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Q1. Check if a number is within the specified range
def check_range():
    number = validateNumber()
    if 20 <= number <= 50:
        print("The number is within the range. ")
    else:
        print("The number is not within the range.")

# Q2. Calculate area and perimeter of a rectangle
def calculateRectangleProperties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    result= {
        "perimeter": perimeter,
        "area": area
    }
    print(result) 

# Q3 Concatenate two strings with different methods
def concatenate_strings(string1, string2):
    concatenated = string1 + string2
    print({"concatenated String": concatenated}) 

# Q4 Square elements in a list
def square_list_elements(*args):
    squared_list = [x * x for x in args]
    print(squared_list) 

# Q5 Merge two dictionaries
def merge_dictionaries(dic1, dic2):
    merged = {**dic1, **dic2}
    print(merged) 
# merge_dictionaries({"a": 1, "b": 2}, {"c": 3, "d": 4})


# Q6 Merge two lists
def merge_lists(list1, list2):
    merged_list = list1 + list2
    return merged_list
# merge_lists([1, 2, 3], [4, 5, 6])



# Q7 Check if keys exist in a dictionary
def check_keys_exist(dictionary):
    if 'job' in dictionary and 'card_number' in dictionary:
        return 'job' in dictionary and 'card_number' in dictionary
    else:
        print("Sorry not found 😢")
        return False
# check_keys_exist({"name": "jone", "email": "jane@outlook.com", "age": 25, "job": "engineer", "address": "cairo, Egypt"})



# Q8 Calculate sum of numbers from 1 to 100
def calculate_sum():
    total = 0
    for number in range(1, 101):
        total += number
    print("Sum of numbers from 1 to 100:", total)
# print(calculate_sum())


# Q9 Check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Q10 Reverse a given string
def reverse_string(input_string):
    return input_string[::-1]
#print(reverse_string("Abanoub"))

# Q11 Check if a string is a palindrome
def is_palindrome(input_string):
    return input_string == input_string[::-1]
#print(is_palindrome("aibohphobia"))

# Q12 Remove even numbers and square remaining odd numbers in a list
def process_list(input_list):
    processed_list = [x * x for x in input_list if x % 2 != 0]
    return processed_list
# print(process_list([1,2,3,4,5,6,7]))


# Q13 Check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number / 2) + 1):
        if number % i == 0:
            return False
    return True
# print(is_prime(5))

# Q14 Calculate factorial of a number
def calculate_factorial(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    return factorial
#print(calculate_factorial(10))

# Q15 Perform various operations on a list of numbers
def perform_operations(numbers):
    results = {
        'sum': sum(numbers),
        'minimum': min(numbers),
        'maximum': max(numbers),
        'squared_list': [num ** 2 for num in numbers]
    }
    return results
#print(perform_operations([1,2,3,4,5,6,7]))
