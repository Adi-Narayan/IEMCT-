print("Input a linear equation with 3 variables")
const = int(input('const = '))
print(f'Given equation is: x + y + z = {const}')

for x in range(++const):
    z = 0
    y = 0
    for y in range(++const):
        z = 0
        for z in range(++const):
            if (x + y + z == const):
               print(f'x = {x}, y = {y}, z = {z}')
               break
            z += 1
        y += 1    
    x += 1  
