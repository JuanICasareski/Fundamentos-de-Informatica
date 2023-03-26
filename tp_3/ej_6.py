
# Una remisería requiere un programa que calcule el precio de un viaje  
# a partir de la cantidad de kilómetros que desea recorrer el usuario. 
# Para eso cuenta con la siguiente tarifa:
#  - Viaje mínimo $250. Sólo se cobra cuando el importe por kilómetro no alcanza este mínimo.
#  - Si recorre entre 0 y 10 km: $30 por km
#  - Si recorre 10 km o más: $20 por km


cost_per_km = 30

travel_distance = int(input("Ingrese la distancia del viaje en km: "))


if travel_distance > 10:
    cost_per_km = 20

cost = cost_per_km * travel_distance

if cost < 250:
    cost = 250

print(f"El costo del viaje es de ${cost}")
