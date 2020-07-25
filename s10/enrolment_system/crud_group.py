from user_interface import prop_update
from user_interface import ask_course
from user_interface import ask_teacher
from user_interface import ask_id
from user_interface import get_option
from entities import person_exist
from entities import index_of_person
from entities import Group

''' Mantenimiento de profesores '''

# Crear un grupo
def create_group(course, id_group, week_day, groups, teacher=None ):
    '''crea y agrega un prof. a la lista de profes que recibe como parametro'''
    group = Group(course, id_group, week_day, teacher)
    key = course + '-' + id_group
    groups[key] = group
    return f'Grupo {key} creado.'

# Leer grupo
def read_group(key, groups):
    ''' recibe un diccionario de grupos y una key con el formato Curso-X
    regresa una cadena con los datos del grupo (si existe) '''
    if len(groups) > 0:
        group = groups.get(key)
        return str(group)
    else:
        return '>>>ERROR!: No hay grupos.'

#Actualizar grupo
def update_group(key, groups, teachers, teachers_names, students):
    '''Actualiza los datos de un grupo: '''
    group = groups.get(key)
    
    print('\n>>Dia de la semana actual: ', group.week_day)
    if (prop_update('día de la semana')):
        group.week_day = input('Ingrese nuevo dia de la semana: ')

    if group.teacher == None:
        print ('\nEste grupo no tiene Prof. asignado...')
        if len(teachers)>0:
            if (prop_update('Profesor asignado')):
                teacher = ask_teacher(teachers, teachers_names)
                group.set_teacher(teacher)
        else:
            print('\nSin embargo, la lista de profesores esta vacía.') 
            print('\nDebe agregar un profesor a la lista previamente para poder asignarlo a este grupo.''')
    else:
        print('\n>>Nombre del profesor actual: ', group.teacher.name)
        if (prop_update('profesor')):
            teacher = ask_teacher(teachers, teachers_names)
            group.set_teacher(teacher)
    
    print('\n>>Estudiantes : ')
    print(group.get_students_names())
    if (prop_update('lista de estudiantes')):
        print("\nQue desea hacer ?\n")
        opt = get_option(['Agregar Estudiante', 'Eliminar Estudiante', 'Salir...'])
        while opt !=3: 
            if opt == 1:
                if len(students)>0:
                    student_id = ask_id()
                    if person_exist(student_id, students):
                        i = index_of_person(student_id, students)
                        group.add_student(students[i])
                        #print('\tSe agregó al estudiante, con id: {}'.format(student_id))
                    else:
                        print('\t>>>Error!, No se encontró un estudiante, con id: {}'.format(student_id))

                else:
                    print('Aún no hay estudiantes registrados en la lista general de estudiantes.')
            elif opt == 2:
                if len(group.g_students)>0:
                    student_id = ask_id()
                    i = index_of_person(student_id, group.g_students)
                    group.del_student(group.g_students[i])
                else:
                    print('>>>Error!, La lista de estudiantes del presente grupo esa vacía!')
                    print('No es posible borrar estudiante')
            
            print("\nQué desea hacer ?\n")
            opt = get_option(['Agregar Estudiante', 'Eliminar Estudiante', 'Salir...'])
                            
    return ('\nActualización completa... \n' + read_group(key, groups))    
    
             
# Eliminar grupo
def delete_group(key, groups, groups_labels):
    '''Elimina un grupo del diccionario de grupos con base en el curso y el identificador'''
    groups.pop(key)
    groups_labels.remove(key)
    return print('Se eliminó al grupo: ', key)
        

# Retorna info de todos grupos de la lista en un string
def groups_to_str(groups):
    count = 1
    g_str='' # almacena toda la info de todos los prof 
    for g in groups:
        g_str += '['+str(count)+']'+('+'*30)+'\n'
        g_str += '\n'+ str(g) + '\n'
        count+=1
    return g_str

