from user_interface import *
from business_logic_layer import Student

''' Mantenimiento de estudiantes '''

# Crear profesor
def create_student(id_num,  name, email, course, students):
    '''crea y agrega un estudiante a la lista de profes que recibe como parametro'''
    student = Student(id_num, name, email, course)
    students.append(student)

# Leer profesor
def read_student(id_num, students):
    '''regresa una cadena con los datos del profe: nombre y curso'''

    for t in students:
        if t.id_num == id_num:
            return ('''
                >> Datos del estudiante:
                    Id Num: {}
                    Nombre: {}
                    email: {}
                    Curso: {}

            '''.format(t.id_num, t.name, t.email, t.course))

#Actualizar profesor
def update_student(id_num, students):
    found= False
    for t in students:
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
            
            print ('Actualización completa... ', read_student(id_num, students))    
    
    if (not found):
        print('No se encontró ningun profesor con el ID: ' + id_num)
             
# Eliminar profesor
def delete_student(id_num, students):
    found = False
    index = 0
    for t in students:
        if t.id_num == id_num:
            found = True
            break
        index += 1

    if found:
       students.pop(index)
       print('Se eliminó al prof. con Id: ', id_num)
    else:
       print('No se encontro prof. con Id: ', id_num)