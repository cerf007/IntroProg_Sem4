#Calcula la calificación final de un estudiante con ponderaciones:
#Tareas: 30%
#Examen parcial: 30%
#Examen final: 40%
print("Bienvenido a tu calculadora de la calificación final")
print("Las tareas equivalen el 30%")
print("El examen parcial equivale un 30%")
print("El examen final equivale el 40%")
tareas = float(input("Ingrese la calificación de las tareas: "))
examen_parcial = float(input("Ingrese la calificación del examen parcial: "))
examen_final = float(input("Ingrese la calificación del examen final: "))

tarea_pond = (tareas) * 30/100
examen_parcial_pond = (examen_parcial) * 30/100
examen_final_pond = (examen_final) * 40/100
nota_final = (tarea_pond + examen_parcial_pond + examen_final_pond)
print(f"Tu nota final es: {nota_final:.2f}")