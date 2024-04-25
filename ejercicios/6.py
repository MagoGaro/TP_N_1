#Enunciado
"""6. Programe una aplicación de consola que pregunte el precio total de la cuenta, luego 
pregunte cuántos comensales hay. A continuación deberá dividir la cuenta total por el 
número de comensales y mostrar cuánto debe pagar cada persona."""

#Codigo
precioTotal = input("Ingrese importe total de su cuenta: ")
comensales = input("cantidad de personas que comieron: ")

total = float(precioTotal) / int(comensales)
print("Total por persona :", round(total,2))
