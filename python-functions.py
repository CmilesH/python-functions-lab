# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
from unittest import result


def sum_to(num):
  i = 1
  sum = 0
  while i <= num:
    sum += i
    i += 1
  return sum

print(sum_to(6))

# 2.Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.

def largest(nums):
  return max(nums)

print(largest([10, 4, 2, 231, 91, 54]))

# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

def occurences(str1, str2):
  count = str1.count(str2)
  return count

print(occurences('fleep floop', 'e') )

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product. HINT: Review your notes on args.

def product(*args):
  result = 1
  for arg in args:
    result *= arg
  return result

print(product(4, 0.5, 5))