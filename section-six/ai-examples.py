# @classmethod
# A @classmethod method takes a reference to the class itself as its first argument, typically named cls.
# This allows it to access and modify class-level attributes, which are shared across all instances of the class.
# @classmethod is useful when you want to define a method that should affect the class as a whole rather than an individual instance.
class PlayerCharacter:
    # Class attribute
    membership = True
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def create_with_default_age(cls, name):
        # Accesses the class (cls) and returns an instance with age 18
        return cls(name, 18)

# Use the class method to create an instance with a default age
player = PlayerCharacter.create_with_default_age("Alice")
print(player.name)  # Output: Alice
print(player.age)   # Output: 18




# @staticmethod
# A @staticmethod method does not take any implicit first argument like self or cls.
# It behaves like a regular function but is accessible from within the class namespace.
# @staticmethod is used when you want a method that belongs to the class logically but doesn’t need to access or modify class-level or instance-level data.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Call the static method without creating an instance
result = MathUtils.add(5, 3)
print(result)  # Output: 8

# ____________________________________________________________________________________________________________________________________________________________________________

# Encapsulation in Action
# Here’s how encapsulation works to control access:

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # update balance securely
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid deposit amount."

    def get_balance(self):
        return f"{self.owner}'s balance: ${self.__balance}"  # provide controlled access

# Create account and make deposit
account = BankAccount("Alice", 100)
print(account.deposit(50))         # Deposited $50. New balance: $150
print(account.get_balance())        # Alice's balance: $150


########################################################################################################################################################################

# class that uses some dunder methods

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)

# Create two vector instances
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# Print the vector
print(v1)             # Output: Vector(2, 3)

# Add two vectors
v3 = v1 + v2
print(v3)            # Output: Vector(6, 8)

# Get the length of a vector
print(len(v1))      # Output: 3

# Dunder methods are an essential part of Python's object-oriented programming, 
# enabling you to define how objects behave in different contexts. By implementing 
# these methods, you can make your custom classes more powerful and user-friendly, taking advantage of Python's built-in functionality.