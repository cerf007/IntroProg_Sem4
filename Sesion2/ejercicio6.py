#Crea un algoritmo que, dado el año de nacimiento de una persona y el año actual,
##calcule su edad actual y su edad en 10 años.
print("Bienvenido a tu calculadora de edades actuales y en 10 años despues")
actualidad = int(input("Ingrese el año actual: "))
nacimiento =  int(input("Por favor, introduzca el año de su nacimiento: "))
edad = actualidad - nacimiento
edad_posterior = edad + 10
print(f"Su edad actual es {edad} y su edad en 10 años será {edad_posterior} ")