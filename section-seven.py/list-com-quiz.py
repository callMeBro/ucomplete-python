#note comments generated by chatgpt code is from udemy
# Initial list with some duplicate values
some_list = ['a', 'b', 'c', 'd', 'm', 'n', 'n']

# Empty list to store duplicates
duplicates = []

# Iterate over each value in the list
for value in some_list:
    
    # Check if the current value appears more than once in the list
    if some_list.count(value) > 1:
        
        # If the value is not already in the 'duplicates' list, add it
        # This ensures that each duplicate is added only once
        if value not in duplicates:
            duplicates.append(value)

# Print the final list of duplicates
print(duplicates)


my_list4 = [num**2 for num in some_list if some_list.count(value) > 1 if value not in duplicates and not duplicates.append(num)]

# num ** 2: Squares each duplicate number.
# some_list.count(num) > 1: Checks if the number appears more than once in the list.
# num not in duplicates: Ensures each duplicate is only added once to duplicates_squared.
# not duplicates.append(num): Ensures duplicates is updated with new duplicates while preserving the list comprehension structure.