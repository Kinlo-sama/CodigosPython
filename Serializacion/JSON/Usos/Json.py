import json

datos = {
    "Nombre": "Leonardo",
    "Edad":21,
    "Ciudad": "Veracruz"
    }

with open("Datos.json","w") as archivo:
    json.dump(datos,archivo)
