'''productos = {
    "Mouse":"[10,1500]",
    "Teclado" : [5,2500],
    "Monitor" : [3,180000]
}'''
def agregar_producto(productos):
    nombre = input("Nombre del producto: ").strip().lower()

    if nombre == "":
        print("El nombre no puede ser vacío")
        return
    
    if nombre in productos:
        print("El producto ya existe!")
        return

    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese precio $: "))

    productos[nombre] = [stock,precio]
    print("Producto agregado correctamente!")

def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return

    for nombre in productos:
        print(nombre,"-Stock: ",productos[nombre][0],"-Precio : $",productos[nombre][1])

def buscar_producto(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    nombre = input("Ingrese nombre del producto a buscar: ").strip().lower()

    if nombre in productos:
        print("Producto encontrado!")
        print(f"Stock: {productos[nombre][0]}")
        print(f"Precio $: {productos[nombre][1]}")

    else:
        print("Producto no existe o esta agotado!")

def producto_mas_caro(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
    
    mayor = 0
    nombreMayor = ""
    for nombre in productos:
        precio = productos[nombre][1]

        if precio > mayor:
            mayor = precio
            nombreMayor = nombre

    print(f"Producto mas caro es: {nombreMayor}")
    print(f"Su precio es: ${mayor}")