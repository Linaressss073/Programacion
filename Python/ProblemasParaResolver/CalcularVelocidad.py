'''

4. Dado el tiempo en segundos y la distancia en metros de un
móvil, ingresados por teclado, calcule la velocidad
correspondiente.

'''

#Variables

tiempo = 0
distancia = 0  
velocidad = 0

print("===============================================\nBienvenidos\n===============================================")

tiempo = float(input("Ingrese tiempo en segundos: "))
print("El tiempo ingresado es: " , tiempo , " Segundos")

distancia = float(input("Ingrese distancia en METROS: "))
print("La distancia ingrsada es: " , distancia , " En metros")

velocidad = distancia/tiempo

print("La velocidad total es: " , velocidad , " m/s")