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
