from functools import reduce

my_list = [1,2,3]


# map, filter, zip, and reduce

# function to multiply the items by two
def multiply_by2(item):
    return item*2

# function to return true for  numbers
def only_odd(item):
    # check if item is odd return true or false 
    return item % 2 != 0 

# accumulaor function for reducing a List
def accumulator(acc, item):
    print(acc, item)
    return acc + item
    
    
# use filter on each element on the list 
# using reduce to sum all elements in my_list, starting from 0
print(reduce(accumulator, my_list, 0)),        
print(my_list)


# exampple zip usage
# zip take the two iterables abd zips them together (1, 10) (2, 20) (3,30) 
your_list = [10, 20, 30]
print("Zipped list:", list(zip(my_list, your_list)))  # Output: [(1, 10), (2, 20), (3, 30)]
print("Original list after zip:", my_list)  # Output: [1, 2, 3]