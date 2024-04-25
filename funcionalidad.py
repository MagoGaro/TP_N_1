import os, subprocess

def limpiar():
    os.system("clear")
    
def banner_bienvenida():
    print("""\n 
    Hola ! bienvenidos a la presentación del
        Trabajo Practico  N°1\n""")

def read_file(filename):
    try:
        filepath = os.path.join('./ejercicios/', filename)
        with open(filepath, 'r', encoding="utf-8") as f:
            content = f.read()
            print(content)
            print("\n")
    except FileNotFoundError as e:
        print(f"Error: Archivo No Encontrado: {filename}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    

def execute_script(script_path):
    try:
        print("Ejecutando Script ...")
        print("\n")
        subprocess.run(['py', "./ejercicios/"+script_path])
        #cambiar py por el comando que usen para ejecutar
        print("\n")
        print("Finaliza Ejecición ...")
        print("\n")
    except FileNotFoundError as e:
        print(f"Error: Archivo No Encontrado: {script_path}")
    except Exception as e:
        print(f"Error Al Ejecutar el Script: {e}")
        
def autores():
    limpiar()
    print("""\n 
            ################################
                 Trabajo Practico N° 1
                   
                       Autores:
              Maria Julieta Gutierrez Castro
              Maria Belen Rabel Zarate
              Gabriel Sebastian Roman
            ################################
     \n """)
