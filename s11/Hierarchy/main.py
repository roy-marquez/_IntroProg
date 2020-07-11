from dog import Dog
from races import *

milo = Dog('Milo', 2)
jack = JackRussellTerrier('Jack', 3)
buddy = Dachshund('Buddy', 9)
billy = Bulldog('Billy', 2)

# print(milo)
# print(milo.speak('Guau'))

# print(jack.species)
# print(buddy.name)
# print(buddy)
# print(billy.speak("Woof"))

def menu():
    print('Menu:')
    print('''
    a. Crear
    b. Leer
    c. Editar
    d. Eliminar
    e. Salir
    ''')

    selection = input()
    if selection.lower() == 'a':
        addDog()
        menu()        
    elif selection.lower() == 'b':
        printDogs()
        menu()
    elif selection.lower() == 'c':
        editDog()
        menu()
    elif selection.lower() == 'd':
        deleteDog()
        menu()
    elif selection.lower() == 'e':
        print('Saliendo...')
    else:
        print('Opcion incorrecta...')

def addDog():
    print(f'1.{JackRussellTerrier.race} 2.{Dachshund.race} 3.{Bulldog.race}')
    race = input('Raza? ')
    name = input('Nombre? ')
    age =  input('Edad? ')

    if race == 1:
        dog = JackRussellTerrier(name, age)
    elif race == 2:
        dog = Dachshund(name, age)
    elif race == 3:
        dog = Bulldog (name, age)
    
    dogs.append(dog)

def printDogs():
    pass

def editDog():
    pass

def deleteDog():
    pass

menu()