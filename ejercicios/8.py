#Enunciado
"""8. Escriba un programa que permita al usuario ingresar la base y altura de un triángulo para 
luego imprimir por pantalla la superficie total."""

#Codigo
base = input("Ingrese para la base: ")
altura = input("Ingrese para la altura: ")

superficie = f"({base} * {altura}) / 2"
print(f"La superficie total es: {eval(superficie)} m²")
