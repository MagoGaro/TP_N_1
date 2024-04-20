#Enunciado
"""11. Programe una aplicación de consola que muestre los primeros 5 caracteres de una cadena 
de texto ingresada por el usuario. """
#Código
texto = input("Ingrese una palabra de 5 caracteres o mas: ")

#print(f"los primeros 5 caracteres son: {texto[:5]}")

primeros5 = ""
for i in range(5):
    primeros5 += texto[i]

print(f"los primeros 5 caracteres son: {primeros5}")    
