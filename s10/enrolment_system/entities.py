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
        info = 'Rol:   {}'.format(self.rol) + '\n'
        info += 'Id:    {}'.format(self.id_num) + '\n'
        info += 'Nombre:{}'.format(self.name) + '\n'
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
    #teacher = None
    #g_students = []
    
    def __init__(self, course, id_group, week_day,  teacher = None):
        self.course = course
        self.id_group = id_group
        self.week_day = week_day
        self.teacher = teacher
        self.g_students = list()
        self.teacher = None

    def get_students_names(self):
        '''Regresa un string con los nombres de todos los estudiantes de este grupo'''
        names = ''
        for i in range(0, len(self.g_students)):
            names += '\t[' + str(i+1) +']. Id:'+ str(self.g_students[i].id_num) +' => ' + str(self.g_students[i].name) + '\n'
        return names

    def __str__(self):
        '''Regresa un string de toda la información del grupo'''
        info = '\nCurso: {}'.format(self.course) + '\n'
        info += 'Grupo Id: {}'.format(self.id_group) + '\n'
        info += 'Dia de la semana: {}'.format(self.week_day) + '\n'
        if self.teacher != None:
            info += 'Profesor: {}'.format(self.teacher.name) + '\n'
        else:
            info += 'Profesor: No Asignado' + '\n'
        info += 'Estudiantes: \n {}'.format(self.get_students_names() + '\n')
        return info
    
    def set_teacher(self, teacher):
        '''Permite asignar el profesor que recibe como parámetro a este grupo'''
        self.teacher = teacher
        #print ('\n Se asigna {0} como profesor del Grupo {1} del Curso de {2}.'.format(self.teacher.name, self.id_group, self.course))
        print('Se asignó profesor al grupo.')
    
    def add_student(self, student):
        '''Permite agregar el estudiante que recibe por parametro a este grupo'''
        self.g_students.append(student)
        print ('\n Se agregó {0}, a la lista de estudiantes del Grupo {1} del Curso de {2}.'.format(student.name,self.id_group, self.course))
    
    def del_student(self, student):
        '''Permite eliminar el estudiante que recibe por parametro de la lista de estudiantes de este grupo'''
        self.g_students.remove(student)
        print ('\n Se eliminó {0}, a la lista de estudiantes del Grupo {1} del Curso de {2}.'.format(student.name,self.id_group, self.course))
    

## Funciones generales
def person_exist(id_num, people_list):
    ''' Determina si una persona (prof o estudiante) existe en una lista 
        por medio de la prop. id_num, devuelve True si la encuentra
    '''
    for p in people_list:
        if (p.id_num == id_num):
            return True
    return False

def index_of_person(id_num, people_list):
    ''' Si una persona existe en una lista devuelve el indice (entero positivo) donde se encuentra.
    '''
    if person_exist(id_num, people_list):
        for p in people_list:
            if (p.id_num == id_num):
                return people_list.index(p)

def exist_group(course, id_group, groups):
    ''' Determina si existe un grupo con del course y el id_group en el diccionario ingresado'''
    for g in groups:
        if g.course == course:
            if g.id_group == id_group:
                return True
    return False     