#Dado un total de cuenta y un porcentaje de propina (por ejemplo, 10%), 
#alcula cuánto dejar de propina
print("Bienvenido a tu calculadora de propinas")
cuenta = float(input("Ingrese la cuenta de la comida: "))
porcentaje = float(input("Ingrese el porcentaje de la propina: "))
propina =  cuenta * (porcentaje/100)
print("===="*10)
print("===="*10)
print("Cuenta \t propina")
print(f"{cuenta:>4} \t {propina:>4}")
print("===="*10)
print("===="*10)
print(f"La propina recomendada por una comida de {cuenta:.2f} es de {propina:.2f}")