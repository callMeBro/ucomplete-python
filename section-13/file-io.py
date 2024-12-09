# my_file = open('test.txt')

# print(my_file.read())


# Use __file__ to Get the Script’s Directory
# Use __file__ to construct a path that’s always relative to the script’s location. This avoids issues with different working directories
import os
my_file_path = os.path.join(os.path.dirname(__file__), 'test.txt')
my_file = open(my_file_path)
print(my_file.read())

