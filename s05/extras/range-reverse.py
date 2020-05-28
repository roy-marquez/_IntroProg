#   Se ingresa una palabra y se imprime letra a letra de forma inversa.
word = input('ingrese la palabra: ')
for i in range(len(word)-1, -1, -1):
    print (word[i])