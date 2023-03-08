import unittest
from math_functions import Exercises


class TestMathFunctions(Exercises, unittest.TestCase):
    def test_area_function(self):
        assert self.circle_area(2) == 12.566370614359172
        assert self.circle_area(0) == 0

    def test_factorial_of_a_number_function(self):
        assert self.factorial_of_a_number(6) == 720
        assert self.factorial_of_a_number(0) == 1

    def test_maximum_of_3_numbers_function(self):
        assert self.maximum_of_3_numbers(1, 1, 1) == 1
        assert self.maximum_of_3_numbers(1, 10, 3) == 10
        assert self.maximum_of_3_numbers(1, -10, 3) == 3

    def test_check_if_number_is_prime_function(self):
        assert self.check_if_number_is_prime(5)
        assert not self.check_if_number_is_prime(6)

    def test_get_fibonacci_sequence_function(self):
        assert self.get_fibonacci_sequence(0) == []
        assert self.get_fibonacci_sequence(1) == [0]
        assert self.get_fibonacci_sequence(2) == [0, 1]
        assert self.get_fibonacci_sequence(5) == [0, 1, 1, 2, 3]

    def test_sum_of_2_numbers_function(self):
        assert self.sum_of_2_numbers(-4, 5) == 1
        assert self.sum_of_2_numbers(0, 5) == 5

    def test_avg_for_a_list_of_numbers_function(self):
        assert self.avg_for_a_list_of_numbers([-4, 7, 6]) == 3
        assert self.avg_for_a_list_of_numbers([0]) == 0

    def test_check_if_a_number_is_even_function(self):
        assert self.check_if_a_number_is_even(6)
        assert not self.check_if_a_number_is_even(3)

    def test_get_largest_number_in_a_list_function(self):
        assert self.get_largest_number_in_a_list([2, -4, 1, 6]) == 6
        assert self.get_largest_number_in_a_list([1, 5, 5, 1]) == 5
        assert self.get_largest_number_in_a_list([9]) == 9

    def test_get_smallest_number_in_a_list_function(self):
        assert self.get_smallest_number_in_a_list([2, -4, 1, 6]) == -4
        assert self.get_smallest_number_in_a_list([1, 5, 5, 1]) == 1
        assert self.get_smallest_number_in_a_list([9]) == 9

    def test_check_if_a_number_is_perfect_square_function(self):
        assert self.check_if_a_number_is_perfect_square(9)
        assert not self.check_if_a_number_is_perfect_square(10)

    def test_sum_of_digits_of_a_number_function(self):
        assert self.sum_of_digits_of_a_number(1232) == 8
        assert self.sum_of_digits_of_a_number(-1042) == 7
        assert self.sum_of_digits_of_a_number(-3) == 3

    def test_check_if_a_number_is_palindrome_function(self):
        assert self.check_if_a_number_is_palindrome(12321)
        assert self.check_if_a_number_is_palindrome(-121)
        assert not self.check_if_a_number_is_palindrome(1232)

    def test_distance_between_2_points_function(self):
        assert self.distance_between_2_points(1, 2, 5, 10) == 8.94427190999916
        assert self.distance_between_2_points(-3, 2, -2, 12) == 10.04987562112089
        assert self.distance_between_2_points(1, 1, 1, 1) == 0

    def test_sum_of_first_n_natural_numbers_function(self):
        assert self.sum_of_first_n_natural_numbers(0) == 0
        assert self.sum_of_first_n_natural_numbers(1) == 1
        assert self.sum_of_first_n_natural_numbers(10) == 55

    def test_sum_of_the_digits_of_a_number_until_is_single_digit_function(self):
        assert self.sum_of_the_digits_of_a_number_until_is_single_digit(1234) == 9
        assert self.sum_of_the_digits_of_a_number_until_is_single_digit(-43232) == 10
        assert self.sum_of_the_digits_of_a_number_until_is_single_digit(9) == 0

    def test_sum_of_square_of_the_first_natural_perfect_square_numbers_function(self):
        assert self.sum_of_square_of_the_first_natural_perfect_square_numbers(5) == 55
        assert self.sum_of_square_of_the_first_natural_perfect_square_numbers(1) == 1
        assert self.sum_of_square_of_the_first_natural_perfect_square_numbers(0) == 0


if __name__ == '__main__':
    unittest.main()
