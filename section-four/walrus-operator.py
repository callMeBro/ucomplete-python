
# Checks if the length of 'a' is greater than 10 and assigns the length to 'n' at the same time
if ((n := len(a)) > 10):
    print(f"too long {n} elements")

# Continuously reduces the length of 'a' until only one character is left
while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]  # Removes the last character from 'a'

print(a)
