#   Programa que aplica una serie de funciones
#   a una lista de nombres de amigos.
names = []
end = False # fin de ingreso de nombres

print ('\nHola, ingresa una lista de tus mejores amigos. Usar sólo minúsculas porfa!')
while not end:
    userInput = input('Agregar nombre o digita \'z\' para finalizar: ')
    if  userInput == 'z':
        end = True
    else: 
        names.append(userInput)

print('\nAsí va la lista: ', names)

if len(names) > 0:
    # Imprimir la lista ordenada ascendentemente 
    names.sort()
    print('\nLa lista en orden Alfabetico Ascendente queda así: ')
    i = 0
    while i < len(names):
        print ('\t'+ str(i+1) + '.' + names[i])
        i+=1

    # Ordenar la lista descendente 
    names.sort(reverse = True)
    print('\nLa lista en orden Alfabetico Descendente queda así: ')
    i = 0
    while i < len(names):
        print ('\t'+ str(i+1) + '.' + names[i])
        i+=1
    names.sort()

    #Buscar a amigos llamados Juan
    juan = names.count("juan")
    if juan > 0 :
        print('\nTienes ' + str(juan) + ' amigo(s) llamado(s) Juan' )
    else:
        print('\nNo tienes amigos llamados Juan')

    # Sacar a alguien de la lista
    print('\nPara SACAR a alguien de la lista (Ascendente) digita su numero, ')
    pop_name = int(input('O bien digita 0 (cero) si no deseas sacar a nadie: '))

    if pop_name >= 1 and pop_name < len(names):
        names.pop(pop_name-1)
    elif pop_name == 0: 
        print('\nElegiste Cero, la lista queda igual...')
    else:
        print('\nLa opción ' + str(pop_name) + ' no es válida. ')

    print ('\nOK la lista definitiva queda así: ')
    i = 0
    while i < len(names):
        print ('\t'+ str(i+1) + '.' + names[i])
        i+=1
else:
    print('\nLista Vacía!')

print('\n --> fin del programa <--')