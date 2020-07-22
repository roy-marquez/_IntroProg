from user_interface import prop_update
from user_interface import ask_course
from entities import Group


''' Mantenimiento de profesores '''

# Crear un grupo
def create_group(course, id_group, week_day, groups, teacher=None ):
    '''crea y agrega un prof. a la lista de profes que recibe como parametro'''
    group = Group(course, id_group, week_day, teacher)
    key = course + '-' + id_group
    groups[key] = group

# Leer profesor
def read_group(course, id_group, groups):
    ''' recibe un diccionario de groupos y una key con el formato Nombre-X
    regresa una cadena con los datos del grupo (si existe) '''
    if len(groups) > 0:
        for g in groups:
            if g.course == course:
                if g.id_group == id_group:
                    return str(g)
                else:
                    '>>>ERROR!: No se encotró ningun grupo con ese ID'
            else:
                return '>>>ERROR!: No se encontró ningun grupo de ese CURSO'
    else:
        return '>>>ERROR!: No hay grupos.'

#Actualizar grupo
def update_group(course, id_group, groups):
    '''Actualiza los datos de un profesor'''
    found= False
    for g in groups:
        if g.course == course:
            if g.id_group == id_group:
                found = True
                print('\n>>Dia de la semana actual: ', g.weekday)
                if (prop_update('día de la semana')):
                    g.weekday = input('Ingrese nuevo dia de la semana: ')

                print('\n>>Nombre del profesor actual: ', g.teacher)
                if (prop_update('profesor')):
                    g.profesor = input('Ingrese el nombre del nuevo profesor: ')
                                
        print ('\nActualización completa... ', read_group(course, id_group, groups))    
    
    if (found != True):
        print('No se encontró grupo del curso {0} con el ID: {1}'.format(course, id_group))
             
# Eliminar profesor
def delete_teacher(course, id_group, groups):
    found = False
    key = ''
    for g in groups:
        if g.course == course:
            if t.id_group == id_group:
                found = True
                key = course+'-'+id_group
                break

    if found:
       group.pop(key)
       return print('Se eliminó al grupo: ', key)
    else:
       return print('No se encontró grupo del curso {0} con el ID: {1}'.format(course, id_group))
        

# Retorna info de todos grupos de la lista en un string
def groups_to_str(groups):
    count = 1
    g_str='' # almacena toda la info de todos los prof 
    for g in groups:
        g_str += '['+str(count)+']'+('+'*30)+'\n'
        g_str += '\n'+ str(g) + '\n'
        count+=1
    return g_str