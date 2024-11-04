from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
# create new_empty list
capitalized_list = []

# loop through pet names 
capitalized = [a.upper() for a in my_pets]

print(capitalized)    
    
#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
# my_numbers = my_numbers.sort

# zip usage
your_list = [10, 20, 30]
print("Zipped list:", list(zip(my_strings, sorted(my_numbers))))  
print("Original list after zip:", my_strings) 

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

j2 = [i for i in scores if i > 50]
# j2.sort()
print(j2)


