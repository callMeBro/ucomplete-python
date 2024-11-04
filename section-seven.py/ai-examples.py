# Lambda functions in Python are small, anonymous functions defined with the lambda keyword. They are useful when you need a simple function for a short period, often as an argument to other functions. Lambda functions are typically single-line expressions that perform a specific task.

# lambda arguments: expression


# lambda is the keyword that indicates it’s a lambda function.
# arguments are the parameters the function takes (they can be zero or more).
# expression is the operation or computation performed and returned by the lambda function.


add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15


def add_ten(x):
    return x + 10


numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]


numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # Output: [1, 3, 5]


pairs = [(1, 2), (3, 1), (5, 0)]
# Sort pairs by the second element in each tuple
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(5, 0), (3, 1), (1, 2)]


# Anonymous: Lambda functions don’t have names, hence "anonymous."
# Single Expression: They’re limited to a single expression (though you can sometimes use multiple expressions with tricks, it’s not recommended for readability).
# Return Implicit: Lambda functions return the result of their expression automatically.
# When to Use Lambda Functions
# Lambda functions are great for short, simple operations that you want to use once or within higher-order functions like map(), filter(), and sorted(). However, for more complex operations, it’s often better to use a regular def function for readability and reusability.