# Infinite Sequences
# Generators can handle infinite sequences, generating values one at a time without running out of memory. This is useful for creating endless lists of numbers or performing on-demand calculations.

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter))  # Outputs 1
print(next(counter))  # Outputs 2


# File Reading
# When reading large files, generators enable line-by-line processing without loading the entire file into memory, making them ideal for large files.

def read_large_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line

# Example usage:
for line in read_large_file('big_file.txt'):
    process(line)  # Process each line as it’s read


# Infinite Sequences with No Limit
# Generators are also ideal for producing infinite sequences, like a continuous series of numbers.
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

infinite = infinite_sequence()
print(next(infinite))  # Outputs 0
print(next(infinite))  # Outputs 1


# Generator Expressions
# Generator expressions are like list comprehensions, but they produce a generator object instead of a list, saving memory by generating items one at a time.

squared = (x * x for x in range(10))  # Creates a generator object
print(next(squared))  # Outputs 0
print(next(squared))  # Outputs 1


# Advantages of Generators
# Memory Efficiency: They yield values on demand, making them ideal for large or infinite data sets.
# Improved Performance: Generators can run faster with large datasets by not storing all items in memory at once.
# Simplified Code: Generators make code cleaner and easier to read, especially for managing complex data flows.