""" Programa en Python que cree un set con los números compuestos del 1 al 100
    y un set con los números impares del 1 al 100.
    Usando esos dos sets, cree un tercer set (comp_even) con los números compuestos pares.
    Luego pregunte al usuario un número y búsque este número entre el set (comp_even). 
"""

composite_nums = set()
odd_nums = set()
even_nums = set()

for number in range(1,101):
    # determinar los compuestos
    divisors=0
    for i in range (1, number+1):
        if number % i == 0:
            divisors += 1
    if  divisors > 2:
        composite_nums.add(number)
    
    # determinar los impares y pares
    if number % 2 == 1:
        odd_nums.add(number)

# Para determinar los pares, se restan de 
# TODOS los numeros del 1  al 100 los impares
even_nums = set(range(1,101))
even_nums = even_nums.difference(odd_nums)

# Determinar los que sean compuestos y pares.
comp_even = composite_nums.intersection(even_nums)

# Imprimir los sets
print('\nLos numeros compuestos son: ', composite_nums)
print('\nLos numeros impares son: ', odd_nums)
print('\nLos numeros pares son: ', even_nums)
print('\nLos numeros compuestos-pares son: ', comp_even)

# Buscar el número x en el set comp_even
x = int(input('\nDigite el número a buscar: '))
if x in comp_even:
    print ('El número ' + str(x) + ', SI se encuentra en el set comp_even.')
else:
    print ('En número ' + str(x) +  ' NO se encuentra en el set comp_even.')