
# Una editorial determina el precio de un libro según la cantidad de páginas que contiene. 
# El costo básico del libro es de $500, más $3,20 por página con encua-dernación rústica. 
# Si el número de páginas supera las 300 la encuadernación debe ser en tela, lo que incrementa el costo en $200. 
# Además, si el número de páginas sobrepasa las 600 se hace necesario un procedimiento especial de en-cuadernación que incrementa el costo en otros $336. 
# Desarrollar un programa que calcule el costo de un libro dado el número de páginas.


initial_cost = 500
cost_per_page = 3.20

pages_number = int(input("Ingrese el número de páginas del libro: "))

cost = initial_cost + (pages_number * cost_per_page)


if (pages_number > 600):
    # Costo de encuadernación en tela y procedimiento especial de encuadernación
    cost += 200 + 336
elif (pages_number > 300):
    cost += 200

print(f"El costo del libro es de ${cost}")
