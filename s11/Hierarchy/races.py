from dog import Dog

class JackRussellTerrier(Dog):
    race = 'JackRussellTerrier'
    def speak(self, sound='Argg'):
        return f'{sound} es lo que dice {self.name}'
    pass

class Dachshund(Dog):
    race = 'Dachshund'
    pass

class Bulldog(Dog):
    race = 'Bulldog'
    pass