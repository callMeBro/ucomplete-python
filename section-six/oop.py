#   Define the PlayerCharacter class
class PlayerCharacter:
    # Class attribute, shared by all instances
    membership = True

    # Initialize instance with optional name and age attributes
    def __init__(self, name='anonymous', age=0):
        self.name = name                 # instance attribute for name
        self.age = age                   # instance attribute for age

    # Method for run action (prints "run" when called)
    def run(self):
        print('run')

    # Method to shout the character's name
    def shout(self):
        print(f'my name is {self.name}')
        
   # Class method that adds two numbers and returns a new instance of the class
@classmethod
def adding_things(cls, num1, num2):
    # Use 'cls' to create a new instance with the sum as the parameter for initialization
    return cls(num1 + num2)


# Static method that adds two numbers and returns the result
@staticmethod
def adding_things2(num1, num2):
    # Since it's a static method, it doesn't access or modify the class itself
    return num1 + num2

        
# Instantiate player1 with name 'Cindy' and age 44
player1 = PlayerCharacter('Cindy', 44)

# Instantiate player2 with default values (name='anonymous', age=0)
# player2 = PlayerCharacter()

# Print player2's name, which defaults to 'anonymous'
print(player1.name)
# print(player1.adding_things(2,3))

player3 = PlayerCharacter.adding_things(2, 3)

print(player3.age)

# print(PlayerCharacter.adding_things(2,3))
