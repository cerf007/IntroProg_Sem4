#Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los tiempos obtenidos. 
# Determinar el tiempo promedio que la persona tarda en recorrer la ruta en una semana cualquiera
print("Bienvenido a tu calculadora de promedio de tiempo")
dia_1 = float(input("Ingrese el tiempo en minutos en el que recorrió el trayecto en su primer dia (lunes): "))
dia_2 = float(input("Ingrese el tiempo en minutos en el que recorrió el trayecto en su segundo dia (miércoles): "))
dia_3 = float(input("Ingrese el tiempo en minutos en el que recorrió el trayecto en su tercer dia (viernes): "))
promedio = (dia_1 + dia_2 + dia_3)/3
print(f"Su tiempo promedio de esos 3 días en una semana cualquiera en minutos es de {promedio:.2f}")