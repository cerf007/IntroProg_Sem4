#Solicita el precio de 3 productos y muestra:
#Subtotal
#IVA (15%)
#Total a pagar

producto1 = float(input("Ingrrese el valor del primer del producto: "))
producto2 = float(input("Ingrrese el valor del segundo del producto: "))
producto3 = float(input("Ingrrese el valor del tercer del producto: "))

subtotal = producto1 + producto2 + producto3
iva = subtotal*(15/100)
total_pagar = subtotal + iva
print(f"Subtotal \t IVA \t Total a pagar")
print(f"{subtotal:<10} \t {iva:<10} \t {total_pagar:<10}")