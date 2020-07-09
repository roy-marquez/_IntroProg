# Hacer un programa que lea un texto largo y cuente las veces que aparece cada palabra.
# Ejemplo: En la ciudad de Pamplona, hay una plaza. En la plaza, hay una esquina. En la esquina, hay una casa. En la casa, hay una pieza. En la pieza, hay una cama. En la cama, hay una estera.

text = input('Ingrese su texto: ')

text = text.replace('.', '').replace(',', '').lower()

splitText = text.split()
words = []
count = []
letters = []

for word in splitText:
    if word in words:
        index = words.index(word)
        count[index] += 1
    else:
        words.append(word)
        count.append(1)
        letters.append(len(word))
print(words)
print(count)
print(letters)

for index, word in enumerate(words):
    print(word, count[index], letters[index])