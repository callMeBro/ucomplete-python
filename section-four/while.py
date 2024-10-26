i = 0  # Initialize the variable 'i' to 0

# Start a while loop that continues as long as 'i' is less than 50
while i < 50:
    print(i)  # Print the current value of 'i'
    i += 1  # Increment 'i' by 1 (this line won't be executed after break)
    
    # Immediately break out of the loop after the first iteration
    break

# The 'else' clause in a 'while' loop is executed if the loop finishes without hitting a 'break'
# Since we have a break inside the loop, the else block will not run
else:
    print('done with all the work')  # This will only print if the loop is completed without a break
