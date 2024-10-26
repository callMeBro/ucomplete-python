# iterable - list, dictionary, tuple, set, string
# In Python, an iterable is any object capable of returning its elements one at a time.
# Examples: list, dictionary, tuple, set, and string.

# iterate -> one by one check each item in the collection.
# The act of going through each element in an iterable is called iteration.

user = {
    'name': 'Golem', 
    'age': 5006,
    'can_swim': False
}
# Here, `user` is a dictionary with three key-value pairs.

# Loop through the dictionary to get both the keys and values
for key, value in user.items():
    # `.items()` method returns the dictionary’s key-value pairs.
    # key, value = item (Each iteration assigns the current key and value to the variables `key` and `value`)
    print(key, value)
    # This will print both the key and the corresponding value for each key-value pair in the dictionary.

# Loop through the dictionary to get only the values
for item in user.values():
    # `.values()` method returns only the values in the dictionary.
    print(item)
    # This will print the value for each key in the dictionary.

# Loop through the dictionary to get only the keys
for item in user.keys():
    # `.keys()` method returns only the keys in the dictionary.
    print(item)
    # This will print each key in the dictionary.
