
# Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. 
# ¿Cómo cambiaría el algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?


num = int(input("Enter a number to display its multiplication table: "))

i = 1


while i <= 12:
    result = num * i
    print(num, "x", i, "=", result)
    i += 1
