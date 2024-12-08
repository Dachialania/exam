#1. Create a function that takes a list of numbers and returns the sum of all positive numbers.

# def sum_of_positive(numbers):
#     total = 0
#     for num in numbers:
#         if num > 0:
#             total += num
#         return total
# print(sum_of_positive([-1, -2, -3, -4]))


#2. Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.



# def sum_of_positive_number(numbers):
#     total = 0
#     for num in numbers:
#         if num > 0:
#             total += num // 1 
#     return total

# numbers = [-1.5, 2.7, -3.3, 4.8]
# result = sum_of_positive_number(numbers)
# print(result)



#3. Create a function to find the missing number in a list of integers from 1 to n.

# def find_missing_number(number,n):
#     sum1 = n * (n + 1) // 2
#     sum2 = sum(number)
#     return sum1 - sum2 
# number = [1, 2, 4, 5]
# n = 5
# number2 = find_missing_number(number, n)
# print(number2)



#4.Create a function that finds the length of the longest substring without repeating characters.
# def length_of_longest_substring(m):
#     longest = 0
#     substring = " "

#     for char in m:
#         if char not in substring:
#             substring += char
#     else:
#         substring =