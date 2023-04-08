#Empezamos con codigos sencillos para practicar desde la documentacion de la pagina oficial de Python
#definamos la funcion fib ->Serie de Fibonacci
def fib(n):
  a,b = 0,1#multiple asignacion, se asignan con forme a su declaracion osea a -> 0 y b -> 1
  for i in range(n): #Este for va de 0 hasta n-1
    print(a,end = " ")#Imprimos el elemento i de la serie de fibonacci
    a,b = b, a + b#Aqui aplicamos la regla de la serie de fibonaci el numero siguiente sera la suma entre el numero actual y el numero anterior
    #La asignacion aqui se da sin tomar en cuenta la nueva asignacion de a osea que en la primera iteracion la asignacion de b sera 0 + 1 y no 1 + 1
  
fib(10)
