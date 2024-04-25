#Enunciado
"""7. Pida al usuario un número x de días y luego mostrar por pantalla cuántas horas, minutos y 
segundos son esos números de días"""

#Codigo
dias = input("cantidad de días: ")

horas = int(dias) * 24
minutos = horas * 60
segundos = minutos * 60
print(dias,"días son:", horas,"Horas" ,minutos,"Minutos",segundos,"Segundos")
