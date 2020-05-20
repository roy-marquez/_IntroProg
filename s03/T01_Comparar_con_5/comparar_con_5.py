import random

x = random.randint(0,10)
print('\nSe generó numero aleatorio "x", entre 0 y 10...')

if x == 5:
    print('\tx es igual a 5')
elif x < 5:
    print ('\tx es menor a 5')
else:
    print ('\tx es mayor a 5')

print('\t"x" es: ' + str(x) + '\n')