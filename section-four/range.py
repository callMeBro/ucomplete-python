for _ in range(10, 0, -2):
    # range(10, 0, -2) generates a sequence of numbers starting from 10, down to 1 (exclusive),
    # decrementing by 2 on each iteration.
    # The underscore (_) is used as a variable name to indicate that the value isn't used in the loop's body.
    print(_)
    # Output will be: 10, 8, 6, 4, 2
    # The loop will print numbers 10 down to 2, decreasing by 2 in each iteratio
    
    
for _ in range(2):
    # range(2) creates a sequence [0, 1], so this loop runs twice.
    # Each time the loop runs, it creates a list using range(10),
    # which generates numbers from 0 to 9, and prints it.
    print(list(range(10)))
    # Output will be the same list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] printed twice.
