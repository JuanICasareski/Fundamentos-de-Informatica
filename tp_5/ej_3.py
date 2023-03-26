
# Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
# - Aplica el precio base a la primera docena de unidades.
# - Aplica un 10% de descuento a todas las unidades entre 13 y 100.
# - Aplica un 25% de descuento a todas las unidades por encima de las 100.
# Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio base es 100. 
# El cálculo resultante sería: 100 * 12 + 90 * 88 + 75 * 130 = 18870 y el precio promedio es de 18870/230 = 82.04
# Escribir un programa que lea la cantidad solicitada de un producto y su precio base, 
# y muestre el valor total de la venta y el precio promedio por unidad. 
# El fin de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar: 
# - Cantidad de ventas realizadas total.
# - Cantidad de ventas en las que se aplicó un 10% de descuento.
# - Cantidad de ventas en las que SOLO se aplicó el precio base, es decir que no se le realizaron descuentos.


def get_total_price(units: int, base_price: int) -> tuple:
    OFF_10_PRICE = base_price * .9
    OFF_25_PRICE =  base_price * .75

    total_sales = 0
    total_base_sales = 0
    off_10_sales = 0

    if units <= 12:
        total_sales += 1
        total_base_sales += 1
        price = units * base_price

    elif units <= 100:
        total_sales += 1
        off_10_sales += 1
        price = 12 * base_price + (units - 12) * OFF_10_PRICE

    else:
        total_sales += 1
        off_10_sales += 1
        price = 12 * base_price + 88 * OFF_10_PRICE + (units - 100) * OFF_25_PRICE
    
    return price, total_sales, total_base_sales, off_10_sales


total_sales = 0
total_base_sales = 0
total_off_10_sales = 0


sales = int(input("Ingrese la cantidad de unidades vendidas (-1 para salir): "))
price = int(input("Ingrese el precio base del producto: "))

while sales != -1:
    price, all_sales, all_base_sales, all_off_10_sales = get_total_price(sales, price)

    if sales > 0:
        print(f"El precio total es de ${price}")
        print(f"El precio promedio es de ${price/sales}")

        total_sales += all_sales
        total_base_sales += all_base_sales
        total_off_10_sales += all_off_10_sales

    sales = int(input("Ingrese la cantidad de unidades vendidas (-1 para salir): "))
    if sales > 0: 
        price = int(input("Ingrese el precio base del producto: "))

print(f"Se realizaron {total_sales} ventas en total")
print(f"Se realizaron {total_base_sales} ventas con solo el precio base")
print(f"Se realizaron {total_off_10_sales} ventas con un 10% de descuento")
