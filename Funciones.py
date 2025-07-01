

producto=[]

def registrostock(codigo, nombre, cantidad, precio):
    if codigo>=0:
        if nombre==len(input())>2:
            if cantidad>=0:
                if precio>0:
                    datos={
                        "codigo":codigo,
                        "nombre":nombre,
                        "cantidad":cantidad,
                        "precio":precio
                    }
                    producto.append(datos)
                    print("Producto(s) agregado(s)")
                else:
                    print("Cantidad no valida. precio mayor que 0")
            else:
                ("Cantidad stocks no valido. Ingrese número positivo")
        else:
            print("Necesita ser 3 caracteres o más")
    else:
        print("Codigo no valido")

def listaProducto(clave):
    clave=registrostock
    for i in range(clave):
        (clave(codigo="codigo"))
        return i
    return -i

def buscarProducto(producto):
    while True (len(listaProducto))>0:
        indice=producto
        if input()=="codigo":
            listaProducto
            print(f"Codigo: {indice[producto]["codigo"]} Nombre: {indice[producto]["nombre"]} Cantidad: {indice[producto]["cantidad"]} Precio {indice[producto]["precio"]}")
            return
        else:
            print("No valido")
    else:
        print("No existente")

def eliminarProducto(producto):
    while True (len(listaProducto))>=0:
        if input()=="codigo":
            registrostock.pop(producto)
            print("Producto eliminado")
    else:
        print("Producto no encontrado")