# def hello():
#     print('hellooo')
    
# greet = hello()
# del hello

# print(greet)    


# Python is smart enough to know even if you delete hello it will delete hello but keep the function 
# decorators are only possible because of python method being first class 
def greet():
    print('still here')
    
def hello(func):
    func()
    
a = hello(greet)

print()    
