

### Problem: Find Indices of Multiples of a Number

# **Objective:**

# Create a program that finds the indices of all multiples of a given number within a range from 0 to 99. Use `enumerate()` to track the indices as you iterate through the range.

# **Requirements:**

# 1. **Input Parameters**:
#     - Create a function `find_multiples(target_number: int)`.
#     - The function should take an integer `target_number` as an argument, representing the number whose multiples you’re looking for within the range 0–99.
# 2. **Iteration and Condition**:
#     - Use `enumerate()` to iterate over the list of numbers from 0 to 99.
#     - Check if each number is a multiple of `target_number` (i.e., `num % target_number == 0`).
#     - If it is a multiple, print the index and the number.
# 3. **Function Output**:
#     - Print the indices and values of all multiples of `target_number` within the range.
#     - If `target_number` is 0, print a message saying "Cannot divide by zero".
    
def find_multiples(target_number):
    for i, char in enumerate(list(range(100))):
        # enumerate() adds a counter (i) to the iteration over the list(range(100)).
        # The list(range(100)) generates a list of numbers from 0 to 99.
        # In each iteration, `i` is the index, and `char` is the corresponding number (character) from the list.
    
        if target_number == 0:
            print("Cannot divide by zero") 
        if(char % target_number == 0):
            print(i, char)
        # This prints the index `i` and the value `char` at that index in each iteration.
    
    return "Index " + str(i) + ": " + str(char)
     # The f-string is used to display the index of the number 50.

print(find_multiples(10))    