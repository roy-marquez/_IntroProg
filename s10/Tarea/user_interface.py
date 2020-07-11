''' Módulo que define clases y funciones de la interfaz de usuario '''

## Funciones generales

def prop_update (prop):
    ''' Pregunta si se desea actualizar la propiedad que se recibe como parámetro
        Si la respuesta es 's' se retorna un True de lo contrario un False
    '''
    answer = 'Actualizar {} ? : [S = si] / [N = no] :'.format(prop)
    if (input(answer.lower()) == 's'):
        return True
    else:
        return False