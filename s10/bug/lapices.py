class Lapiz():
    tipo = 'lapiz generico'
    largo = '20cm'
    
    def __init__(self, color='gris'):
        self.color = color
    
    def __str__(self):
        return f'{self.tipo}: {self.color}'


class Lapiz_color(Lapiz):
    tipo = 'Lapiz de color'
    
    def __init__(self, color='gris'):
        self.color = color

    def pintar(self):
        return f'Pinto de color {self.color}!'


class Lapiz_grafito(Lapiz):
    tipo = 'Lapiz de grafito'

    def pintar(self):
        return 'Pinto de color GRIS'
    
    def borrar(self):
        return 'Puedo borrar, porque tengo borrador.'