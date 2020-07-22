from user_interface import *
from data import courses



# print( 'Acualizar id_num: ', prop_update('id_num'))
# print( 'Acualizar nombre: ', prop_update('nombre'))
# print( 'Acualizar email: ', prop_update('email'))
# print( 'Acualizar curso: ', prop_update('curso'))

def option_menu(literal=''):
    '''Despliega las opciones de mantenimientos disponibles y devuelve int '''
    print('''\n=============== Mantenimiento {0} =============== \n
    Seleccione una opción:
    \t1. Crear {0}
    \t2. Consultar {0}
    \t3. Actualizar {0}
    \t4. Eliminar {0}
    \t5. Imprimir lista.
    \t6. SALIR!
    '''.format(str(literal)))  
    
    option = input("Digíte una opción: ")
    
    #Selecciona solo caracter numericos por medio de valores ascii
    if len(option) == 1:
        opt = ord(option)
        if opt >= 49 and opt<= 54:
            return int(option)
        else:
            print ('>>> ERROR OPCION NO VALIDA')
            return option_menu(literal)

#print(option_menu('profesor'))

menu_options = [
    'Crear', 
    'Consultar',
    'Actualizar',
    'Eliminar',
    'Salir'
]



#print (get_option_from(menu_options, "Mantenimiento Profes!"))
#print(new_title('*', 100, '*', True ))
'''
print(new_title('Mantenimiento de estudiantes', 60, '=', True))

print(new_title('Titulo corto', 60, '*', True))

print(ask_id())

#print(ask_course())
'''
letras = {'A', 'B', 'C', 'D'}
letras_copy = letras.copy()


# print('Imprimiento letras', letras)
# print('Se eliminó {} de letras'.format(letras.pop()))
# print('Imprimiento letras', letras)

# print ('Imprimiendo letras_copy', letras_copy)
print('Seleccion de Grouo_id >> ')
print(ask_letter(letras))