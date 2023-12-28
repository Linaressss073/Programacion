'''
Calcular el monto a pagar por un artículo si se tiene como
datos de entrada la cantidad de docenas que compra y el costo
por unidad de este artículo.

'''

print("\n========================================")
print("Bienvenido a la calculadora de docenas")
print("========================================\n")


#Entradas

producto = ""
precio = 0
docena = 12

#Inputs
producto = str(input("Ingrese el nombre del producto: "))
precio = float(input("Ingrese el valor del producto: "))

print("\nEl nombre del producto es:" , producto , "\nEl valor de UN producto es: " , precio , "\n")

print("Multiplicado por doce es decir , una decena es total a: " , precio*docena , "\n")



