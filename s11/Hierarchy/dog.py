class Dog:
    species = 'Canis familiaris'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Este {Dog.species} se llama {self.name} y es de {self.age} años.'

    def speak(self, sound):
        return f'{self.name} dice {sound}'