weight = int(input('Weight: '))
unit = input('(G)allons or (L)iters: ')
if unit.upper() == "G":
    converted = weight * 3.79
    print(f'You are {converted} Liters')
else:
    converted = weight / 3.79
    print(f'You are {converted} Gallons')
