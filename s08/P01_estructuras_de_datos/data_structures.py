'''
Programa que permite registrar estudiantes y asignarles y color y una fruta...
'''
#Tuplas
colors = ('rojo', 'azul', 'verde', 'anaranjado')
fruits = ('banano', 'naranja', 'pera')

#Set
days = {'lunes', 'martes', 'miercoles', 'jueves', 'viernes'}

#Lista
students = []

def menu():
    '''Brinda las opciones del programa al usuario'''
    print('Seleccione una opcion: ')
    print('''
    a. Imprimir colores
    b. Imprimir frutas
    c. Imprimir días disponibles
    d. Imprimir estudiantes
    e. Agregar estudiante
    f. Salir
    ''')
    selection = input()

    if selection.lower() == 'a':
        printColors()
        menu()
    elif selection.lower() == 'b':
        printFruits()
        menu()
    elif selection.lower() == 'c':
        printDays()
        menu()
    elif selection.lower() == 'd':
        printStudents()
        menu()
    elif selection.lower() == 'e':
        addStudent()
        menu()
    elif selection.lower() == 'f':
        quitProgram()
    else:
        print ('Error incorrecta!')
        menu()

def printColors():
    print(colors)

def printFruits():
    print(fruits)

def printDays():
    print(days)
    
def printStudents():
    print(students)

def addStudent():
    student = {}
    student['name'] = input('Digite un nombre: ')
    
    print ('Seleccione un color: (0,1,2,3): ', colors)
    student['color'] = colors[int(input())]
    
    print ('Seleccione una fruta: (0,1,2): ', fruits)
    student['fruta'] = fruits[int(input())]
    
    print ('Asingnando un día: ', days)
    day = days.pop()
    print('Día asignado: ', day)
    student['day'] = day

    students.append(student)

def quitProgram():
    print('Gracias.\n Ciao')

menu()