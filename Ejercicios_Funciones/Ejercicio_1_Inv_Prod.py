def agregar_productos(productos):


productos = {
}

while True:

    print('''
    ********Menu********
    1. Agregar producto
    2. Mostrar productos
    3. Buscar producto
    4. Producto mas caro
    5. Salir''')

    Opcion = int(input("Seleccione una opcion del menu: "))

    contador = 0

    if Opcion == 1: 
        Cantidad = int(input("Ingrese la cantidad de productos a guardar: "))
        for contador in range(Cantidad):
            nombre = input("ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad en inventario: "))
            precio = float(input("Ingrese valor de producto: "))
            producto = [nombre, cantidad , precio]









