import json

with open("Datos.json","r") as archivo:
    datos = json.load(archivo)
    print(datos)

'''
    contenido = archivo.read()

datos = json.loads(contenido)

for dato in datos:
    nombre = dato["Nombre"]
    edad = dato["Edad"]
    ciudad = dato["Ciudad"]
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}\n")
Para ver mejor la info.
'''

