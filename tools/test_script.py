# test_script.py

from tools.numbers.simp import add_numbers, subtract_numbers
from tools.numbers.comp import sumofdigits, ispal
from tools.col import myzip

# Test functions
result_addition = add_numbers(5, 3)
result_subtraction = subtract_numbers(10, 4)

print("Result of addition:", result_addition)
print("Result of subtraction:", result_subtraction)

result_sum_of_digits = sumofdigits(234)
result_is_palindrome = ispal(1221)

print("Sum of digits:", result_sum_of_digits)
print("Is palindrome?", result_is_palindrome)

# Test myzip function
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result_myzip = myzip(list1, list2)

# Printing the result of myzip as a list
print("Result of myzip:", list(result_myzip))
