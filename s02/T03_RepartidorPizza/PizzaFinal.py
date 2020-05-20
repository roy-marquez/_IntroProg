# Inputs
pizzas = int(input ("cantidad de pizzas: ")) 
rebanadasDePizzas = int(input ("rebanada de pizzas: "))
personas  = int(input("cantidad de personas: "))

# Process
rebanadasCorrespondientes = pizzas * rebanadasDePizzas // personas
sinDueno = (pizzas * rebanadasDePizzas) - ( personas * rebanadasCorrespondientes)

# Outputs
print("\tCantidad de rebanadas por persona:", rebanadasCorrespondientes)
print("\tRebanadas sin dueño:", sinDueno)
