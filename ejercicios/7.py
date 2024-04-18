#Enunciado
"""7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y 
segundos son esos números de días"""

#Codigo
dias = input("cantidad de días: ")
horas = f"{dias} * 24"
minutos = eval(horas) * 60
segundos = minutos * 60
print(f"La cantidad de hora es: {eval(horas)} minutos: {minutos} segundos: {segundos}")
