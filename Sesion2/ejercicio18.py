#El dueño de una tienda compra un artículo a un precio determinado. 
# Obtener el precio en que lo debe vender para obtener una ganancia del 30%.
precio_compra = float(input("Ingrese el precio de compra del articulo: "))
ganancia = (precio_compra) * 30/100
precio_venta = precio_compra + ganancia
print(f"Para sacar un 30% de ganancia a un prouducto de {precio_compra} deberá venderse a {precio_venta} ")