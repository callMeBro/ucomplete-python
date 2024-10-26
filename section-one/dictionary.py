#Dictionary 
dict = {
    'a':[1,2,3],
    'b':2
}, {
    'a':[1,2,3],
    'b':2
}, {
    'a':[1,2,3],
    'b':2,
    'c':3
}

print(dict["a"])
print(dict)
print(dict['a'][1])


# A dictionary is an unordered collection of items. Each item is a key-value pair, where a key maps to a value.
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Dictionaries are defined using curly braces {}
# In the example above, "name", "age", and "city" are keys, while "Alice", 25, and "New York" are values.

# create empty dictionary
empty_dict = {}

# use dict() construcyor to create dictionary 
my_dict = dict(name="Alice", age=25, city="New York")


#Access value by referencing corresponding keys 
name = my_dict["name"]  # Output: 'Alice'


# If you try to access a key that doesn’t exist, Python raises a KeyError. To avoid this, use the get() method.
age = my_dict.get("age")  # Output: 25
gender = my_dict.get("gender", "Not Specified")  # Output: 'Not Specified'


# You can add or update values by assigning a value to a key.
my_dict["age"] = 26  # Updates 'age'
my_dict["country"] = "USA"  # Adds a new key-value pair

# Use pop() to remove an item and return its value.
age = my_dict.pop('age')


# You can also use del to remove a key-value pair without returning the value.
del my_dict["city"]  # Deletes the 'city' key

# To remove the last key-value pair, use popitem().
last_item = my_dict.popitem()  # Removes and returns ('country', 'USA')


# You can check if a key exists using the in operator.
if "name" in my_dict:
    print("Name is in the dictionary")



# keys(): Returns a view of the dictionary’s keys.
# values(): Returns a view of the dictionary’s values.
# items(): Returns a view of key-value pairs (tuples).

for key in my_dict:
    print(key, my_dict[key])  # Prints each key-value pair

# Or iterate over both keys and values:
for key, value in my_dict.items():
    print(f"{key}: {value}")

# You can merge two dictionaries using the update() method, or with Python 3.9+, use the | operator.
dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
dict1.update(dict2)  # Merges dict2 into dict1

# In Python 3.9+:
merged_dict = dict1 | dict2  # Combines the dictionaries


# You can create a dictionary using dictionary comprehension, similar to list comprehension.
squared_numbers = {x: x**2 for x in range(5)}  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Dictionaries can contain other dictionaries (or any other data type).
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# Accessing nested values:
name = nested_dict["person1"]["name"]  # Output: 'Alice'

# Dictionaries are implemented using hash tables, which makes lookups very efficient (average time complexity O(1) for most operations).
# You can check the size of a dictionary using len().
size = len(my_dict)  # Output: 2

# Copying Dictionaries
# Shallow Copy: Use the copy() method

new_dict = my_dict.copy()  # Creates a shallow copy


# Deep Copy: Use the copy.deepcopy() method to recursively copy nested dictionaries.
import copy
deep_copy_dict = copy.deepcopy(nested_dict)

# A special kind of dictionary is defaultdict from the collections module. It provides a default value for missing keys.
from collections import defaultdict

# Creating a defaultdict with int, so missing keys have a default value of 0
default_dict = defaultdict(int)
default_dict["a"] += 1  # Output: {'a': 1}

