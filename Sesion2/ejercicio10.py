#Calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre su salario actual 
# y un descuento de 2,5% por servicios.
print("Hola, a continuación calcularemos tu nuevo salario en base a un incremento del 8%")
print("Asi mismo, se realizara un descuento del 2.5% por servicios")
salario_original = float(input("Por favor, ingrese su salario actual: "))

aumento = float((salario_original) *8/100)
salario_incrementado = float(salario_original + aumento)
descuento = float((salario_incrementado) * 2.5/100)
salario_final = float(salario_incrementado - descuento)

print(f"Su salario incicial era de: {salario_original:.2f}")
print(f"Su salario con un incremento del 8% es de: {salario_incrementado:.2f}")
print(f"Pero con un descuento de 2.5% por servicios su salario final es: {salario_final:.2f}")
