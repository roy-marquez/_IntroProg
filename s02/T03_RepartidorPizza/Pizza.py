# Estos inputs estan perfectos, muy bien!.
#   yo le agregaria un espacio al final la solicitud del dato:
#   Ejemplo: input ("Cantidad de pizzas: ")
pizzas = int(input ("cantidad de pizzas")) 
rebanadadepizzas = int(input ("rebanada de pizzas"))
personas  = int(input("cantidad de personas"))

# 1. No puedes convertir "sin dueño" a entero solo numeros ejemplos: 1, 56, 150
# 2. Nunca usas la variable sobra en los calculos o para imprimir, entonces no la declares.
sobra = int (input ("sin dueño"))

# Para hacer los calculos no debes usar la funcion conversor int(), puede usar el operador //
# simplemente las variables y los operadores, recuerde que ya los convirtio antes.
# Nombres muy largos de variables trata de evitarlos pero si los usas
#   inicia con minuscula y cada nueva palabra inicia con Mayuscula, es mas legible
#   Por ejemplo : rebanadasCorrespondientes, rebanadasDePizza
rebanadascorrespondientes = int(("pizzas * rebanadadepizzas)/personas" ))

# Igual aquí, no hace falta la funcion conversor int() despues de la coma solo la variable
#   y ten cuidado con los nombres de las varibles, digitaste corespondientes con una 'r'.
print(("cantidad de rebanadas por personas"), int("rebanadascorespondientes"))

# 1. Trata de no usar 'ñ' en nombres de variables
# 2. De nuevo no hace falta la funcion conversora int()
# 3. La doble comilla ("") la usaste alredor de toda la formula, es un calculo no la uses.
sindueño = int("pizzas * rebanadasdepizzas) - ( personas * rebanadascorrespondientes)")

# Si intentas imprimir las variables, entoces No agregues las comillas.
print("rebandascorrespondientes, sindueño")
