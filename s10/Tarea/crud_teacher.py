from user_interface import *
from business_logic_layer import Teacher

''' Mantenimiento de profesores '''

# Crear profesor
def create_teacher(id_num,  name, email, course, teachers):
    '''crea y agrega un prof. a la lista de profes que recibe como parametro'''
    teacher = Teacher(id_num, name, email, course)
    teachers.append(teacher)

# Leer profesor
def read_teacher(id_num, teachers):
    '''regresa una cadena con los datos del profe: nombre y curso'''
    # info=None
    # if person_exist(id_num, teachers):
    #     i = index_of_person(id_num, teachers)
    #     info = 'Datos del profesor: \n\t'
    #     info += str(teachers[i])
    # return info

    for t in teachers:
        if t.id_num == id_num:
            return ('''
                >> Datos del profesor
                    Id Num: {}
                    Nombre: {}
                    email: {}
                    Curso: {}

            '''.format(t.id_num, t.name, t.email, t.course))

#Actualizar profesor
def update_teacher(id_num, teachers):
    found= False
    for t in teachers:
        if t.id_num == id_num:
            found = True
            print('>>Nombre actual: ', t.name)
            if (prop_update('nombre')):
                t.name = input('Ingrese nuevo nombre del profesor: ')

            print('>>Email actual: ', t.email)
            if (prop_update('email')):
                t.email = input('Ingrese nuevo email del profesor: ')
            
            print('>>Curso actual: ', t.course)
            if (prop_update('course')):
                t.course = input('Ingrese nuevo curso del profesor: ')
            
            print ('Actualización completa... ', read_teacher(id_num, teachers))    
    
    if (not found):
        print('No se encontró ningun profesor con el ID: ' + id_num)
             
# Eliminar profesor
def delete_teacher(id_num, teachers):
    found = False
    index = 0
    for t in teachers:
        if t.id_num == id_num:
            found = True
            break
        index += 1

    if found:
       teachers.pop(index)
       print('Se eliminó al prof. con Id: ', id_num)
    else:
       print('No se encontro prof. con Id: ', id_num)