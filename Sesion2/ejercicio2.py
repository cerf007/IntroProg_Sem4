#Declara tres variables numéricas y evalúa la siguiente expresión: (a + b) * c / 2.
#Muestra el resultado y explica cómo se evalúa la expresión paso a paso
print("Bienvenido a tu calculadora de la expresión (a + b) * c / 2")
variable_a = float(input("Ingrese el valor númerico a: "))
variable_b = float(input("Ingrese el valor númerico b: "))
variable_c = float(input("Ingrese el valor númerico c: "))
operacion = float(variable_a + variable_b) * variable_c / 2
print("Primero se realiza la suma de varibale a", variable_a, "con la variable b", variable_b)
print("Luego, del resultado del parenteris se multiplica con la varible c", variable_c)
print("Por último, se divide el todo eel resulatado entre 2 para obtener", operacion)