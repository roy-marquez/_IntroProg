from user_interface import prop_update
from user_interface import ask_course
from entities import Student

''' Mantenimiento de estudiantes '''

# Crear estudiante
def create_student(id_num,  name, email, course, students):
    '''crea y agrega un estudiante a la lista de profes que recibe como parametro'''
    student = Student(id_num, name, email, course)
    students.append(student)

# Leer estudiante
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

#Actualizar estudiante
def update_student(id_num, students, courses):
    found= False
    for t in students:
        if t.id_num == id_num:
            found = True
            print('>>Nombre actual: ', t.name)
            if (prop_update('nombre')):
                t.name = input('Ingrese nuevo nombre del estudiante: ')

            print('>>Email actual: ', t.email)
            if (prop_update('email')):
                t.email = input('Ingrese nuevo email del estudiante: ')
            
            print('>>Curso actual: ', t.course)
            if (prop_update('course')):
                t.course = ask_course(courses)
            
            print ('\nActualización completa... ', read_student(id_num, students))    
    
    if (not found):
        print('No se encontró ningun estudiante con el Id: ' + id_num)
             
# Eliminar estudiante
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
       print('Se eliminó al estudiante con Id: ', id_num)
    else:
       print('No se encontro estudiante con Id: ', id_num)

# Retorna info de todos los profes de la lista en un string
def students_to_str(students):
    count = 1
    s_str='' # almacena toda la info de todos los prof 
    for s in students:
        s_str += '['+str(count)+']'+('+'*30)+'\n'
        s_str += '\n'+ str(s) + '\n'
        count+=1
    return s_str