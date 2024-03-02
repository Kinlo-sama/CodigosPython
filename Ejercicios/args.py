import sys

valores = sys.argv[1:]
suma = 0
for i in valores:
	suma += int(i)
media = suma / len(valores)
print(f'{media:.2f}')
