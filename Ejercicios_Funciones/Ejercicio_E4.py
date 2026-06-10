
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
    Generos = ["F", "M"]
    while True:
        try:
            ingresar_sexo = str(input("Ingrese sexo: F / M: ")).upper()
            if ingresar_sexo in Generos:
                print("Sexo guardado exitosamente")
                break
            else:
                print("Sexo debe ser solo M / F")
        except ValueError:
            print("Debe Seleccionar solo F ó M")
   
    while True:
        ingresar_contraseña = input("Ingrese su contraseña: ")
        contraseña_valida = True

        if len(ingresar_contraseña) < 8:
            print("La contraseña debe tener al menos 8 caracteres.")
            contraseña_valida = False
            
        if " " in ingresar_contraseña:
            print("La contraseña no puede contener espacios en blanco.")
            contraseña_valida = False
            
        numero = False
        letra = False
        
        for caracter in ingresar_contraseña:
            if caracter.isdigit():
                numero = True
            if caracter.isalpha():
                letra = True
                
        if not numero or not letra:
            print("La contraseña debe contener al menos una letra y un número.")
            contraseña_valida = False
        
        if contraseña_valida: 
            usuarios[nombre_de_usuario] = [ingresar_sexo, ingresar_contraseña]
            print(f"\n¡Usuario '{nombre_de_usuario}' registrado con exito!")
            break
def buscar_usuario(usuarios):
    if not usuarios:
        print("No existen usuarios, agrege usuarios primero.")
        return

    nombre_de_usuario = input("Ingrese nombre de usuario que busca: ").strip().title()

    if nombre_de_usuario not in usuarios:
        print(f"El usuario '{nombre_de_usuario}' no existe.")
        return

    usuario = usuarios[nombre_de_usuario]
    
    print("\nUsuario encontrado")
    print("Nombre:", nombre_de_usuario, "- Sexo:", usuario[0], "- Contraseña:", usuario[1])


def eliminar_usuario(usuarios):
    if not usuarios:
        print("No existen usuarios, agrege usuarios primero.")
        return

    nombre_de_usuario = input("Ingrese el nombre de usuario a eliminar: ").strip().title()
    if nombre_de_usuario in usuarios:
        del usuarios[nombre_de_usuario]
        print("Usuario eliminado!")
    else:
        print(f" El usuario {nombre_de_usuario} no existe")

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
        buscar_usuario(usuarios)
    elif Opcion == 3:
        eliminar_usuario(usuarios)
    elif Opcion == 4:
        print("Saliendo del sistema...")
        
    else:
        print("seleccione una opcion valida en el menu")
