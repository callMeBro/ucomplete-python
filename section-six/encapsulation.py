# note comments generated by chatgpt code is from udemy

# Define a PlayerCharacter class
class PlayerCharacter:
    # Initialization method (constructor) to set up the name and age attributes
    def __init__(self, name, age):
        self.name = name         # Instance attribute 'name' stores the player's name
        self.age = age           # Instance attribute 'age' stores the player's age
        
# Create an instance of PlayerCharacter named 'player1' with name 'andrei' and age 100
player1 = PlayerCharacter('andrei', 100)

# Print the name and age attributes of player1
print(player1.name)              # Outputs: 'andrei'
print(player1.age)               # Outputs: 100

# Attempt to call a method 'speak' that doesn't yet exist in this class definition (will raise an error)
# player1.speak()

# Define a dictionary to represent player2 with similar structure to player1
player2 = {'name': 'andrei', 'age': 100}

# Access dictionary values (similar to attributes in a class instance)
print(player2['name'])           # Outputs: 'andrei'
print(player2['age'])            # Outputs: 100

# Expanded PlayerCharacter class with added methods

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name         # Attribute 'name' for the player's name
        self.age = age           # Attribute 'age' for the player's age
        
    # Define a 'run' method (for demonstration, it simply prints "run")
    def run(self):
        print('run')
    
    # Define a 'speak' method to introduce the player by name and age
    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old') 

# Instantiate player1 again with name 'andrei' and age 100, now with methods 'run' and 'speak' available
player1 = PlayerCharacter('andrei', 100)

# Print the name and age attributes of player1
print(player1.name)              # Outputs: 'andrei'
print(player1.age)               # Outputs: 100

# Call the speak method to output a message with player's name and age
player1.speak()                  # Outputs: 'my name is andrei, and I am 100 years old'