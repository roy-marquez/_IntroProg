 

''' Módulo que define clases y funciones de la lógica de negocio '''
class Person:
    '''Representa una persona'''
    rol='Persona'
    def __init__(self, id_num, name, email, course):
        self.id_num = id_num
        self.name = name
        self.email = email
        self.course = course

    def __str__(self):
        info = 'Rol: {}'.format(self.rol) + '\n'
        info += 'Id: {}'.format(self.id_num) + '\n'
        info += 'Nombre: {}'.format(self.name) + '\n'
        info += 'Email: {}'.format(self.email) + '\n'
        info += 'Curso: {}'.format(self.course) + '\n'
        return info

class Teacher(Person):
    '''Representa un profesor '''
    rol = 'Profesor'

class Student(Person):
    '''Representa un estudiante '''
    rol = 'Estudiante'

class Group:
    '''Representa un grupo: Curso, profesor y lista de estudiantes '''
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

    def __str__(self):
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
    
## Funciones generales

def person_exist(id_num, people_list):
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
    if person_exist(id_num, people_list):
        for i in range(len(people_list)):
            if id_num == people_list[i].id_num:
                return i
    else:
        return -1
