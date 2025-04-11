#Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio
# la fórmula es: pulsaciones = (220 - edad)/10
print("Bienvenido a tu calculadora de pulsaciones")
edad = int(input("Ingrese su edad actual: "))
pulsaciones = (220 - edad)/10
print(f"El número de pulsaciones que debe tener cada 10 segundos a la edad de {edad} es de {pulsaciones:.0f}")