
# Se desea analizar cuántos autos circulan con patente con numeración par y cuántos con numeración impar en un día. 
# Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar 
# -1 e informe cuántos vehículos pasaron con numeración par y cuántos con numeración impar.


odd_plates = 0
even_plates = 0


while 1:
    plate_number = int(input("Ingrese la terminación de la patente [0-9] (-1 para salir): "))

    if plate_number == -1:
        break
    elif not 9 >= plate_number >= 0:
        print("La placa ingresada es invalida")
    elif plate_number % 2 == 0:
        even_plates += 1
    else:
        odd_plates += 1

print()
print(f"En el dia pasaron {even_plates} placas pares.")
print(f"En el dia pasaron {odd_plates} placas impares.")
