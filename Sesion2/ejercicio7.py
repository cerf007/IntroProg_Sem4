#Diseña un algoritmo que intercambie el valor de dos variables numéricas. 
# Usa una variable auxiliar para hacerlo.
variable_a = 5
variable_b = 10

print("Antes de intercambio:")
print(f"la variable a es: {variable_a}")
print(f"la variable b es: {variable_b}")
print("=="*10)
auxiliar = variable_a
variable_a = variable_b
variable_b = auxiliar
print("=="*10)
print("Estos son las variables luego de interpolar")
print(f"La variable a es: {variable_a}")
print(f"La variable b es: {variable_b}")