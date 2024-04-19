#Verificar la instalación de ucimlrepo
#Deberia de funcionar lo siguiente por defecto
#en la terminal -> pip install ucimlrepo
#o en caso de fallo 
#./ruta_instalacion_Python pip install ucimlrepo
try:
    from ucimlrepo import fetch_ucirepo 
    import pandas as pd
    import numpy as np  
    import random 
    from scipy.stats import mode
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ucimlrepo', 'pandas', 'numpy', 'scipy'])
    # Una vez instaladas las bibliotecas, intenta importarlas nuevamente
    from ucimlrepo import fetch_ucirepo 
    import pandas as pd
    import numpy as np  
    from scipy.stats import mode

# Configuraciones para no truncar la salida ***************
pd.set_option('display.max_rows', None)

#Configuraciones para no truncar la salida  ***************
pd.set_option('display.max_rows', None)

#sintaxis ->    DataFrame.iloc[fila,columna] 

# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
data_num = iris.data.features #Caracteristicas 
data_label = iris.data.targets  #Objetivos

#Porcentaje 50 
percent_query = 15

#Datos 

#Query
nume_samples_query = int((len(data_num) * percent_query)/100)                       #Numero de muestras con respecto al porcentanje         
query_index_samples = random.sample(list(range(0,149)),nume_samples_query)          #Escogemos los indices de query aleatoriamente sin remplazo
query_index_samples.sort()                                                          #Ordenamos 
query_samples = data_num.iloc[query_index_samples]                                  #seleccionamos de data_num con respecto a los indices encontrados 
#    Training
#Agregar inplace como True para eliminar de la original 
training_samples = data_num.drop(query_index_samples)                               #Escogemos los indices faltantes

#Label 
query_samples_label = data_label.iloc[query_index_samples]                          #iloc -> [] usando los indices antes encontrados para query
training_samples_label = data_label.drop(query_index_samples)                       #Escogemos los indices faltantes 


cols_dn = len(data_num.columns)                                                     #Columnas de data_num
size_ts = len(training_samples)                                                     #Size de training_samples
size_q  = len(query_samples)                                                        #Size de query
k_DI = []                                                                           #Aqui se almacenan las k distancias mas pequeñas
k = 5                                                                               #
for j in range(size_q):                                                             #iteramos por todos los elementos de la query
    Q = np.tile(query_samples.iloc[j,:],(training_samples.shape[0],1))              #Igual que 'repmat'
    Z = Q - training_samples                                                        #
    S_with_garbage = Z @ Z.T                                                        #puede usar tambien np.dot(m1,m2)
    distancia_S = np.diag(S_with_garbage) ** (1 / 2)                                #Obtener la diagonal y elevar sus elem a 1/2
    
    sort_index = np.argsort(distancia_S)                                            #Obtener los indices ordenados
    
    k_index = sort_index[:k]                                                        #Seleccionamos los k primeros
    k_dis = distancia_S[k_index]                                                    #Almacenamos las k distancias minimas

    mode_k_dis = mode(k_dis)[0]                                                     #mode retorna (moda, repeticiones)
    index_mode = np.where(distancia_S == mode_k_dis)[0][0]                          #buscamos indice en distancia_S de mode_k_dis
    """
    index_mode1 = 0                                                                 #La primera forma que se me ocurrio de hacerlo
    for i in k_index:                                                               #luego encontre la solución de arriba
        if distancia_S[i] == mode_k_dis:
            index_mode = i
            break
    print(distancia_S[index_mode],distancia_S[index_mode1])
    """
    k_DI.append(index_mode) 


for i in range(len(query_samples_label)):
    print(f"Label {i} en query:{query_samples_label.iloc[i]}")
    print(f"Valor dado por kNN:{training_samples_label.iloc[k_DI[i]]}\n")
