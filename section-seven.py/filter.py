my_list = [1,2,3]
your_list = [10, 20, 30]
their_zip = (5, 4, 3)

# map, filter, zip, and reduce
def multiply_by2(item):
    return item*2

def only_odd(item):
    # check if item is odd return true or false 
    return item % 2 != 0 

# use filter on each element on the list 
print(list(filter(only_odd, [1,2,3]))),         #adds the odd numbers to the list
print(my_list)

# zip take the two iterables abd zips them together (1, 10) (2, 20) (3,30) 
print(list(zip(my_list, your_list)))
print(my_list)