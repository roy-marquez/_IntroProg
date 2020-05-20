# Imprime los numeros enteros pares entre dos numeros 
# a y b, ingresados por el usuario, a y b incluidos
# puede recibir float pero los redondea hacia abajo

a = int(float (input('ingrese primer numero: ')))
b = int(float (input('ingrese segundo numero: ')))
even_nums = ''

if a > b:
    a,b = b,a

even_nums = '\nLos numeros pares entre ' + str(a) + ' y ' + str(b) + ' son: '

while a<=b: 
    if a % 2 == 0:
        even_nums += str(a) + ' '
    a += 1
print (even_nums, '\n')