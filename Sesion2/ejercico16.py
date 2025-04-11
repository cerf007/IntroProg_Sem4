# Diseñe un algoritmo que lea los datos necesarios y calcule la masa, según la formula siguiente
#(presión * volumen)/(0.37 *(temperatura + 460))\
print("Hola, bienvenido a tu calculadora de masa")
presion = float(input("Ingrese la presion: "))
volumen = float(input("Ingrese el valor del volumen: "))
temperatura = float(input("Ingrese el valor de la temperatura: "))
masa = (presion * volumen)/ (0.37 * (temperatura + 460))
print(f"La masa es {masa:.2f}")