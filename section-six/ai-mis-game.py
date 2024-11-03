# Define a base class `User` with a `sign_in` method that all user-based classes can inherit
class User:
    def sign_in(self):
        # Method to simulate user login
        print('logged in')

# Define a subclass `Wizard` that inherits from `User`
class Wizard(User):
    def __init__(self, name, power):
        # Use `super()` to call the `User` class's init, if there is one
        super().__init__()
        # Initialize `name` and `power` attributes for the wizard
        self.name = name
        self.power = power

    # Method to simulate the wizard's attack
    def attack(self):
        # Print a statement showing the wizard's power level during the attack
        print(f'attacking with power of {self.power}')

# Define another subclass `Archer` that also inherits from `User`
class Archer(User):
    def __init__(self, name, num_arrows):
        # Use `super()` to call the `User` class's init, if there is one
        super().__init__()
        # Initialize `name` and `num_arrows` attributes for the archer
        self.name = name
        self.num_arrows = num_arrows

    # Method to simulate the archer's attack
    def attack(self):
        # Print a statement showing the number of arrows left during the attack
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

    def run(self):
        print('ran really fast')

# Define the `HybridBorg` class, inheriting from both `Wizard` and `Archer`
class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        # Call the `__init__` methods of both parent classes using `super()`
        super().__init__(name, power)
        self.num_arrows = num_arrows  # Unique attribute for `Archer` is set separately

    # Override the attack method to combine both Wizard and Archer attacks
    def attack(self):
        print(f'Hybrid attack with power of {self.power} and {self.num_arrows} arrows')

# Create an instance of `HybridBorg` with a name, power, and number of arrows
hb1 = HybridBorg("borgie", 50, 100)

# Call the `sign_in()` method from the `User` class
hb1.sign_in()  # Output: 'logged in'

# Call the `attack()` method from the `HybridBorg` class
hb1.attack()   # Output: 'Hybrid attack with power of 50 and 100 arrows'
