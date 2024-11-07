# Initializing list
list_a = [12, 67, 98, 34, 43]
list_b = [10, 20, 30, 40, 50, 60]

# printing original list
print("The original list is : " + str(list_a))
 
def double_a(lst): 
# Double List using map() function
    return list(map(lambda x: x + x, list_a))

 
# function to filter out the evens returns t or f 
def even_filter_out(list_a):
    return list(filter(lambda x: x % 2 == 0, list_a))           #checks if x is even by checking if the remainder when x is divided by 2 is 0 
            
            
dl = double_a(list_a)
fl = even_filter_out(dl)

# zip the filter with list_b so each tuple has one element from the filtered list and one from list_b
zipped_list = list(zip(fl, list_b))    
        
print("Doubled list:", dl)
print("Filtered odd numbers:", fl)
print("Zipped list with list_b:", zipped_list)



# list are dynamic array thats time complexity is O(n) when accessing an element by index e.g.(list[i]), it takes constant time,  O{1}. The time complexity depends on how many elements we need to process. 

# When iterating through list size(n), all it's element (like in map(), filter(), or zip()) will take O(n) time 


# The map function applies a a given function to each element of an iterable. When processing each element exactly once the time complexity of map() is O(N), where n is the number of elements in list_a. This gives a linier time complexity, 
# as the number of operations grow with the input size 


# The filter function applies a test to each element in a list and retrns an iterable. It's time complexity is 0(n) because each element of thee list is evaluated by the lambda function. 


# The zip function combines multiple iterables into a iterator of tuples, where each tuple contains one element from each of the input iterables at the same index. This will also be O(n) because zip processes each pair of elements from the input list once. n is the number of pairs formed(which is thee length of the shortest input iterable)





