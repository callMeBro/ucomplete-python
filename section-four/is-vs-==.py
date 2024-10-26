print(True is True)  
# This checks if both "True" literals point to the same object in memory.
# Output: True
# Since "True" is a singleton object in Python, both instances of "True" are the same object in memory.

print('1' is '1')  
# This checks if the string '1' refers to the same object in memory.
# Output: True
# Small strings in Python are cached, so both '1' literals point to the same object in memory.

print(10 is 10)  
# This checks if the integer 10 refers to the same object in memory.
# Output: True
# Python caches small integers (from -5 to 256), so both 10 literals refer to the same object.

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  
# This checks if the contents of lists a and b are equal (value comparison).
# Output: True
# "==" compares the values of both lists, and since the elements in both lists are the same, the result is True.
