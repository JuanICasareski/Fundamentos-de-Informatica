
# Crear una lista de N números generados al azar entre 0 y 100 pero sin elemen-tos repetidos.
# El valor de N se ingresa por teclado. 
# Resolver este problema utili-zando dos estrategias distintas:
#  - Impidiendo el agregado de elementos repetidos
#  - Eliminando los duplicados luego de generar la lista. Asegurarse que la cantidad final de elementos sea la solicitada.


from random import randint

def generate_list(n: int) -> list:
    result = []
    i = 0

    while i < n:
        num = randint(0, 100)

        if num not in result:
            result.append(num)
            i += 1

    return result


print(generate_list(10))
