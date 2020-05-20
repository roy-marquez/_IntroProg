number1 = int(input('Ingrese el primer numero: '))
number2 = int(input('Ingrese el segundo numero: '))
number3 = int(input('Ingrese el tercer numero: '))

if number1 > number2:
    if number1 > number3:
        print('El primer numero es mayor ')
    else:
        print('El tercer numero es mayor ')
else:
    if number2 > number3:
        print('El segundo numero es mayor ')
    else:
        print('El tercer numero es mayor ')