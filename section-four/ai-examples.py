# default parameters are commonly used in place of overloaded functions, as Python does not support function overloading in the same way that languages like C++ or Java do
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Alice"))          # Output: Hello, Alice!
print(greet("Bob", "Hi"))      # Output: Hi, Bob!

# This approach allows you to call the same function with different numbers of arguments, and 
# it is the typical way of handling different argument scenarios in Python. Additionally,
# Python supports variable-length arguments using *args and **kwargs, which can also give 
# similar flexibility to function calls.



# In Python, *args and **kwargs allow functions to accept a variable number of arguments.

# *args lets you pass a variable number of positional arguments to a function.
# **kwargs lets you pass a variable number of keyword arguments (like a dictionary) to a function.
def my_function(*args, **kwargs):
    # *args will be a tuple of all positional arguments
    for i, arg in enumerate(args, start=1):
        print(f"Positional argument {i}: {arg}")
    
    # **kwargs will be a dictionary of all keyword arguments
    for key, value in kwargs.items():
        print(f"Keyword argument '{key}': {value}")

# Calling the function with variable arguments
my_function(10, 20, 30, name="Alice", age=25, location="Wonderland")


# OUTPUT
# Positional argument 1: 10
# Positional argument 2: 20
# Positional argument 3: 30
# Keyword argument 'name': Alice
# Keyword argument 'age': 25
# Keyword argument 'location': Wonderland



# DOCSTRINGS
def greet(name):
    """
    This function greets the person whose name is passed as an argument.

    Parameters:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"



print(greet.__doc__)
help(greet)