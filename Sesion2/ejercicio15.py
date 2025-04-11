#Pide una edad actual y muestra qué edad tendrá el usuario dentro de 5, 10 y 20 años.
edad = int(input("Ingrese su edad actual: "))
edad_5 = edad +5
edad_10 = edad + 10
edad_20 = edad + 20
print("Edad en 5 años \t Edad en 10 años \t Edad en 20 años")
print(f"{edad_5:>10} \t {edad:>10} \t {edad_20:>10}")