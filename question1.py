const = int(input('const = '))
print(f'Given equation is: x + y + z = {const}')

for x in range(++const): 
    for y in range(++const):
        for z in range(++const):
            if (x + y + z == const):
               print(f'x = {x}, y = {y}, z = {z}')
               break 
