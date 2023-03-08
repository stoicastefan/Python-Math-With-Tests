import math


# - Calculate the area of a circle

def circle_area(radius):
    area = math.pi * (radius ** 2)

    return area


# - Calculate the factorial of a number

def factorial_of_a_number(number):
    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    return factorial


# - Find the maximum of three numbers

def maximum_of_3_numbers(number1, number2, number3):
    maximum_number = number1

    if number2 > maximum_number:
        maximum_number = number2

    if number3 > maximum_number:
        maximum_number = number3

    return maximum_number


# - Check if a number is prime or not

def check_if_number_is_prime(number):
    is_not_prime = False

    for i in range(2, number):
        if number % i == 0:
            is_not_prime = True

    if is_not_prime:
        return False
    else:
        return True


# - Return the Fibonacci sequence

def get_fibonacci_sequence(sequence_length):
    first_number = 0
    second_number = 1
    fibonacci_sequence = []

    if sequence_length >= 1:
        fibonacci_sequence.append(0)

    if sequence_length >= 2:
        fibonacci_sequence.append(1)

    while len(fibonacci_sequence) < sequence_length:
        fibonacci_sequence.append(first_number + second_number)

        aux_number = first_number
        first_number = second_number
        second_number = second_number + aux_number

    return fibonacci_sequence


# - Calculate the sum of two numbers

def sum_of_2_numbers(first_number, second_number):
    return first_number + second_number


# - Calculate the average of a list of numbers

def avg_for_a_list_of_numbers(list_of_numbers):
    sum_of_numbers = 0

    for number in list_of_numbers:
        sum_of_numbers += number

    return sum_of_numbers / len(list_of_numbers)


# - Check if a number is even

def check_if_a_number_is_even(number):
    number = int(input("EX12. Number: "))

    if number % 2 == 0:
        return True
    else:
        return False


# - Find the largest number in a list

def get_largest_number_in_a_list(list_of_numbers):
    if len(list_of_numbers) > 1:
        largest_number = list_of_numbers[0]

    for number in list_of_numbers[1:]:
        if number > largest_number:
            largest_number = number

    return largest_number


# - Find the smallest number in a list

def get_smallest_number_in_a_list(list_of_numbers):
    if len(list_of_numbers) > 1:
        smallest_number = list_of_numbers[0]

    for number in list_of_numbers[1:]:
        if number < smallest_number:
            smallest_number = number

    return smallest_number


# - Check if a number is divisible by another number

def check_if_a_number_is_divisible_to_another(number_to_be_divisible, number_to_divide):
    if number_to_be_divisible % number_to_divide == 0:
        return True
    else:
        return False


# - Check if a number is a perfect square

def check_if_a_number_is_perfect_square(number):
    is_square = False

    for i in range(1, number):
        if i ** 2 == number:
            is_square = True

    if is_square:
        return True
    else:
        return False


# - Find the sum of the digits of a number

def sum_of_digits_of_a_number(number):
    sum_of_digits = 0

    while number > 0:
        sum_of_digits += int(number % 10)
        number /= 10

    return sum_of_digits


# - Check if a number is a palindrome or not

def check_if_a_number_is_palindrome(number):
    palindrome = ""
    number_as_string = str(number)

    for i in reversed(number_as_string):
        palindrome += i

    if number_as_string == palindrome:
        return True
    else:
        return False


# - Calculate the distance between two points

def distance_between_2_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# - Find the sum of the first n natural numbers

def ex26(number):
    sum_of_numbers = 0
    number_as_string = str(number)

    for i in range(1, number_as_string + 1):
        sum_of_numbers += i

    return sum_of_numbers


# - Find the sum of the digits of a number until it is a single digit

def sum_of_the_digits_of_a_number_until_is_single_digit(number):
    sum_of_digits = 0

    while number >= 10:
        sum_of_digits += number % 10
        number = int(number / 10)

    return sum_of_digits


# - Find the sum of the squares of the first n natural numbers

def sum_of_square_of_the_first_natural_numbers(number_of_squares):
    last_square = 1
    sum_of_squares = 0

    while number_of_squares > 0:
        if int(math.sqrt(last_square)) ** 2 == last_square:
            sum_of_squares += last_square
            print(f"{last_square}----{sum_of_squares}")
            last_square += 1
            number_of_squares -= 1
        else:
            last_square += 1

    return sum_of_squares
