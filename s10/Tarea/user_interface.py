''' Módulo que define clases y funciones de la interfaz de usuario '''

TITLE_LONG = 60

## Funciones generales
def prop_update (prop):
    ''' Pregunta si se desea actualizar la propiedad que se recibe como parámetro
        Si la respuesta es 's' se retorna un True de lo contrario un False
    '''
    answer = 'Actualizar {} ? : [S = si] / [N = no] : '.format(prop)
    if (input(answer.lower()) == 's'):
        return True
    else:
        return False

# Funcion que verifica si un str que recibe como paremetro
# retorna true, si el str puede representar un entero positivo
def is_positive_integer(user_str):
    '''Función que determina si un string contiene unicamente carácteres numéricos'''
    is_int = True
    allowed_chars = ['0','1','2','3','4','5','6','7','8','9']
    for char in user_str:
        if allowed_chars.count(char) < 1:
            is_int = False
            break
    return is_int

def new_title(title, long, char, upper=False):
    title = ' ' + title +  ' '
    if upper:
        title = title.upper()
    if (len(title) + 6 > long):
        return '\n' + (char*3) + title + (char*3) + '\n'
    else:
        left = (long - len(title)) // 2
        right = long - left - len(title)
        return '\n' + left * char + title + right * char + '\n'


# Recibe una lista de string de opciones para el menu
# e imprime la lista con un numero de opcion antepuesto
def print_menu(menu_options_list, title='Menu'):
    print (new_title(title, TITLE_LONG, '≡', True))
    count = 0
    for menu_option in menu_options_list:
        count += 1
        print ('\t'+ str(count) + '. ' + menu_option)


def get_option_from(menu_options_list, title='Menú'):
    print_menu(menu_options_list, title)
    option = input("\nDigíte el número de la opción seleccionada: ")
    if is_positive_integer(option):
        opt = int(option)
        if opt > 0 and opt<=len(menu_options_list) :
            return int(option)
        else:
            print ('>>> ERROR!, opción fuera de rango. \n')
    else:
        print ('>>> ERROR!, opción NO válida \n')
    return get_option_from(menu_options_list, title)

def get_option(menu_options_list):
    count = 0
    for menu_option in menu_options_list:
        count += 1
        print ('\t'+ str(count) + '. ' + menu_option)
    option = input("\nDigíte el número de la opción seleccionada: ")
    if is_positive_integer(option):
        opt = int(option)
        if opt > 0 and opt<=len(menu_options_list) :
            return int(option)
        else:
            print ('>>> ERROR!, opción fuera de rango. \n')
    else:
        print ('>>> ERROR!, opción NO válida \n')
    return get_option(menu_options_list)

def ask_id():
    '''funcion que solicita un Id valido, formado de numeros'''
    id_num = input('Ingrese número de id: ')
    if is_positive_integer(id_num):
        return id_num
    else:
        print('>>> ERROR!, opción NO válida \n')
        return ask_id()

def ask_name():
    '''funcion que solicita y retorna el nombre'''
    return input('Ingrese el nombre completo: ')

def ask_email():
    '''funcion que solicita y retorna el email'''
    return input('Ingrese el email: ')

def ask_course(courses):
    '''funcion que solicita y retorna el curso seleccionado'''
    print('Los cursos disponibles son: \n')
    i = get_option(courses)-1
    return courses[i]

def ask_letter(allowed_chars):
    '''funcion que solicita y retorna el group_id(letter) seleccionado'''
    valid_selected_char = False
    while (valid_selected_char != True):
        print('Las id disponibles para el curso son: \n')
        print ('\t'+ str(allowed_chars))
        selected_char = input('Seleccione la letra: ').upper()
        for c in allowed_chars:
            if c == selected_char:
                valid_selected_char = True
                break
    return selected_char

    
    