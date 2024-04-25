#Enunciado
"""12. Pedir al usuario que ingrese una fecha en formato dd/mm/aaaa e imprimir en pantalla el 
día, mes y año. Ej: 
Usuario ingresa: 17/05/1985
Programa imprime: Día: 17, Mes: 05 y Año: 1985"""

#Código
fecha = input("ingrese una fecha en formato dd/mm/aaaa: ")

print("Dia: "+fecha[:2]+" Mes: "+fecha[3:5] +" Año: "+fecha[6:])