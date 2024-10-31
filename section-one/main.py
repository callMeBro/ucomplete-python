name = input("What is your name? ")
print(" " + name)




# Data Types
# int
# float
# bool
# strlist
# tupleset
# dict


# Classes -> custom types

# Specialized Data Types 

# None

print(type(6))
print(type(2 - 4))
print(type(2 * 4))
print(type(2 / 4))

print(2 ** 3)
print(5 // 4)
print(6 % 4)

#math functions 

# round(3.1, ndigits)

#augmented assignment operator 
some_value = 5
some_value = some_value * 2 

# escape sequence
weather = "It\'s \"kind of \" sunny"                #every thing that comes after the backslash is a string 
print(weather)

print(len('helllood'))              #get the length of the string 

greet = 'hellloooo'
print(greet[0:8])


birth_year = input('what year were you born?')
print(type(birth_year))

age = 2024 - int(birth_year)

print(f'your age is: {age} ')


username = input('What is your username?')
password = input('What is your password?')

password_length = len(password)
hidden_password = '*' * password_length


print(f'{username}, your password, {hidden_password}, is {len(password_length)} letters long')






