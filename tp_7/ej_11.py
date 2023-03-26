
# Cargar dos listas de números A y B con N números al azar entre 1 y 100, donde N se ingresa por teclado. 
# Mostrar ambas listas por pantalla. 
# Luego construir e imprimir tres nuevas listas C, D y E que contengan:
#  - La concatenación de los valores pares de A con los impares de B. 
#    (valores pares o valores impares se refiere a los elementos propiamente dichos y no a sus posiciones).
#  - La concatenación de los valores impares de A con el reverso de los valores pares de B. 
#  - La intercalación de los elementos de A y B.


from random import randint


n = int(input("Ingrese el largo de las listas: "))

list_a = [randint(1, 100) for _ in range(n)]
list_b = [randint(1, 100) for _ in range(n)]

print(f"Lista A: {list_a}")
print(f"Lista B: {list_b}")

list_a_evens = [n for n in list_a if n % 2 == 0]
list_a_odds = [n for n in list_a if n % 2 != 0]
list_b_evens = [n for n in list_b if n % 2 == 0]
list_b_odds = [n for n in list_b if n % 2 != 0]


list_c = list_a_evens + list_b_odds
list_d = list_a_odds + list_b_evens[::-1]

list_e = [[list_a[i], list_b[i]] for i in range(len(list_b))]
list_e = [j for i in list_e for j in i]


print(f"Lista C: {list_c}")
print(f"Lista D: {list_d}")
print(f"Lista E: {list_e}")
