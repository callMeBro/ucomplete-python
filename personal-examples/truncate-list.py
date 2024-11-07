### Problem: Truncate a List until Target Length

# **Objective:**

# Create a program that continuously removes the last item from a list until its length is equal to or less than a specified target length. Use the walrus operator to check the list’s length in the loop condition.

# **Requirements:**

# 1. **Input Parameters:**
#     - Create a function `truncate_list(target_length: int, items: list)`.
#     - The function should take two arguments: `target_length` (the desired maximum length of the list) and `items` (a list of elements to truncate).
# 2. **Initial Length Check:**
#     - Check if the initial length of `items` is greater than `target_length`.
#     - If so, print a message: `"List too long with {n} elements"`, where `n` is the current length of the list.
# 3. **Truncation Loop:**
#     - Use a `while` loop to keep reducing the length of `items` by removing the last item until its length is less than or equal to `target_length`.
#     - Use the walrus operator (`:=`) to reassign the length of `items` to `n` in each loop iteration.
#     - Print the current length `n` each time an item is removed.
# 4. **Final Output:**
#     - Print the truncated list after the loop exits.



def truncate_list(target_length, items):
    # check if the of the length of the items is greater than target_length 
    # checks if items is greater than 10 and assigns items length to n at the sametime 
    if((n := len(items)) > target_length):
        # list_len = len(items)
        print(f"List too long with {n} elements")
        
        # while loop to keep reducing the length of items to n in each loop iteration
        
        
    while (n := len(items)) > target_length:
        # remove the last element from the list
        new_list = items.pop()
        print(new_list)
        # print(f"Removed {removed_item}, new length: {len(items)}")
        
    return items
        
        
# truncate_list(3, [1, 2, 3, 4, 5, 6, 7])

result = truncate_list(3, [1, 2, 3, 4, 5, 6, 7])
print("Truncated list:", result)


    
# When getting the length of the items len(items) function operates in O(1), as the length of the list is stored in n (internally)
# checking the length of list and comparing it to the target element takes O(1)

#    While Loop:
# the while loop continues to execute as long as the length of items is greater than target length
# In .pop(), it removes the last element from the list in  O(1) 

# The loop continues until the length of items is reduced to target_length. So, if the original list has n elements and the target length is k, the loop will run (n - k) times
# In each iteration, the .pop() operation is O(1), and it will be called (n - k) times.

# Space Complexity: O(n) due to the input list items.