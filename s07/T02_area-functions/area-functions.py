# Cree un programa en Python que tenga funciones para calcular el área de  las siguientes figuras geométricas: Círculo, Cuadrado, Rectángulo, Triángulo.
# La función del área del cuadrado y el rectángulo debe ser la misma, con el segundo parámetro para calcular el rectángulo opcional.
# Debe ser interactivo de manera que el usuario use un menú donde pueda escoger qué quiere calcular.
import math

def area_circle(radius):
    """ Devuelve el área de un circulo a partir en su radio """
    return math.pi*(radius**2)

def area_quad(side1, side2=0):
    """Devuelve el área del cuadrilatero. Si sólo se ingresa un parámetro,
    devuelve el área el un cuadrado"""
    if side2==0:
        return side1**2
    else:
        return side1 * side2
        
def area_triangle(base, height):
    """Devuelve el área de un triangulo"""
    return (base * height) / 2

def menu():
    print('\n=============== Menu =============== \n ')
    print("MENU: Calcular área de: ")
    print("\t[1] CIRCULO ")
    print("\t[2] CUADRADO ")
    print("\t[3] RECTANGULO ")
    print("\t[4] TRIANGULO ")
    print("\t[5] SALIR... ")
    option = int(input("Digite opción de 1 a 5: "))
    if option >= 1 and option <= 5:
        return option
    else:
        print('Opción NO válida, 1 a 5 por favor.')
        return menu()

exit = False
while not exit:
    option = menu()
    if option == 1:
        print('\nCalculando Area de CIRCULO...\n')
        radius = int(input('Digite el RADIO del circulo: '))
        print ('El área del circulo es: ', area_circle(radius))
    elif option == 2:
        print('\nCalculando Area de CUADRADO...\n')
        side = int(input('Digite el LADO del cuadrado: '))
        print ('El área del cuadrado es: ', area_quad(side))
    elif option == 3:
        print('\nCalculando Area de RECTANGULO...\n')
        side1 = int(input('Digite el LARGO del rectangulo: '))
        side2 = int(input('Digite el ANCHO del rectangulo: '))
        print ('El área del rectangulo es: ', area_quad(side1, side2))
    elif option == 4:
        print('\nCalculando Area de TRIANGULO...\n')
        base = int(input('Digite la BASE del triangulo: '))
        height = int(input('Digite la ALTURA del triangulo: '))
        print ('El área del triangulo es: ', area_triangle(base, height))
    elif option == 5:
        exit = True