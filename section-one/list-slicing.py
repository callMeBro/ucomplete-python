#List slicing 
amazon_cart = [
    'notebook', 
    'sunglasses', 
    'toys',
    'grapes'
]


amazon_cart[0] = 'laptop'
# new_cart = amazon_cart[0:3]
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

# list unpacking
a, b, c, *first_few, d = [1, 2, 3, 4, 5] 


print(a)
print(b)
print(c)
print(first_few)
print(d)