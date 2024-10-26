my_string = "Hello, World!"
print(my_string[0])   #Output: H
print(my_string[-1])  #Output: !

# Immutability of Strings:
# Strings in Python are immutable, meaning once they are created, their contents cannot be changed. You can't modify individual characters of a string directly.
my_string = "Hello"
# my_string[0] = "h"  # This will raise an error

# len(): Returns the length of the string.
print(len(my_string))  # Output: 13

# str.upper() / str.lower(): Converts the string to uppercase or lowercase.
print(my_string.upper())  # Output: HELLO, WORLD!

# str.strip(): Removes any leading and trailing whitespace (or specific characters).
print("  Hello  ".strip())  # Output: Hello


# str.replace(old, new): Replaces occurrences of a substring with another substring.
print(my_string.replace("World", "Everyone"))  # Output: Hello, Everyone!

# str.split(): Splits the string into a list based on a delimiter (default is whitespace).
words = my_string.split(", ")
print(words)  # Output: ['Hello', 'World!']

# str.join(): Joins elements of a list into a single string.
sentence = " ".join(words)
print(sentence)  # Output: Hello World!

#  Advanced String Indexing & Slicing:
# Step Argument in Slicing: Besides basic slicing, you can use a step argument to specify how much to increment or decrement between indices. This is useful for tasks like reversing a string or skipping characters.

my_string = "abcdef"
print(my_string[::2])  # Output: ace (every second character)
print(my_string[::-1]) # Output: fedcba (reverses the string)


# String Interpolation and F-strings: F-strings (formatted string literals) allow you to easily include expressions inside a string by using {}.
name = "John"
age = 25
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)  # Output: Hello, my name is John and I am 25 years old.


# You can even add expressions or functions directly in the f-string:
print(f"Next year, I will be {age + 1}")  # Output: Next year, I will be 26


# Immutability with Strings:
# Why Immutability Matters: When working with strings, immutability makes it more memory efficient and safe for sharing across different parts of your program. But this also means you can't modify the string in place.

# If you want to "modify" a string, you must create a new string.
old_string = "Python"
# This doesn't modify old_string, it creates a new one
new_string = old_string[:1] + "Y" + old_string[2:]
print(new_string)  # Output: PYthon

# Even though strings are immutable, lists (which are mutable) can be a workaround if you need frequent modifications:
# Convert the string to a list, modify, and convert it back to a string
char_list = list(old_string)
char_list[1] = 'Y'
modified_string = ''.join(char_list)
print(modified_string)  # Output: PYthon


# startswith() and endswith(): These functions are useful when checking prefixes or suffixes in strings.
text = "Hello, World!"
print(text.startswith("Hello"))  # Output: True
print(text.endswith("!"))        # Output: True


# find() and index(): These functions help you locate substrings within a string. The difference is that find() returns -1 if the substring isn’t found, while index() raises an error.
print(text.find("World"))  # Output: 7 (index where "World" starts)
print(text.find("Python")) # Output: -1 (not found)
# Using index() would raise a ValueError if not found
# print(text.index("Python"))  # Raises ValueError

# isalnum(), isdigit(), isalpha(): These are quick ways to check the types of characters in a string.
print("abc123".isalnum())  # Output: True (contains only letters and numbers)
print("12345".isdigit())   # Output: True (only digits)
print("abc".isalpha())     # Output: True (only letters)

# join() with complex structures: You can use join() with complex data structures like lists of lists:
word_list = ['I', 'love', 'Python']
sentence = ' '.join(word_list)
print(sentence)  # Output: I love Python

# Exploring Advanced Built-in Functions:
# sorted(): This can be used to sort characters in a string (which turns it into a list). It’s especially useful when you need to compare strings after sorting the characters.

word = "python"
print(sorted(word))  # Output: ['h', 'n', 'o', 'p', 't', 'y']
print(''.join(sorted(word)))  # Output: hnopty

# format() Method (String Formatting): While f-strings are the modern way to format strings, the format() method is still powerful and commonly used.
sentence = "The {} in the {}.".format("cat", "hat")
print(sentence)  # Output: The cat in the hat.

# Positional arguments
sentence = "The {0} in the {1}, and the {0} likes it.".format("cat", "hat")
print(sentence)  # Output: The cat in the hat, and the cat likes it.

# Keyword arguments
sentence = "The {animal} in the {object}.".format(animal="cat", object="hat")
print(sentence)  # Output: The cat in the hat.


