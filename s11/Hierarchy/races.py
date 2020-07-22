from dog import Dog

class JackRussellTerrier(Dog):
    race = 'JackRussellTerrier'
    def speak(self, sound='Argg'):
        return f'{sound} es lo que dice {self.name}'
    

class Dachshund(Dog):
    race = 'Dachshund'
    

class Bulldog(Dog):
    race = 'Bulldog'
    