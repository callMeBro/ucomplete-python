# Error Handling

# loop until user provide valid input 
while True:
    try:
        # get input from user and attempt to convert it
        age = int(input('what is your age? '))
        print(age)
    except:
        # catch the error if the input is not valid 
        print('please enter a number')   
    else: 
        # if no exception message print thank you message 
        print('thank you!')
        break      
        
# method that defines two integers                 
def sum(num1, num2):                    #should change sum to a more sutible name  
    try:
        #sum numbers
        return num1+num2
    except(TypeError, ZeroDivisionError):
        print('please enter a age higher than 0')
    else:
        print('thank you')
         
                # method that defines two integers                 



def sum(num1, num2):                    #should change sum to a more sutible name  
    try:
        #sum numbers
        return num1+num2
    except TypeError as err:
        print('please enter a age higher than 0' + err)         #err prints out the specific error 
    else:
        print('thank you')