#Square
my_list = [5, 4, 3]


# write a lambda expression that print a squared list 
my_list = [5, 2, 3]
my_list.sort(lambda x: x**2, my_list)

print()

#List Sorting sort in asending order based on the second value of the tuple 
a = [(0,2), (4,3), (9,9), (10, -1)]
a.sort(key=lambda x: x[-1])             #note tutorial use one instead one instead of -1 can cause errors when not exaply 2 element in the list and we want to return the last      
print(a)