"""
Question : c) Write a Python program to find the largest number in a list without
using built-in functions.
"""
numbers = [10, 25, 5, 40, 15]
largest = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i = i + 1
print(largest)
