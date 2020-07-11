def prop_update (prop):
    answer = 'Actualizar {} ? : [S = si] / [N = no]'.format(prop)
    if (input(answer.lower()) == 's'):
        return True
    else:
        return False


# print( 'Acualizar id_num: ', prop_update('id_num'))
# print( 'Acualizar nombre: ', prop_update('nombre'))
# print( 'Acualizar email: ', prop_update('email'))
# print( 'Acualizar curso: ', prop_update('curso'))

def option_menu(person=''):
    '''Despliega las opciones de mantenimientos disponibles y devuelve '''
    print('''\n=============== Mantenimiento {0} =============== \n
    Seleccione una opción:
    \t1. Crear
    \t2. Consultar 
    \t3. Actualizar 
    \t4. Eliminar 
    \t5. Imprimir lista.
    \t6. SALIR!
    '''.format(str(person)))  
    
    opcion = input("Digíte una opción: ")
    
    #Selecciona solo caracter numericos por medio de valores ascii
    if len(opcion) == 1:
        opt = ord(opcion)
        if opt >= 49 and opt<= 54:
            return opt
        else:
            print ('\n>>> ERROR! OPCION NO VALIDA.\n')
            option_menu()
    else:
        print ('>>> ERROR!, FAVOR DIGITE UN CARACTER NUMERICO')
        option_menu()

    
print(option_menu('profesor'))