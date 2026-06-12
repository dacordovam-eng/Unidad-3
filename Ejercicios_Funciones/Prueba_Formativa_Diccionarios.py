Usuarios = {
    "juan" : ["M", "AJKHSKVS455154"]
}""

#Funciones

def ingresar_usuario():
    nombre = input("Ingrese nombre de usuario")

    if nombre in Usuarios

# PARTE PPL

Usuarios = {}

while True:
    print("---Menu Principal"---)
    print("1. Ingresar usuario")
    print("2. Buscar usuario")
    print("3. Eliminar usuario")
    print("4. Salir")


    while True:
        try: 
            op = int(input("Ingrese su opcion: "))
            break
        except ValueError:
            print("por favor ingrese una opcion valida")

    if op == 1:
        ingresar_usuario()
    elif op == 2:
        buscar_usuario()
    elif op == 3:
        eliminar_usuario()
    elif op == 4:
        print("Saliendo")
        break
    else:
        print("Por favor ingrese un valor entre 1 y 4")