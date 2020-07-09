#   Programa que recibe un entero positivo en base 10 (decimal)
#   e imprime su equivalente en base 2 (binario)

num_decimal = int(input('\nDigite el número en base 10: '))
num_binary = ''

while num_decimal > 0 :
    num_binary += str(num_decimal % 2)
    num_decimal = num_decimal // 2

#   Slice de toda la cadena que inicia en -1 y va hacia atras digito a digito
print('El número en binario es: ' + str(num_binary[::-1]) + '\n' )