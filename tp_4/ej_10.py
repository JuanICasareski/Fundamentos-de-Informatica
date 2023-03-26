
# El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X <= N. 
# Desarrollar un programa para calcular el factorial de un número dado. 
# Deberán rechazarse las entradas inválidas (menores que 0).


num = int(input("Ingrese el número del cual calcular su factorial: "))

sum = 1


while num > 0:
    sum *= num
    num -= 1

print(f"El factorial es: {sum}")
