weight = int(input('Weight: '))
unit = input('(G)allons or (L)iters: ')
if unit.upper() == "G":
    converted = weight / 0.26417
    print(f'You are {converted} Liters')
else:
    converted = weight * 0.26417
    print(f'You are {converted} Gallons')
