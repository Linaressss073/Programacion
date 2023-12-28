'''
Escribir un programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas el nombre
del usuario tantas veces como el número introducido.
'''

#Variables
nombre = ""
repeticiones = 0

print("\n==============================")
nombre = str(input(" Como te llamas? "))
print("==============================\n")

print("¡ Hola" , nombre , "!")

repeticiones = input("Introduce un numero para hacer las repeticiones (ENTERO) ")
print((nombre + "\n") * int(repeticiones))
