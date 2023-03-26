
# Desarrollar la función signo(n), 
# que reciba un número entero y devuelva 1, -1 o 0 
# según el valor recibido sea positivo, negativo o nulo.


def signo(n: int) -> int:
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


num = int(input("Ingrese un número: "))

print(f"El signo del número es: {signo(num)}")