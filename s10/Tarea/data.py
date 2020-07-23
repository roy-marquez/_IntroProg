## Variables globales de almacenamiento ("Seudo Base de Datos")

# Almacena todas las INSTANCIAS de Teacher del sistema
teachers = [] 

teachers_names = []

# Almacena todas las INSTANCIAS de Student del sistema
students = []

# Diccionario que almacena todas las INSTANCIAS de Group 
# del sistema, cuya key es la letra de grupo, y el value una instancia de Group 
groups = {}

#Almacena las etiquetas (Curso-Letra) de los grupos creados
created_groups_labels = []

# lista del conjunto de cursos que se ofrecen
courses = ['Python', 'Kotlin', 'JS', 'Java']

# id_group para cada tipo de curso
groups_letters = {'A', 'B', 'C', 'D'}

# letras libres por curso
free_letters_by_course = {
    'Python': groups_letters.copy(), 
    'Kotlin': groups_letters.copy(),
    'JS': groups_letters.copy(),
    'Java': groups_letters.copy(),
    }

# letras tomadas por curso
taken_letters_by_course = {
    'Python': set(), 
    'Kotlin': set(),
    'JS': set(),
    'Java':set()
}

# lista de dias en que se imparten los cursos
days = ['martes', 'miercoles', 'jueves', 'viernes']