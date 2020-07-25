from caja_lapices import *
from lapices import *

## CAJA 1
caja_eduardo = caja_lapices('Eduardo')

lapiz_rojo = Lapiz_color('rojo')
lapiz_azul = Lapiz_color('azul')

caja_eduardo.agregar_lapiz(lapiz_rojo)
caja_eduardo.agregar_lapiz(lapiz_azul)


## CAJA 2
caja_roy = caja_lapices('Roy')

lapiz_grafito = Lapiz_grafito()
lapiz_naranja = Lapiz_color('naranja')

caja_roy.agregar_lapiz(lapiz_grafito)
caja_roy.agregar_lapiz(lapiz_naranja)

print ('Mostrar contenido de las cajas')
print (caja_eduardo)
print (caja_roy)