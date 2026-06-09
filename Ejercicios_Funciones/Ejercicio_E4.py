
'''Usuario = {
"Pedro": [F, Contraseña]}'''

usuarios = {}

def agregar_usuario(usuarios):
    print("\n*** Agregando nuevo usuario ***")
    nombre_de_usuario = input("Agrege nombre de usuario: ").strip().title()
    if nombre_de_usuario == "":
        print("Nombre no puede estar vacio. ingrese un nombre")
        return
    if nombre_de_usuario in usuarios:
        print('''Nombre ya exite,
              intente agregando segundo nombre, segundo apellido o nickname''')
        return
    for letra in nombre_de_usuario:
        if letra.isdigit():
            return
    
    
    
    

    ingresar_sexo = str(input("Ingrese sexo: F / M / C")).upper()
    if ingresar_sexo == "":
        print("Nombre no puede estar vacio. ingrese un nombre")
        return

        

while True:
    print('''
    MENU PRINCIPAL
    1.- Ingresar usuario.
    2.- Buscar usuario.
    3.- Eliminar usuario.
    4.- Salir
    ''')
    while True:
        try:
            Opcion = int(input("Ingrese un numero de opcion en el menu: "))
            if 1 <= Opcion <= 4:
                break
            print("Opcion no valida, Ingrese una opcion valida mostrada en el menu")
        except ValueError:
            print("Letras no permitidas, Ingrese un numero valido mostrado en el menu")

    if Opcion == 1:
        agregar_usuario(usuarios)
    elif Opcion == 2:
        print("")
    elif Opcion == 3:
        print("")
    elif Opcion == 4:
        print("Saliendo del sistema...")
        
    else:
        print("seleccione una opcion valida en el menu")
