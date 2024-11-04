# first class functions
def multiply_by2(list):
    #create empty list
    new_list = []
    # loop over list and append items 
    for item in list:
        new_list.append(item*2)
        
    return new_list    
    
    
print(multiply_by2([1,2,3]))    