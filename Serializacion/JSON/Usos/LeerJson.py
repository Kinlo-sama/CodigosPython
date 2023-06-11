import json

with open("Datos.json","r") as archivo:
    contenido = archivo.read()

datos = json.loads(contenido)

for dato in datos:
    nombre = dato["Nombre"]
    edad = dato["Edad"]
    ciudad = dato["Ciudad"]
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}\n")

print("Enter para salir")
input()

