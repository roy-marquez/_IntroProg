class Teacher:
    '''Representa un profesor '''
    def __init__(self, id_num, name, email, course):
        self.id_num = id_num
        self.name = name
        self.email = email
        self.course = course
    
class Student:
    '''Representa un estudiante '''
    def __init__(self, id_num, name, email, course):
        self.id_num = id_num
        self.name = name
        self.email = email
        self.course = course

class Group:
    teacher = None
    students = []
    
    def __init__(self, course, id_group, teacher = None):
        self.course = course
        self.id_group = id_group
        self.Teacher = teacher
    
    def get_students_names(self):
        names = ''
        for i in self.students:
            names += '\t' + i +'.'+ self.students[i].name + '\n'
        return names

    def get_info_group(self):
        info = 'Curso: {}'.format(self.course) + '\n'
        info += 'Grupo Id: {}'.format(self.id_group) + '\n'
        info += 'Profesor: {}'.format(self.teacher) + '\n'
        info += 'Estudiantes: \n {}'.format(self.get_students_names() + '\n')
        return info
    
    def set_teacher(self, teacher):
        '''Asignar el profesor del curso'''
        self.teacher = teacher
        print ('\n Se asign a {0} como profesor del Grupo {1} del Curso de {2}.'.format(teacher.name, self.id_group, self.course))
    
    def add_student(self, student):
        self.students.append(student)
        print ('\n Se agregó {0}, a la lista de estudiantes del Grupo {1} del Curso de {2}.'.format(student.name,self.id_group, self.course))

## Variables globales de almacenamiento (Base de Datos)

# Almacena todas las instancias de Teacher del sistema
teachers = [] 

# Almacena todas las instancias de Student del sistema
students = []

# Diccionario que almacena todas las instancias de Group 
# del sistema, cuya key es la letra de grupo, y el value una instancia de Group 
groups = {}

#
subjects = ('Python', 'Kotlin', 'JS')

## Funciones generales
def prop_update (prop):
    ''' Pregunta si se desea actualizar la propiedad que se recibe como parametro
        Si la respuesta es 's' se retorna un True de lo contrario un False
    '''
    answer = 'Actualizar {} ? : [S = si] / [N = no] :'.format(prop)
    if (input(answer.lower()) == 's'):
        return True
    else:
        return False

def exist(id_num, people_list):
    ''' Determina si una persona (prof o estud) existe en una lista 
        por medio de la prop. id_num, devuelve True si la encuentra
    '''
    for p in people_list:
        if (p.id_num == id_num):
            return True
        else:
            return False

def index_of_person(id_num, people_list):
    ''' Si una persona existe en una lista devuelve la posicion donde se encuentra
        de lo contrario devuelve -1.
    '''
    if exist(id_num, people_list):
        for i in range(len(people_list)):
            if id_num == people_list[i].id_num:
                return i
    else:
        return -1


### Mantenimiento de profes

# Crear profesor
def create_teacher(id_num,  name, email, course):
    '''crea y agrega un prof. a la lista de profes'''
    teacher = Teacher(id_num, name, email, course)
    teachers.append(teacher)

# Leer profesor
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
    
# Actualizar profesor
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
             
# Eliminar profesor
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

### Mantenimiento de estudiantes

# Crear estudiante
def create_student(id_num,  name, email, course):
    '''crea y agrega un estudiante a la lista de estudiantes'''
    student = Student(id_num, name, email, course)
    students.append(student)

# Leer estudiante
def read_student(id_num):
    '''regresa una cadena con los datos del estudiante: nombre y curso'''
    for s in students:
        if s.id_num == id_num:
            return ('''
                >> Datos del estudiante:
                    Id Num: {}
                    Nombre: {}
                    email: {}
                    Curso: {}

            '''.format(s.id_num, s.name, s.email, s.course))
    
# Actualizar estudiante
def update_student(id_num):
    found= False
    for s in students:
        if s.id_num == id_num:
            found = True
            print('>>Nombre actual: ', s.name)
            if (prop_update('nombre')):
                s.name = input('Ingrese nuevo nombre del estudiante: ')

            print('>>Email actual: ', s.email)
            if (prop_update('email')):
                s.email = input('Ingrese nuevo email del estudiante: ')
            
            print('>>Curso actual: ', s.course)
            if (prop_update('course')):
                s.course = input('Ingrese nuevo curso del estudiante: ')
            
            print ('Actualización completa... ', read_student(id_num))    
    
    if (not found):
        print('No se encontró ningun estudiante con el ID: ' + id_num)
             
# Eliminar estudiante
def delete_student(id_num):
    found = False
    index = 0
    for s in students:
        if s.id_num == id_num:
            found = True
            break
        index += 1

    if found:
       students.pop(index)
       print('Se eliminó al estudiante con Id: ', id_num)
    else:
       print('No se encontro estudiante con Id: ', id_num)


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



def option_menu(literal=''):
    '''Despliega las opciones de mantenimientos disponibles y devuelve '''
    print('''\n=============== Mantenimiento {0} =============== \n
    Seleccione una opción:
    \t1. Crear {0}
    \t2. Consultar {0}
    \t3. Actualizar {0}
    \t4. Eliminar {0}
    \t5. Imprimir lista.
    \t6. SALIR!
    '''.format(str(person)))  
    opcion = input("Digíte una opción: ")
    
    #Selecciona solo caracter numericos por medio de valores ascii
    if len(opcion) == 1:
        opt = ord(opcion)
        if opt >= 49 and opt<= 54:
            return int(option)
        else:
            print ('\n>>> ERROR! OPCION NO VALIDA.\n')
            option_menu()
    else:
        print ('>>> ERROR!, FAVOR DIGITE UN CARACTER NUMERICO')
        option_menu()

main_menu()
teachers_menu()
update_teacher(input('\nIngrese el ID del profesor a actualizar: '))
delete_teacher(input('\nIngrese el ID del profesor a eliminar: '))