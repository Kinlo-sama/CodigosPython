import random
#******************************Es mas facil escribir los string de los nombres en un txt, me refiero a estar poniendo " y cerrando ", :u
archivo = open("Numeros.txt","r")
contenido = list((archivo.read()).split())
#Quitamos los espacios y saltos de linea ^
sublista = []
sublistaAct = []
#sublista almacena las sublista de los string del archivo
for elemento in contenido:#iteramos por todo el contenido
    if elemento == '-':#buscamos la separacion
        if sublistaAct:#si la lista no esta vacia
            sublista.append(sublistaAct)#Agregamos a la sublista
            sublistaAct = []#e inicializamos de nuevo en 0 
    else:
        sublistaAct.append(elemento)#seguimos agregando
if sublistaAct:
    sublista.append(sublistaAct)#si quedaron datos aun en la listaAct

unidades = sublista[0]
deuni = sublista[1]
decenas = sublista[2]
centenas = sublista[3]
millares = sublista[4]

#************************************Comienzo del ADT Numero*****************************

class Numero:
    def __init__(self,num):#Por conveniencia usaremos str para representar al numero
        if isinstance(num,str):
            self.numero = "".join(num.split())#En caso de que haya espacios al ingresar los numero 
        else:
            self.numero = str(num)
        if self.numero[0] == '-':#Vericamos si es un numero negativo y activamos una bandera para indicarlo
            self.negativo = True
            self.numero = self.numero[1:]
        else:
            self.negativo = False#De igual manera indicamos que no es negativo si no lo es
        self.digitos = self.digNum()
    
    def digNum(self):
        digito = 0
        if isinstance(self.numero,str):
            digito = len(self.numero)
        elif isinstance(self.numero,int):
            dig = 1
            numAux = self.numero
            while numAux // 10 != 0:
                numAux /= 10
                dig += 1
            digito = dig
        return digito
    
    def tresDig(self,numero):#Esta funcion es la base de nuestro __str__
        nombre = ""
        dig = len(numero)
        deciuni = False #bandera para los deuni
        dece = False    #bandera para evitar agregar "y"
        
        for num in numero:
            #****************************Para las centenas
            if dig == 3:
                nombre += centenas[int(num)] + " "
                dig -= 1
            #***************************Para las decenas    
            elif dig == 2:
                if int(num) == 0:
                    dig -= 1
                    continue
                if int(num) == 1:
                    deciuni = True
                else:
                    nombre += decenas[int(num)]
                    dece = True
                dig -= 1
            #**************************Para las unidades    
            elif dig == 1:
                if deciuni:
                    nombre += deuni[int(num)]
                    dig -= 1
                    continue
                if int(num) == 0:
                    continue
                if dece:
                    nombre += " y " + unidades[int(num)] + " "

                else:
                    nombre += unidades[int(num)] + " "

                dig -= 1
            #**************************Fin
        return nombre
    
    def masDig(self):
        nombre = ""
        dig = self.digitos
        if dig <= 3:
            return self.tresDig(self.numero)
        else:
            numeroList = list(self.numero)
            gruposNum = [numeroList[i -3:i] for i in range(-3,-len(numeroList),-3)]
            gruposNum.insert(0,numeroList[-3:])
            gruposNum.reverse()
            numGrupos = len(gruposNum)
            
            for numero in gruposNum:

                if numGrupos == 3:
                    nombre += self.tresDig("".join(numero)) + " millones "
                    numGrupos -= 1
                elif numGrupos == 2:
                    nombre += self.tresDig("".join(numero)) + " mil "
                    numGrupos -= 1
                elif numGrupos == 1:
                    nombre += self.tresDig("".join(numero))
                    numGrupos -= 1
        return nombre

    #**************************
        
    def __add__(self,otro):
        total = int(self.numero) + int(otro.numero)
        return Numero(total)

    def __sub__(self,otro):
        total = int(self.numero) - int(otro.numero)
        return Numero(total)

    def __mult(self,otro):
        total = int(self.numero) * int(otro.numero)
        return total

    #***************************Por ahora solo las operaciones basicas
            
    def __str__(self):
        if self.negativo:
            return "menos " + self.masDig()
        else:
            return self.masDig()


#***********************************FIN de ADT Numero ***************************************************+
#Pruebas--Esta clase puede sumar y obtener el resultado de maximo -999 999 999 hasta 999 999 999 por ahora
'''
def main():
    for i in range(40):
        num = random.randint(-1000,10000)
        print(Numero(num),":",num)

#Quita las comillas para probar directamente aqui 
if __name__ == "__main__":
    main()
'''
