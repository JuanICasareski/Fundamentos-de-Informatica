
# Escribir una función que reciba como parámetros dos números enteros. 
# Calcular y devolver el resultado de la multiplicación de ambos valores utilizando solamente sumas. 
# Por ejemplo 4 * 3 = 4 + 4 + 4 .


def multiply(a: int, b: int) -> int:
    result = 0
    i = 1 

    while i <= b:
        result += a
        i += 1
    
    return result


num1 = int(input("Ingrese el número a multiplicar: "))
num2 = int(input("Ingrese el número que lo multiplicará: "))

print(f"El resultado de la multiplicación es: {multiply(num1, num2)}")