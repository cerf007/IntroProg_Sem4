#En un hospital existen 3 áreas: Urgencias, Pediatría y Traumatología. 
# El presupuesto anual del hospital se reparte de la siguiente manera:
#urgencias = 37%
#pediatria = 42%
#traumatología = 21%
presupuesto = float(input("Ingrese el presupuesto del hospital: "))
urgencias = (presupuesto) * 37/100
pediatria = (presupuesto) * 42/100
traumatologia = (presupuesto) * 21/100
print(f"El presupuesto para urgencias será de: {urgencias:.2f}")
print(f"El presupuesto para pediatría será de: {pediatria:.2f}")
print(f"El presupuesto para traumatología será de: {traumatologia:.2f}")