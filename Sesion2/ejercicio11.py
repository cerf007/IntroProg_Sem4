#Solicita el nombre, precio de un producto y un porcentaje de descuento. 
# Muestra el nombre del producto y precio final luego de aplicar el descuento.
nombre_producto = input("Introduzca el nombre del producto: ")
precio_producto = float(input("Introduzca el valor del producto: "))
cantidad = float(input("Ingrese la cantidad a comprar: "))
porcentaje = float(input("Ingrese un porcentaje de descuento: "))
gasto = precio_producto * cantidad
descuento = ((gasto) *porcentaje/100)
total = gasto - descuento
print("===="*10)
print("===="*10)
print(f"Nombre de producto \t Precio \t Cantidad \t descuento \t Total")
print(f"{nombre_producto:>10} \t{precio_producto:>10} \t {cantidad:>10} \t {descuento:>10} \t {total:>10}")