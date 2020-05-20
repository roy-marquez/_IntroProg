#Entradas de usuario
cantidadPizzas = int(input ('Digite la cantidad de pizzas: '))
tamanoPizza = int(input('Digite el tamaño de las pizzas [Opciones: 8, 12, 16] : '))
cantidadPersonas = int(input('Digite la cantidad de personas: '))

#Calculos
porcionesTotal = cantidadPizzas * tamanoPizza
porcionesPorPersona = porcionesTotal // cantidadPersonas
porcionesDeSobra = porcionesTotal % cantidadPersonas

#Salidas
print ('Le corresponden '+ str(porcionesPorPersona) + ' porciones a cada persona.')
print ('Y sobran ' + str(porcionesDeSobra) + ' porciones despues de repartir.')
