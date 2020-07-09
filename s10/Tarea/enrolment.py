class Teacher:
    def __init__(self, id_num, name, email, course):
        self.id_num = id_num
        self.name = name
        self.email = email
        self.course = course
    
class Student:
    def __init__(self, id_num, name, email, course):
        self.id_num = id_num
        self.name = name
        self.email = email
        self.course = course

class Group:
    def __init__(self, course, groupId, teacher, students):
        self.course = course
        self.groupId= groupId
        self.teacher = teacher
        self.students = students
    
    def get_students_names(self):
        names = ''
        for i in students:
            names += '\t' + i +'.'+ students[i].name + '\n'
        return names

    def get_info_group(self):
        info = 'Curso: {}'.format(self.course) + '\n'
        info += 'Grupo Id: {}'.format(self.groupId) + '\n'
        info += 'Profesor: {}'.format(self.teacher) + '\n'
        info += 'Estudiantes: \n {}'.format(self.get_students_names() + '\n')
        return info

# Variables globales de almacenamiento
teachers = []
students = []
subjects = ('Python', 'Java', 'Kotlin', 'JS', 'Php')

# Funciones generales
def prop_update (prop):
    ''' Pregunta si se desea actualizar la propiedad que se recibe como parametro
        Si la respuesta es 's' se retorna un True de lo contrario un False
    '''
    answer = 'Actualizar {} ? : [S = si] / [N = no] :'.format(prop)
    if (input(answer.lower()) == 's'):
        return True
    else:
        return False

### Mantenimiento de profes

# Crear
def create_teacher(id_num,  name, email, course):
    '''crea y agrega un prof. a la lista de profes'''
    teacher = Teacher(id_num, name, email, course)
    teachers.append(teacher)

# Leer
def read_teacher(id_num):
    '''regresa una cadena con los datos del profe: nombre y curso'''
    for t in teachers:
        if t.id_num == id_num:
            return ('''
                >> Datos del profesor
                    Id Num: {}
                    Nombre: {}
                    email: {}
                    Curso: {}

            '''.format(t.id_num, t.name, t.email, t.course))
    
# Actualizar
def update_teacher(id_num):
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
            
            print ('Actualización completa... ', read_teacher(id_num))    
    
    if (not found):
        print('No se encontró ningun profesor con el ID: ' + id_num)
             
# Eliminar
def delete_teacher(id_num):
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


def main_menu():
    print ('='*10 + ' SISTEMA MATRICULA ' + '='*10 )

def teachers_menu():
    print('Agregando profes...')
    for i in range(3):
        print ('\nAgregando PROFESOR ', i+1)
        
        id_num = input('Ingrese el Id: ')
        name = input('Ingrese nombre: ')
        email = input('Ingrese email: ')
        course = input('Ingrese curso que imparte: ')
        
        create_teacher(id_num, name, email, course)
        print ('\n >> Agregado profe: ', teachers[i].name)
    
    print (read_teacher(input('\nIngrese el id del profe a buscar: ')))


main_menu()
teachers_menu()
update_teacher(input('\nIngrese el ID del profesor a actualizar: '))
delete_teacher(input('\nIngrese el ID del profesor a eliminar: '))