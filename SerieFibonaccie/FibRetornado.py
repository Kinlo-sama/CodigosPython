#Ahora en ves de imprimir la serie de Fibonacci, lo guardaremos en una lista para poder manipularla a nuestro gusto
def fibReturn(n):
    resultado = []
    a,b = 0 , 1
    for i in range(n):
        resultado.append(a)
        a,b = b, a + b
    return resultado

listaFib = fibReturn(10)
for item in listaFib:
    print(item,end = " ")
