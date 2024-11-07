# height order function
def greet(func):
    func()
        
def greet2():  
    def func():
        return 5  
    return func 


# a higher order function is a function that acepts a function a parameter or returns a function eg. map, filter, reduce 