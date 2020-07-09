#   Programa que recibe un entero positivo en base 2 (binario)
#   e imprime su equivalente en base 10 (decimal)

num_binary = input('\nDigite el número en binario: ')
num_decimal = 0

num_binary = num_binary[::-1]

for i in range (len(num_binary)):
    n = int(num_binary[i])
    num_decimal += n*(2**i)

print ('El número en base 10 es: ' + str(num_decimal) + '\n')