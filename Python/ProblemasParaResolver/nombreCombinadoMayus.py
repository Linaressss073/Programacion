# Ejercicio

#Escribir un programa que pregunte el nombre completo 
#del usuario en la consola y después muestre por pantalla el
#nombre completo del usuario tres veces,
#una con todas las letras minúsculas, otra con todas 
#las letras mayúsculas y otra solo con la primera letra del 
#nombre y de los apellidos en mayúscula. 
#El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.


nombre = ""

print("\n==============================")

nombre= str(input("Ingresa tu nombre en mayusculas , minuscalas o combinado el programa se encargara de todo :=) "))

print(nombre.lower())
print(nombre.upper())        
print(nombre.title())

print("===============================\n")
