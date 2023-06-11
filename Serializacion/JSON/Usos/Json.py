import json
dato = []

with open("Datos.json","a") as archivo:
    while True:
        datos = {}
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

    json.dump(dato,archivo,indent = 4)#No se que me causa ver lo hermoso que se ve indexado con 4 espacios 

