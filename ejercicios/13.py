#Enunciado
"""13. Programe una aplicación de consola que solicite al usuario su nombre, después su apellido y
a continuación su año de nacimiento. Con esos datos deberá generar una sugerencia de 
usuario y contraseña. Por ejemplo: nombre: Martín, apellido: Francisconi, Año nacimiento: 
1985 -> Usuario: mfrancisconi, Contraseña: mf.1985."""

#Código
nombre = input("Ingrese su nombre: ").lower()
apellido = input("Ingrese su apellido: ").lower()
anio_nacimiento = input("Ingrese su año de nacimiento: ")

usuario = nombre[0:1] + apellido
contrasena = nombre[0:1] + apellido[0:1] + "." + anio_nacimiento

print("Usuario: "+usuario+'\n'+"Contrasena: "+contrasena)


