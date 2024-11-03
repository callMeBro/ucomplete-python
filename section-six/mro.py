# MRO EXAMPLE
class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

# Create an instance of `D`
d_instance = D()

# Access `num` attribute
print(d_instance.num)  # Output will be 1, due to MRO

# Print the MRO of class `D`
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
