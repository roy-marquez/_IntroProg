# Programa que lea un entero positivo, 𝑛, 
# introducido por el usuario y después muestre en pantalla 
# la suma de todos los enteros desde 1 hasta 𝑛. 

n = int(input("Ingrese el n: "))

subsuma = int ((n*(n+1)) / 2)

print ("La suma de todos los enteros desde 1 hasta " + str(n) + " es: " + str(subsuma))