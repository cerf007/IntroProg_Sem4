#Algoritmo para calcular el porcentaje de mujeres y varones en un aula.
print("Bienvenido a tu calculadora de porcentaje de hombres y mujeres de un salon")
numero_varones = int(input("Ingrese el número de varones en la sección: "))
numero_mujeres = int(input("Ingrese el número de mujeres en la sección: "))
total = numero_mujeres + numero_varones
porcentaje_varones = float((numero_varones * 100)/total)
porcentaje_mujeres = float((numero_mujeres * 100)/total)
print(f"El porcentaje de varones es: {porcentaje_varones:.2f}%")
print(f"El porcentaje de mujeres es: {porcentaje_mujeres:.2f}%")