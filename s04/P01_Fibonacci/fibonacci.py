# Declaracion de variables en una misma linea
x, y = 0 , 1
sigue = True

while sigue:
    print(y)
    # Forma No optimizada
    #   t = y
    #   y = x + y
    #   x = t
    
    # Forma opmtimizada
    x, y = y, x + y
    sigue = True if input('¿sigue? s/n ') == 's' else False