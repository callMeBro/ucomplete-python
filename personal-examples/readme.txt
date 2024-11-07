
######################################################################################################### list-manipulation-pipeline.py ##############################################################################################################################

list are dynamic array thats time complexity is O(n) when accessing an element by index e.g.(list[i]), it takes constant time,  O{1}. The time complexity depends on how many elements we need to process. 

When iterating through list size(n), all it's element (like in map(), filter(), or zip()) will take O(n) time 


The map function applies a a given function to each element of an iterable. When processing each element exactly once the time complexity of map() is O(N), where n is the number of elements in list_a. This gives a linier time complexity, 
as the number of operations grow with the input size 


The filter function applies a test to each element in a list and retrns an iterable. It's time complexity is 0(n) because each element of thee list is evaluated by the lambda function. 


The zip function combines multiple iterables into a iterator of tuples, where each tuple contains one element from each of the input iterables at the same index. This will also be O(n) because zip processes each pair of elements from the input list once. n is the number of pairs formed(which is thee length of the shortest input iterable)


######################################################################################################### find-indices.py ##############################################################################################################################

The time complexity for this will be O(n), simply because we have to itterate ove all number(inclusively).

Inside the loop:
(num % target_number == 0), which is a constant time operations, O(1)
An append operation to the list( multiples.append(i, num)) which is also 0(1), on average for dynamic arrays 

The time operation is determind by thee loop hence O(n)





