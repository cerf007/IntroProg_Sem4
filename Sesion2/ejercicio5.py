#Algoritmo que calcule el porcentaje de un número dado. Ejemplo: ¿qué es el 15% de 200?
print("Bienvenido a tu calculadora de porcentaje")
numero = float(input("Por favor, ingrese el numero el cual desea calcular: "))
porcentaje = float(input("Por favor, ingrese el porcentaje con que desea calcular su número: "))
numero_porcentuado = numero * porcentaje/100
print(f"El numero {numero}  con un porcentaje de {porcentaje}% es igual a {numero_porcentuado} ")