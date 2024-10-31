# Define the PlayerCharacter class
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

# Instantiate player1 with name 'Cindy' and age 44
player1 = PlayerCharacter('Cindy', 44)

# Instantiate player2 with default values (name='anonymous', age=0)
player2 = PlayerCharacter()

# Print player2's name, which defaults to 'anonymous'
print(player2.name)
