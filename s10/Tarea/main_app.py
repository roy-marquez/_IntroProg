from user_interface import get_option_from
from user_interface import *
from data import *
from crud_teacher import *
from crud_student import *

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
    'Agregar grupo', 
    'Consultar grupo',
    'Actualizar grupo',
    'Eliminar grupo',
    'Salir'
]

#Sets de letras para grupos

def menu_teachers():
    teachers_opt = get_option_from(menu_options, 'Mantenimiento de profes')
    
    if teachers_opt == 1:
        print (new_title('< Agregar profe >', 60, '═', True))
        create_teacher(ask_id(), ask_name(), ask_email(), ask_course(courses), teachers)
        menu_teachers()
    
    elif teachers_opt == 2:
        print (new_title('< Consultar profe >', 60, '═'))
        print (read_teacher(ask_id(), teachers))
        menu_teachers()
    
    elif teachers_opt == 3:
        print (new_title('< Actualizar profe >', 60, '═'))
        print (update_teacher(ask_id(), teachers, courses))
        menu_teachers()
    
    elif teachers_opt == 4:
        print (new_title('< Eliminar profe >', 60, '═'))
        print (delete_teacher(ask_id(), teachers))
        menu_teachers()
    
    elif teachers_opt == 5:
        print (new_title('< Imprimir lista de Profes >', 60, '═'))
        print(teachers_to_str(teachers))
        menu_teachers()
    
    else:
        print ('\nRegresando a menu principal...')
        start()

def menu_students():
    student_opt = get_option_from(menu_options, 'Mantenimiento de estudiantes')
    if student_opt == 1:
        print (new_title('< Agregar estudiante >', 60, '═'))
        create_student(ask_id(), ask_name(), ask_email(), ask_course(courses), students)
        menu_students()
    
    elif student_opt == 2:
        print (new_title('< Consultar profe >', 60, '═'))
        print (read_teacher(ask_id(), teachers))
        menu_teachers()

    elif student_opt == 3:
        print (new_title('< Actualizar estudiante >', 60, '═'))
        print (update_student(ask_id(), teachers, courses))
        menu_students()
        
    elif student_opt == 4:
        print (new_title('< Eliminar estudiante >', 60, '═'))
        print (delete_student(ask_id(), teachers))
        menu_teachers()
    
    elif student_opt == 5:
        print (new_title('< Imprimir lista de estudiantes >', 60, '═'))
        print(students_to_str(students))
        menu_students()
    
    else:
        print ('\nRegresando a menu principal...')
        start()

def menu_groups():
    group_opt = get_option_from(menu_options_groups, 'Mantenimiento de grupos')
    if group_opt == 1:
        print ('Crear grupo')
    
    elif group_opt == 2:
        print ('Consultar grupo')
    
    elif group_opt == 3:
        print ('Actualizar grupo')
    
    elif group_opt == 4:
        print ('Eliminar grupo')
        start()
    
    else:
        print ('Salir...')

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