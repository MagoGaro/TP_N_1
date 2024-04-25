#Enunciado
""" 5. Escriba un programa que pida al usuario que ingrese 3 números. Sume los dos primeros y 
luego multiplique este total por el tercero. Mostrar la respuesta 
en pantalla de la siguiente forma: “La respuesta es XX """

#Codigo 
num1 = input("Ingrese el primer numero: ")
num2 = input("Ingrese el segundo numero: ")
num3 = input("Ingrese el tercer numero: ")

suma = (int(num1) + int(num2)) * int(num3)
print ("La respuesta es:",suma)
