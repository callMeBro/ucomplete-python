# def gen_fun(num):
#     for i in range(num):
#         yield i 
        
        
# for item in gen_fun(100)        



# def special_for(iterable):
#     iterator = iter(iterable)
#     while True:
#         try: 
#             print(iterator)
#             print(next(iterator)*2)
#         except StopIteration: 
#             break 
        
        
# special_for([1,2,3])            
class MyGen():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = self.first  # Keep track of the current value inside the instance.
  
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.last:  # Now check against the instance's current value
            num = self.current
            self.current += 1  # Increment instance's current value
            return num
        raise StopIteration
    
    
    
    
    
gen = MyGen(0, 100)
for i in gen:
    print(i)
    
