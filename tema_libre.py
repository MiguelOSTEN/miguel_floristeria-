import os
import json

class Floristeria:
    def __init__(self, archivo):
        self.archivo = archivo
        self.inventario = self.cargar_inventario()

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON. Iniciando con un inventario vacío.")
                return []
        else:
            return []

    def guardar_inventario(self):
        with open(self.archivo, 'w') as file:
            json.dump(self.inventario, file, indent=4)

    def agregar_flor(self, nombre, tipo, cantidad, precio):
        flor = {
            'nombre': nombre,
            'tipo': tipo,
            'cantidad': cantidad,
            'precio': precio
        }
        self.inventario.append(flor)
        self.guardar_inventario()
        print(f"La flor '{nombre}' ha sido agregada.")

    def eliminar_flor(self, nombre):
        for flor in self.inventario:
            if flor['nombre'] == nombre:
                self.inventario.remove(flor)
                self.guardar_inventario()
                print(f"La flor '{nombre}' ha sido eliminada.")
                return
        print(f"La flor '{nombre}' no se encontró en el inventario.")

    def buscar_flor(self, nombre):
        for flor in self.inventario:
            if flor['nombre'] == nombre:
                print(f"Flor encontrada: {flor}")
                return flor
        print(f"La flor '{nombre}' no se encontró en el inventario.")
        return None

    def mostrar_inventario(self):
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            print("Inventario de la floristería:")
            matriz_inventario = [["Nombre", "Tipo", "Cantidad", "Precio"]]
            for flor in self.inventario:
                matriz_inventario.append([flor['nombre'], flor['tipo'], flor['cantidad'], flor['precio']])
            for fila in matriz_inventario:
                print(fila)

def limpiar_pantalla():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def mostrar_menu():
    print("\n--- Menú de Floristería ---")
    print("1. Agregar flor")
    print("2. Eliminar flor")
    print("3. Buscar flor")
    print("4. Mostrar inventario")
    print("6. Salir")
    return input("Elige una opción: ")

def main():
    floristeria = Floristeria("inventario_floristeria.json")

    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            nombre = input("Nombre de la flor: ")
            tipo = input("Tipo de la flor: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            floristeria.agregar_flor(nombre, tipo, cantidad, precio)
        elif opcion == '2':
            nombre = input("Nombre de la flor a eliminar: ")
            floristeria.eliminar_flor(nombre)
        elif opcion == '3':
            nombre = input("Nombre de la flor a buscar: ")
            floristeria.buscar_flor(nombre)
        elif opcion == '4':
            floristeria.mostrar_inventario()
        elif opcion == '5':
            limpiar_pantalla()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 6.")

if __name__ == "__main__":
    main()
