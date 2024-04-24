import funcionalidad as f

class MenuItem:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def display(self):
        print(f"{self.name}")

    def execute(self):
        self.action()

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        for i, item in enumerate(self.items):
            print(f"{i + 1}. {item.name}")
        print("\n")

    def get_user_choice(self):
        while True:
            choice = input("Seleccione una opción (1-" + str(len(self.items)) + "): ")
            print("\n")
            if choice.isdigit() and 1 <= int(choice) <= len(self.items):
                return int(choice) - 1
            else:
                print("Opción invalida. Ingrese un número entre 1 y", len(self.items))

    def run(self):
        while True:
            self.display()
            choice = self.get_user_choice()
            self.items[choice].execute()
            if self.items[choice].name == "Salir":
                break

def menu_principal():
    menu = Menu()
    
    menu.add_item(MenuItem("Ver Codigo Ejercicio", lambda: menu_ver.run()))
    menu.add_item(MenuItem("Ejecutar Ejercicio", lambda: menu_ejecutar.run()))
    menu.add_item(MenuItem("Autores", lambda: f.autores()))
    menu.add_item(MenuItem("Exit", lambda: exit()))

    return menu

menup = menu_principal()

def menu1():
    menu = Menu()
    
    menu.add_item(MenuItem("Ejercicio 1", lambda: f.read_file("1.py")))
    menu.add_item(MenuItem("Ejercicio 2", lambda: f.read_file("2.py")))
    menu.add_item(MenuItem("Ejercicio 3", lambda: f.read_file("3.py")))
    menu.add_item(MenuItem("Ejercicio 4", lambda: f.read_file("4.py")))
    menu.add_item(MenuItem("Ejercicio 5", lambda: f.read_file("5.py")))
    menu.add_item(MenuItem("Ejercicio 6", lambda: f.read_file("6.py")))
    menu.add_item(MenuItem("Ejercicio 7", lambda: f.read_file("7.py")))
    menu.add_item(MenuItem("Ejercicio 8", lambda: f.read_file("8.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.read_file("9.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.read_file("10.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.read_file("11.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.read_file("12.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.read_file("13.py")))
    menu.add_item(MenuItem("Menu Principal",lambda: menup.run()))
    
    return menu

def menu2():
    menu = Menu()
    
    menu.add_item(MenuItem("Ejercicio 1", lambda: f.execute_script("1.py")))
    menu.add_item(MenuItem("Ejercicio 2", lambda: f.execute_script("2.py")))
    menu.add_item(MenuItem("Ejercicio 3", lambda: f.execute_script("3.py")))
    menu.add_item(MenuItem("Ejercicio 4", lambda: f.execute_script("4.py")))
    menu.add_item(MenuItem("Ejercicio 5", lambda: f.execute_script("5.py")))
    menu.add_item(MenuItem("Ejercicio 6", lambda: f.execute_script("6.py")))
    menu.add_item(MenuItem("Ejercicio 7", lambda: f.execute_script("7.py")))
    menu.add_item(MenuItem("Ejercicio 8", lambda: f.execute_script("8.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.execute_script("9.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.execute_script("10.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.execute_script("11.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.execute_script("12.py")))
    menu.add_item(MenuItem("Ejercicio 9", lambda: f.execute_script("13.py")))
    menu.add_item(MenuItem("Menu Principal",lambda: menup.run()))
    
    return menu

menu_ver = menu1()
menu_ejecutar = menu2()
