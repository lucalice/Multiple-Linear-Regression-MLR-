import numpy as np
import math

def ren(matriz,renglon):
    #Debemos regresar el renglón solicitado por la función
    renglon = matriz[renglon,:]
    return renglon

def col(matriz,columna):
    columna = matriz[:,columna]
    return columna


def celda(matriz,renglon,columna):
    return matriz[renglon,columna]


def cambioRen(matriz,reng,reng2):
    aux = matriz[reng,:]
    aux2 = matriz[reng2,:]
    aux3 = []
    aux4 = []
    for i in aux:
        aux3.append(i)

    for i in aux2:
        aux4.append(i)

    matriz[reng2,:] = aux3
    matriz[reng,:] = aux4
        
    print(matriz)


def cambioCol(matriz,colu,colu2):
    aux = matriz[:,colu]
    aux2 = matriz[:,colu2]
    aux3 = []
    aux4 = []
    for i in aux:
        aux3.append(i)

    for i in aux2:
        aux4.append(i)
    
    matriz[:,colu2] = aux3
    matriz[:,colu] = aux4
    print(matriz)

def convertirCeros(matriz,renglonP,columnaP,renglonC):
    #columnaP columna pivote renglonP renglon pivote
    #renglonC renglon a cambiar
    #num = -celda(matriz,renglonC,columnaP)/celda(matriz,renglonP,columnaP)
    if(celda(matriz,renglonP,columnaP) != 0):
        num = -celda(matriz,renglonC,columnaP)/celda(matriz,renglonP,columnaP)
        renglon1 = ren(matriz,renglonC)
        renglon2 = ren(matriz,renglonP)
        if (num != 0):
            print(num)
            for i in range(len(renglon2)):
                renglon2[i] = renglon2[i]*num
                
            matriz[renglonC,:] = renglon1+renglon2
            print("\n")
            print(matriz)
            for i in range(len(matriz[0,:])-1):
                for j in range(len(matriz[:,0])-1):
                    matriz[i,j] = matriz[i,j]

            return matriz
        else:
            return matriz
    else:
        return matriz


def convertirUnos(matriz,renglones,columnas):
    aux = 0
    for i in range(renglones-1):
        for j in range(columnas):
            if i == j:
                aux = matriz[i,j]
                matriz[i,j] /= matriz[i,j]
                matriz[i,len(matriz[0,:])-1] /= aux
    
    print("\n")
    print(matriz)
    return matriz

'''
aux = 1

valores = [2.,-1.,4.,1.,-1.,7.,-1.,3.,-2.,-1.,2.,1.,5.,1.,3.,-4.,1.,33.,3.,-2.,-2.,-2.,3.,24.,-4.,-1.,-5.,3.,-4.,-49.]

matriz = np.array(valores).reshape(5,6)#np.random.random((5,5))
#matriz = np.array(matriz_aux)
#print(matriz)
'''
'''
for i in range(5):
    for j in range(5):
        matriz[i,j] = aux
        aux += 1        

print(matriz)

for i in range(5):
    for j in range(5):
        if i != j:
            convertirCeros(matriz, i,i,j) 

convertirUnos(matriz,len(matriz[0,:]),len(matriz[:,0]))
#print(matriz)
'''
'''
print("\n")

convertirCeros(matriz,0,0,1)
convertirCeros(matriz,0,0,2)
convertirCeros(matriz,1,1,0)
convertirCeros(matriz,1,1,2)

'''

'''
for i in range(3):
    for j in range(3):
        if i != j:
            convertirCeros(matriz,i,i,j)
'''
