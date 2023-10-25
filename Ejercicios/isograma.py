cadena = input("Cadena a verficar:")
iso = True
for i in cadena:
	if cadena.count(i) != 1:
		iso = False

if iso:
	print("Isograma")
else:
	print("No isograma")

