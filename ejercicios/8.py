#Enunciado
"""8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para 
luego imprimir por pantalla la superficie total."""

#Codigo
base = input("Ingrese para la base: ")
altura = input("Ingrese para la altura: ")

superficie = (float(base) * float(altura)) / 2
print("La superficie total es:" ,superficie,"m²")
