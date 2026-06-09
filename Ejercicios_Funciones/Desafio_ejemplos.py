temperaturas = {"Santiago": [15.5, 18.2, 14.0], "Valparaíso": [12.0, 13.5, 11.8]}

def promedio_temperatura(temperaturas):
    for comuna, registros in temperaturas.items():
        if registros:
            promedio = sum(registros) / len(registros)
            print(f"{comuna}: promedio = {promedio:.2f}°C")
        else:
            print(f"{comuna}: no hay temperaturas registradas")


if __name__ == "__main__":
    promedio_temperatura(temperaturas)


Auditoria_de_Gastos_de_Viaje =  {}

def Promediod_de_gastos(Auditoria_de_Gastos_de_Viaje):
    while True:
        try:
            Nombre = str(input("Ingrese nombre: "))
            break
        except ValueError:
            print("Ingrese nombre correcto, sin numeros")