#Enunciado
"""12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el 
día, mes y año. Ej: 
Usuario ingresa: 17/05/1985
Programa imprime: Día: 17, Mes: 05 y Año: 1985"""
#Código
fecha = input("ingrese una fecha en formato: dd/mm/aaaa ")
calendario = fecha.split("/")

print(f"Dia: {calendario[0]} Mes:{calendario[1]} Año: {calendario[2]}")
