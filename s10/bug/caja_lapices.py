class caja_lapices():

    def __init__(self, nombre):
        self.nombre = nombre
        self.caja = list()

    def __str__(self):
        lapices = ''
        if len(self.caja)>0:
            for l in self.caja:
                lapices += '\n' + str(l)
        return f'\nCaja de lapices de {self.nombre} con: {lapices}'
    
    def agregar_lapiz(self, lapiz):
        self.caja.append(lapiz)

    def sacar_lapiz(self, lapiz):
        self.caja.remove(lapiz)
