number = int(input('ingrese el numero para generar el patron: '))
count = number
line = ''

while number > 0:
    count = number
    line = ''
    while count > 0:
        line = line + str(count)
        count = count - 1
    print (line)
    number = number - 1