from user_interface import prop_update
from user_interface import ask_course
from entities import Teacher

''' Mantenimiento de profesores '''

# Crear profesor
def create_teacher(id_num,  name, email, course, teachers, teachers_names):
    '''crea y agrega un prof. a la lista de profes que recibe como parametro'''
    teacher = Teacher(id_num, name, email, course)
    teachers.append(teacher)
    teachers_names.append(name)

# Leer profesor
def read_teacher(id_num, teachers):
    '''regresa una cadena con los datos del profe: nombre y curso'''

    for t in teachers:
        if t.id_num == id_num:
            return ('''
                >> Datos del profesor
                    Id Num: {}
                    Nombre: {}
                    Email:  {}
                    Curso:  {}
            '''.format(t.id_num, t.name, t.email, t.course))

#Actualizar profesor
def update_teacher(id_num, teachers, courses):
    '''Actualiza los datos de un profesor'''
    found= False
    for t in teachers:
        if t.id_num == id_num:
            found = True
            print('\n>>Nombre actual: ', t.name)
            if (prop_update('nombre')):
                t.name = input('Ingrese nuevo nombre del profesor: ')

            print('\n>>Email actual: ', t.email)
            if (prop_update('email')):
                t.email = input('Ingrese nuevo email del profesor: ')
            
            print('\n>>Curso actual: ', t.course)
            if (prop_update('curso')):
                t.course = ask_course(courses)
            
        print ('\nActualización completa... ', read_teacher(id_num, teachers))    
    
    if (found != True):
        print('No se encontró ningun profesor con el ID: ' + id_num)
             
# Eliminar profesor
def delete_teacher(id_num, teachers,teachers_names):
    found = False
    index = 0
    for t in teachers:
        if t.id_num == id_num:
            found = True
            break
        index += 1

    if found:
       teachers.pop(index)
       teachers_names [index]
       return print('Se eliminó al prof. con Id: ', id_num)
    else:
       return print('No se encontro prof. con Id: ', id_num)

# Rertonar info de todos los profes de la lista en un string
def teachers_to_str(teachers):
    count = 1
    t_str='' # almacena toda la info de todos los prof 
    for t in teachers:
        t_str += '['+str(count)+']'+('+'*30)+'\n'
        t_str += '\n'+ str(t) + '\n'
        count+=1
    return t_str