# Decorator

def hello(func):
    print("Helloo")
    
    
# function that takes another function as an argument    
def my_decorator(func):
    # define inner function
    def wrap_func(x):
        print('********')
        func(x)
        print('********')
    return wrap_func                #return function     


# apply the decorator
# Under the hood this is exuivalent to hello = my_decorator(hello)
@my_decorator
def hello(greeting):
    print(greeting)
    
# When hello() is called, it actually calls wrap_func() because hello has been replaced by wrap_func.
hello("hiii")



# Using my_decorator Without @ Syntax
def bye():
    print('see ya later')
    
hello2 = my_decorator(hello)
hello2()        