from os import system
from msvcrt import getch
from Funciones import *


while True:
    try:
        print("press")
        getch()
        system("cls")
        print("""
            ------------------------
            Sistema de Tienda
            ------------------------
            1.- Registración de items
            2.- Visualización stocks
            3.- Eliminación de items
            4._ Salir""")
        opcion=int(input("Acción a realizar: "))
        match opcion:
            case 1:
                print("Registración de objecto")
                registrostock()
            case 2:
                print("Visualización stocks")
                buscarProducto
                if buscarProducto==0:
                    print("No hay productos con stocks disponibles")
            case 3:
                print("Eliminación productos")
                eliminarProducto
            case 4:
                print
                ("Saliendo. . .")
                break
            case _:
                print("Acción no valida")

    except Exception as e:
        print(f"error. causa de bug: {e}")