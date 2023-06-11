import json
dato = []
datos = {}
with open("Datos.json","a") as archivo:
    while True:
        nombre = input("Nombre:")
        edad = int(input("Edad:"))
        ciudad = input("Ciudad:")
        datos["Nombre"] = nombre
        datos["Edad"] = edad
        datos["Ciudad"] = ciudad
        dato.append(datos)
        op = int(input("Desea continuar- 1/si 2/no "))
        if op == 2:
            break

    json.dump(dato,archivo)

