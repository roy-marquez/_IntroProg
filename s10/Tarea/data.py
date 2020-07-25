## Variables globales de almacenamiento ("Seudo Base de Datos")

# Almacena todas las INSTANCIAS de Teacher del sistema
teachers = [] 

# Almacena unicamente los nombres de profesores registrados en sistema
teachers_names = []

# Almacena todas las INSTANCIAS de Student del sistema
students = []

# Diccionario que almacena todas las INSTANCIAS de Group 
# del sistema, cuya key es la Etiqueta del grupo, y el value una instancia de Group 
groups = {}

# Almacena las etiquetas (Curso-Letra) de los grupos creados, por ejemplo Python-A
created_groups_labels = []

# Lista de cursos que se ofrecen
courses = ['Python', 'Kotlin', 'JS', 'Java']

# Set de id_group para cada tipo de curso
groups_letters = {'A', 'B', 'C', 'D'}

# Lista de letras(id_group) libres por curso
free_letters_by_course = {
    'Python': groups_letters.copy(), 
    'Kotlin': groups_letters.copy(),
    'JS': groups_letters.copy(),
    'Java': groups_letters.copy(),
    }

# Lista de letras(id_group) tomadas por curso
taken_letters_by_course = {
    'Python': set(), 
    'Kotlin': set(),
    'JS': set(),
    'Java':set()
}

# Lista de dias en que se imparten los cursos
days = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']

