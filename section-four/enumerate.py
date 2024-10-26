# Loop through the enumerated list of numbers from 0 to 99.
for i, char in enumerate(list(range(100))):
    # enumerate() adds a counter (i) to the iteration over the list(range(100)).
    # The list(range(100)) generates a list of numbers from 0 to 99.
    # In each iteration, `i` is the index, and `char` is the corresponding number (character) from the list.
    
    print(i, char)
    # This prints the index `i` and the value `char` at that index in each iteration.
    
    if char == 50:
        # When the value of `char` is equal to 50, print the index `i`.
        print(f'index of 50 is: {i}')
        # The f-string is used to display the index of the number 50.
