#Enunciado
"""10. Escriba un programa que indique si un texto es palíndromo, es decir, se escribe igual al 
derecho que al revés. Por ejemplo: rayar, kayak, somos."""

#Codigo
texto = input("Ingrese un texto: ").lower()

#print(f"El texto {texto} es palíndromo" if texto == texto[::-1] else f"El texto {texto} no es palíndromo")

if texto == texto[::-1]:
    print("El texto "+ texto + " es palíndromo")
else:
    print("El texto "+texto+ " No es palíndromo")
