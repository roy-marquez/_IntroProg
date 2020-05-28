#   Programa que recibe enteros del usuario los almacena en una lista
#   y los suma. Imprime la lista y el total en cada vuelta. 
#   El ciclo se repite hasta que el usuario digita cero. 

cero = False
numbers = []
i = 0
total = 0

while not cero :
    number = int(input('\nAgregue un número a la lista o digite 0 (cero) para SALIR : ' ))
    numbers.append(number)
    while i < len (numbers):
        total += numbers[i]
        i += 1
    print ('\nAsí va la lista...' + str (numbers))
    print ('La suma de todos los números de la lista es '+ str(total))
    
    if number == 0:
        cero = True
        print ('Has SALIDO del programa! \n')  