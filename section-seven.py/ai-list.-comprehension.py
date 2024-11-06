# List comprehension is a concise way to create lists in Python using a single line of code. It combines the process of iterating over an iterable (like a list, range, or other sequence) and applying a transformation or condition into a compact syntax. List comprehensions are often more readable and efficient than using loops to build lists.

# Basic Syntax
# The basic syntax for list comprehension is:

# [expression for item in iterable if condition]


# expression: The operation to apply to each item.
# item: The current element from the iterable.
# iterable: The sequence or collection you are iterating over.
# if condition (optional): A filter to include only certain items.


# Example 1: Creating a Simple List
# Let's say you want a list of squares of numbers from 0 to 9. Instead of using a for loop, you can do:
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# This is equivalent to:

squares = []
for x in range(10):
    squares.append(x**2)


# Example 2: Using a Condition in List Comprehension
# You can add a condition to filter items. For example, if you only want the squares of even numbers:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]


# Example 3: Applying a Transformation
# List comprehension can also apply transformations. For example, converting each word in a list to uppercase:
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']


# Example 4: Nested List Comprehension
# List comprehension can also handle nested lists (2D lists). For example, flattening a list of lists:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Example 5: Using Multiple Conditions
# You can add multiple conditions if needed. For example, getting squares of even numbers that are less than 50:
filtered_squares = [x**2 for x in range(10) if x % 2 == 0 and x**2 < 50]
print(filtered_squares)  # Output: [0, 4, 16, 36]


# Key Points to Remember
# Concise: List comprehension creates lists in a single line, making the code more readable.
# Readable: Often easier to understand than loops when used for straightforward list transformations.
# Fast: List comprehensions are generally faster than traditional for loops, as they’re optimized for these operations in Python.
# When to Use List Comprehension
# Use list comprehension when you need to create a new list by applying a transformation or filtering items from an existing iterable. However, if the logic is too complex, using a for loop might be more readable.