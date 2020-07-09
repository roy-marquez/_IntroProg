class Rectangle:
    def __init__(self,  width, height, color):
        self.width = width
        self.heigh = height
        self.color = color

    def getArea(self):
        area = self.width * self.heigh
        return area

    def getPerimeter(self):
        perimeter = (self.width + self.heigh)*2
        return perimeter

#...

curtain = Rectangle (2, 3, 'verde')
monitor = Rectangle (1, 1, 'negro')
pool = Rectangle(15, 25, 'azul')

print('La cortina es de color {}.'.format(curtain.color))
print('El área del monitor es {} metros cuadrados.'.format(monitor.getArea()))
x = pool.getPerimeter()
print (x)