# Cree un programa de Python con un menú interactivo con las opciones:
# *La hora
# *El día del mes
# *El día de la semana
# *El mes
# *El año
# *Salir

from datetime import datetime
import time
import locale

# Idioma "es-ES" (código para el español de España)
locale.setlocale(locale.LC_ALL, 'es-ES') 
dt = datetime.now()

def hora_actual(formato='12'):
    if formato =='12':
        return (dt.strftime("%I:%M:%S"))
    elif formato == '24':
        return (dt.strftime("%H:%M:%S"))
    else :
        return (dt.strftime("%H:%M:%S"))

def dia_del_mes():
    return dt.strftime('%d')

def dia_de_semana():
    return dt.strftime('%A')

def mes(formato='txt'):
    if formato=='num':
        return dt.strftime('%m')
    elif formato == 'txt':
        return dt.strftime('%B')

def anno():
    return dt.strftime('%Y')
def menu()
    print('''\n=============== Menu =============== \n
    Seleccione una opción
    \t1. Hora Actual
    \t2. El día del mes
    \t3. El día de la semana
    \t4. El mes
    \t5. El año
    \t6. SALIR!
    ''')  
    opcion = input("Digíte una opción: ")
    
    #Selecciona solo digitos numericos por medio de valores ascii
    if len(opcion) == 1:
        opt = ord(opcion)
        if opt >= 49 and opt<= 54:
            return opt
        else:
            print ('\n>>> ERROR! OPCION NO VALIDA.\n')
            menu()
    else:
        print ('>>> ERROR!, FAVOR DIGITE UN DIGITO NUMERICO')
        menu()

def main():
    opt = menu()
    while opt != 54:
        if opt == 49:
            print ('\tLa hora actual es: ' + hora_actual())
            print ('\tEn formato 24h son las: ' + hora_actual('24'))
        elif opt == 50:
            print('\tHoy es el día ' + dia_del_mes() + ' del mes')
        elif opt == 51:
            print ('\tEl día de la semana es: '+ dia_de_semana())
        elif opt == 52:
            print('\tEstamos en el mes de ' + mes() + ' equivalente al mes ' + mes('num') + ' del año.')
        elif opt == 53:
            print('\tEstamos en el año ' + anno())
        else:
            print('\tOops, algo salió mal...')
        opt = menu()
    print ('\n\t >>> Fin del programa <<< \n')
main()