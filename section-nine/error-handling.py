while True:
    try:
        # prompt user to enter age
        age = int(input('what is your age?'))
        10/age
    except ValueError:
        # if input cant be converted to an integer 
        print('please enter a number')
        continue
    except ZeroDivisionError:
        print("please enter age higher than 0")
    else:
        print('thank you!')
        break
    finally:
        print('ok, i am finally done')    
    print('can you hear me?')    
            