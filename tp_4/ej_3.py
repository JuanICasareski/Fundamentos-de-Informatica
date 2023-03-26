
# Desarrollar un programa que imprima la suma de los números impares comprendidos entre 42 y 176.


inital_number = 42
final_number = 176
curr_number = inital_number + 1
total_count = 0


while curr_number < final_number:
    if curr_number % 2 != 0:
        total_count += curr_number
    
    curr_number += 1

print(f"La suma de los números impares entre {inital_number} y {final_number} es {total_count}")
 