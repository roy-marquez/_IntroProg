""" Práctica de funciones. """

def imperial_to_cm(mi=0, yd=0, ft=0, inc=0):
    """ Convierte valores del sistema imperial a centímetros """
    INCH = 2.54
    cms = inc * INCH
    cms += ft * 12 * INCH
    cms += yd * 36 * INCH
    cms += mi * 63360 * INCH
    return cms

#Ejemplos de uso
resultado = imperial_to_cm(2, 4, 2, 7)
print('2 mi, 4 yd, 2 ft, 7 in equivalen a: '+ str(resultado) + ' cms')

resultado = imperial_to_cm(inc=4)
print('4 in equivalen a: '+ str(resultado) + ' cms')

resultado = imperial_to_cm(yd=4, mi=2)
print('2 mi, 4 yd equivalen a: '+ str(resultado) + ' cms')