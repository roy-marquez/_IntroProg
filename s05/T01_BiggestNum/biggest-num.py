#   Programa que recibe una lista de enteros y busca el mayor de ellos.
#   Si el usuario digita 'z' termina el programa

numbers = []
end = False # bandera de fin de programa.
bnum = None #biggest number


while not end:
    userInput = input('Ingrese un numero a la lista o \'z\' para finalizar: ')
    if  userInput == 'z':
        end = True
    else: 
        numbers.append(int(userInput))
    print ('\nAsí va la lista: ' +str(numbers))

    bnum = numbers [0]
    i = 0
    while i < len (numbers):
        if numbers [i] > bnum:
            bnum = numbers [i]
        i += 1
    print ('El numero mayor dentro de la lista es: '+ str(bnum)+'\n')
print ('Fin del programa!!\n')