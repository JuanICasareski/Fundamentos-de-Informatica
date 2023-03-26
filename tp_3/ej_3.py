
# Desarrollar un programa que solicite un número de mes (por ejemplo 4) y escriba el nombre del mes en letras ("abril"). 
# Verificar que el mes sea válido y mostrar un mensaje de error en caso de que no lo sea.

month_number = int(input("Ingrese un número de mes: "))

if (month_number == 1):
    print(f"El mes número 1 es Enero")
elif (month_number == 2):
    print(f"El mes número 2 es Febrero")
elif (month_number == 3):
    print(f"El mes número 3 es Marzo")
elif (month_number == 4):
    print(f"El mes número 4 es Abril")
elif (month_number == 5):
    print(f"El mes número 5 es Mayo")
elif (month_number == 6):
    print(f"El mes número 6 es Junio")
elif (month_number == 7):
    print(f"El mes número 7 es Julio")
elif (month_number == 8):
    print(f"El mes número 8 es Agosto")
elif (month_number == 9):
    print(f"El mes número 9 es Septiembre")
elif (month_number == 10):
    print(f"El mes número 10 es Octubre")
elif (month_number == 11):
    print(f"El mes número 11 es Noviembre")
elif (month_number == 12):
    print(f"El mes número 12 es Diciembre")
else:
    print("El número ingresado no corresponde a un mes")

