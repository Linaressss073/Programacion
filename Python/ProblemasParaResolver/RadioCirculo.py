'''
1. Dado el radio de un círculo, calcule el volumen de la esfera
correspondiente.
'''

# Variables
#Inicializadas en cero para evitar residuos
volumen = 0
radio = 0

pi = 3.14156


print(" ===========================================")
print("Bienvenido al programa de calcular volumen de un circulo")
print(" ===========================================")

radio = float(input("Radio: "))
volumen = 4/3 * pi*pow(radio,3)

print("El volumen de la esfera es: " , volumen)
print(" ===========================================")
