# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write('hey it\' me!')
#     print(my_file.readlines())                     


with open('test.txt', mode='w+') as my_file:
    my_file.write("hey it's me!")   # Write to the file
    my_file.seek(0)                 # Move cursor back to the start of the file
    print(my_file.readlines())      # Read all lines from the file
