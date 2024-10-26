def highest_even(myList = [], *args):
    # Avoid using mutable default arguments; set myList to an empty list if None
    if myList is None:
        myList = []
        
        
    highest_two=0
    for x in myList:
        # find the multiples of 2 and store in variable
         if x % 2 == 0 and x > highest_two:
            highest_two = x

    return highest_two if highest_two != 0 else None  # Return None if no even number is found

        
print(highest_even([10,2,3,4,8,11]))



# def highest_even(li):
#     evens = []
#     for item in li:
#         if item % 2 == 0:
#             evens.append(item)
#     return max(evens)

# print(highest_even([2,10,2,3,4,8,11]))    