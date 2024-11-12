# Example of a pure, stateless function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
# We could run square() on each element concurrently without any risk of conflict
squared_numbers = list(map(square, numbers))  # Returns [1, 4, 9, 16, 25]


# Since square(x) doesn’t depend on or alter any external state, each element in numbers can be processed independently. This allows each calculation to be executed in parallel safely, as no function call affects another