#################################################################################################


# Lists in Python
# A list is a versatile, ordered, and mutable collection of items in Python. Lists can hold elements of different data types, including other lists (allowing you to create matrices or multi-dimensional arrays).


# Creating a list
my_list = [1, 2, 3, 4, 5]

# Adding an element
my_list.append(6)        # my_list becomes [1, 2, 3, 4, 5, 6]

# Inserting an element at a specific position
my_list.insert(1, 'a')   # my_list becomes [1, 'a', 2, 3, 4, 5, 6]

# Removing an element by value
my_list.remove('a')      # my_list becomes [1, 2, 3, 4, 5, 6]

# Removing an element by index
my_list.pop(0)           # my_list becomes [2, 3, 4, 5, 6]

# Length of a list
length = len(my_list)    # length = 5


# Slicing is a way to access parts of sequences like lists, tuples, or strings. The basic syntax is sequence[start:stop:step].

# start is the index to begin the slice (inclusive).
# stop is the index where the slice ends (exclusive).
# step is optional and determines the stride (or step) between elements.

my_list = [0, 1, 2, 3, 4, 5, 6]

# Basic slicing
slice_1 = my_list[1:4]      # [1, 2, 3] (from index 1 to 3, not including 4)

# Omitting start or stop
slice_2 = my_list[:3]       # [0, 1, 2] (from start to index 3)
slice_3 = my_list[3:]       # [3, 4, 5, 6] (from index 3 to the end)

# Negative indexing
slice_4 = my_list[-4:-1]    # [3, 4, 5] (from index -4 to -1)

# Using step
slice_5 = my_list[::2]      # [0, 2, 4, 6] (every second element)

# Reversing a list with slicing
reversed_list = my_list[::-1]  # [6, 5, 4, 3, 2, 1, 0]


# In Python, a matrix can be represented as a list of lists, where each inner list represents a row of the matrix.
# 2x3 matrix (2 rows, 3 columns)
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


# Matrix Traversal:
# You can use loops to traverse and manipulate a matrix.

# Accessing Matrix Elements:
# You can access elements of the matrix using double indexing: the first index for the row and the second for the column.
element = matrix[0][1]   # 2 (row 0, column 1)

# Modify an element
matrix[1][2] = 9         # matrix becomes [[1, 2, 3], [4, 5, 9]]


# Traversing rows
for row in matrix:
    print(row)

# Traversing elements of the matrix
for row in matrix:
    for element in row:
        print(element, end=' ')  # Output: 1 2 3 4 5 9


# Matrix Addition:
# To add two matrices element-wise, you can loop through each element and sum the corresponding elements from both matrices.

# Example: Adding two 2x3 matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_b = [
    [7, 8, 9],
    [10, 11, 12]
]

# Element-wise addition
matrix_sum = [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
# Output: [[8, 10, 12], [14, 16, 18]]

# Matrix Transposition:
# Transposing a matrix means flipping it over its diagonal, turning rows into columns and vice versa.

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

# Transpose the matrix
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# Output: [[1, 4], [2, 5], [3, 6]]


# Matrix Multiplication:
# Matrix multiplication is different from element-wise multiplication. The number of columns in the first matrix must equal the number of rows in the second matrix.
matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]

# Multiply matrix_a by matrix_b
matrix_product = [[sum(a*b for a, b in zip(matrix_a_row, matrix_b_col)) for matrix_b_col in zip(*matrix_b)] for matrix_a_row in matrix_a]
# Output: [[19, 22], [43, 50]]

# More Advanced List Slicing (Step and Negative Step)
# You can use step in slicing to skip elements or even reverse a list/matrix.

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Every second element
step_slice = my_list[::2]    # [0, 2, 4, 6, 8]

# Every third element
step_slice_3 = my_list[::3]  # [0, 3, 6]

# Reversed list
reversed_list = my_list[::-1]  # [8, 7, 6, 5, 4, 3, 2, 1, 0]


# List Comprehensions
# List comprehensions offer a concise way to create lists and matrices.
# Create a list of squares
squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]


# Create a 3x3 identity matrix
identity_matrix = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
# Output: [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


# Useful List and Matrix Functions
# len(): Returns the number of elements in a list.
# max()/min(): Returns the maximum or minimum value.
# sum(): Sums the elements of a list.
# zip(): Combines elements from multiple lists, which is useful for matrix column operations.
