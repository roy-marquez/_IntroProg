from user_interface import get_option_from
from user_interface import *
from data import *
from crud_teacher import *
from crud_student import *
from crud_group import *

main_menu_options = [
    'Mantenimiento Profesores',
    'Mantenimiento Estudiantes',
    'Mantenimiento Grupos',
    'Salir del sistema.'
]

#Lista de opciones de los menu de profesores y estudiantes
menu_options = [
    'Agregar', 
    'Consultar',
    'Actualizar',
    'Eliminar',
    'Imprimir lista',
    'Salir'
]

#Lista de opciones del menu de grupos
menu_options_groups = [
    'Crear grupo', 
    'Consultar grupo',
    'Actualizar grupo',
    'Eliminar grupo',
    'Salir'
]


# Constantes de formateo titulos
LONG = 60
CHAR = '=' 


#Sets de letras para grupos
free_letters = None
taken_letters = None
groups_labels = created_groups_labels


def menu_teachers():
    teachers_opt = get_option_from(menu_options, 'Mantenimiento de profes')
    
    if teachers_opt == 1:
        print (new_title('< Agregar profe >', LONG, CHAR, True))
        create_teacher(ask_id(), ask_name(), ask_email(), ask_course(courses), teachers, teachers_names)
        menu_teachers()
    
    elif teachers_opt == 2:
        print (new_title('< Consultar profe >', LONG, CHAR))
        print (read_teacher(ask_id(), teachers))
        menu_teachers()
    
    elif teachers_opt == 3:
        print (new_title('< Actualizar profe >', LONG, CHAR))
        print (update_teacher(ask_id(), teachers, courses))
        pause()
        menu_teachers()
    
    elif teachers_opt == 4:
        print (new_title('< Eliminar profe >', LONG, CHAR))
        print (delete_teacher(ask_id(), teachers, teachers_names))
        menu_teachers()
    
    elif teachers_opt == 5:
        print (new_title('< Imprimir lista de Profes >', LONG, CHAR))
        print(teachers_to_str(teachers))
        menu_teachers()
    
    else:
        print ('\nRegresando a menu principal...')
        start()

def menu_students():
    student_opt = get_option_from(menu_options, 'Mantenimiento de estudiantes')
    
    if student_opt == 1:
        print (new_title('< Agregar estudiante >', LONG, CHAR))
        create_student(ask_id(), ask_name(), ask_email(), ask_course(courses), students)
        menu_students()
    
    elif student_opt == 2:
        print (new_title('< Consultar estudiante >', LONG, CHAR))
        print (read_student(ask_id(), students))
        pause()
        menu_students()

    elif student_opt == 3:
        print (new_title('< Actualizar estudiante >', LONG, CHAR))
        print (update_student(ask_id(), students, courses))
        menu_students()
        
    elif student_opt == 4:
        print (new_title('< Eliminar estudiante >', LONG, CHAR))
        print (delete_student(ask_id(), students))
        menu_students()
    
    elif student_opt == 5:
        print (new_title('< Imprimir lista de estudiantes >', LONG, CHAR))
        print(students_to_str(students))
        pause()
        menu_students()
    
    else:
        print ('\nRegresando a menu principal...')
        start()

def menu_groups():
    group_opt = get_option_from(menu_options_groups, 'Mantenimiento de Grupos')
    
    if group_opt == 1:
        print (new_title('< Crear Grupo >', LONG, CHAR))
        #pregunto al usuario por el curso
        course = ask_course(courses)
        #obtengo una referencia al set de letras libre de ese curso (en data.py) 
        free_letters = free_letters_by_course.get(course)
        #obtengo una referencia al set de letras tomadas para los cursos
        taken_letters = taken_letters_by_course.get(course)
        #pregunto al usuario cual letra elige
        letter = ask_letter(free_letters)
        # instancio el nuevo grupo basado en curso, letra, dia y lo agrego al diccionario de grupos
        create_group(course, letter, ask_weekday(days), groups)
        # saco la letra usada del set de letras disponibles
        free_letters.remove(letter)
        #agrego la letra tomada al set de letras tomadas por curso
        taken_letters.add(letter)
        # agrego la etiqueta del nuevo grupo a las lista de etiquetas de grupos
        groups_labels.append(course +'-'+ letter )
        #vuelvo a llamar al menu 
        menu_groups()

    elif group_opt == 2:
        print (new_title('< Consultar Grupo >', LONG, CHAR))
        if (len(groups)>0):
            print ('Los grupos actuales son: ') 
            i = get_option( groups_labels)-1
            key = groups_labels[i]
            print ( read_group(key, groups))
        else:
            print('>>> No existen grupos creados. ')
            pause()
        menu_groups()

    elif group_opt == 3:
        print (new_title('< Actualizar Grupo >', LONG, CHAR))
        if (len(groups)>0):
            print ('Los grupos actuales son: ') 
            i = get_option( groups_labels)-1
            key = groups_labels[i]
            print (update_group(key, groups, teachers, teachers_names, students))
        else:
            print('>>> No existen grupos creados. ')
            pause()
        menu_groups()
    
    elif group_opt == 4:
        print (new_title('< Eliminar Grupo >', LONG, CHAR))
        if (len(groups)>0):
            print ('Los grupos actuales son: ') 
            i = get_option( groups_labels)-1
            key = groups_labels[i]
            print(delete_group(key, groups, groups_labels))
        else:
            print('>>> No existen grupos creados. ')
            pause()
        menu_groups()

    else:
        print ('Regresando al menu principal...')
        start()

def start():
    main_opt = get_option_from(main_menu_options, "Menu Principal")
    if main_opt == 1:
        menu_teachers()
    
    elif main_opt == 2:
        menu_students()
    
    elif main_opt == 3:
        menu_groups()
    else:
        print('Saliendo del sistema de matricula')

print(new_title('Sistema de Matricula', 60, '░', True))
start()