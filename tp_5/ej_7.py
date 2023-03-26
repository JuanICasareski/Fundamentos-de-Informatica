
# Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el número invertido. 
# Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321.


def reverse_num(num: int) -> int:
    abs_num = abs(num)
    sign = int(num / abs_num)
    reversed = 0

    while abs_num != 0:
        reversed = reversed * 10 + abs(abs_num % 10)
        abs_num //= 10

    return reversed * sign



num = int(input("Ingrese un número: "))
reversed_num = reverse_num(num)

print(f"El número invertido es: {reversed_num}")