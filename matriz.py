import numpy as np
import csv, operator
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from minimosCuadrados import cCuadrada,dCuadrada,eCuadrada,fCuadrada,gCuadrada,hCuadrada,iCuadrada,jCuadrada,kCuadrada,terminoIndependiente,dosAB,dosAC,dosAD,dosAE,dosAF,dosAG,dosAH,dosAI,dosAJ,dosAK,dosBC,dosBD,dosBE,dosBF,dosBG,dosCD,dosCE,dosCF,dosCG,dosDE,dosDF,dosDG,dosEF,dosEG,dosFG,dosAH,dosBH,dosCH,dosDH,dosEH,dosFH,dosGH,dosAI,dosBI,dosCI,dosDI,dosEI,dosFI,dosGI,dosHI,dosBJ,dosCJ,dosDJ,dosEJ,dosFJ,dosGJ,dosHJ,dosIJ,dosBK,dosCK,dosDK,dosEK,dosFK,dosGK,dosHK,dosIK,dosJK

def readFile():
    #Utilizamos un archivo csv (separado por comas) para leer la información de las tablas.
    archivo = open('prueba.csv', 'r')
    renglones = 0
    columnas = 0
    lista = []

    for i in archivo.readlines():
        renglones = renglones + 1
        lista = i.split(' ')
    
    columnas = len(lista[0].split(','))
    #print(renglones)
    #print()
    archivo.close()
    matriz = np.ones((int(renglones),int(columnas)))
    #print(matriz)
    #print('\n')
    
    with open('prueba.csv') as csvarchivo:
        entrada = csv.reader(csvarchivo)
        aux = []

        for reg in entrada:
            for i in reg: 
                aux.append(i)
    
        #print(aux)
        #print(aux[0])
        cont = 0

        for i in range(renglones):
            for j in range(columnas):
                matriz[i,j] = aux[cont]
                cont += 1
        #Creando la matriz
    
    #print('\n')
    return matriz,renglones,columnas

def mat(listaTerm,renglones,columnas):
    matriz = np.ones((int(renglones),int(columnas)))
    cont = 0
    aux = 0
        
    for j in listaTerm:
        for k in range(columnas):
            matriz[cont,k] = j[aux]
            aux += 1
        
        aux = 0
        cont += 1
    
    print("matriz")
    print(matriz)
    return matriz




def minimosCuarados(matriz,renglones,columnas):
    listaValores = []
    terminoIn = 0
    
    terminoIn = terminoIndependiente(matriz,columnas,renglones)

    if columnas == 2:
        beta1Cuad = 0
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(terminoIn)
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores
    if columnas == 3:
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores

    if columnas == 4:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        #Beta * beta
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        #Beta *  constante
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores

    if columnas == 5:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        listaValores.append(fCuadrada(renglones,columnas,matriz))
        #Beta * beta
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosBF(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosCF(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        listaValores.append(dosDF(renglones,columnas,matriz))
        listaValores.append(dosEF(renglones,columnas,matriz))
        #Beta *  constante
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(dosAF(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores

    if columnas == 6:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        listaValores.append(fCuadrada(renglones,columnas,matriz))
        listaValores.append(gCuadrada(renglones,columnas,matriz))
        #Beta * beta
        #6
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosBF(renglones,columnas,matriz))
        listaValores.append(dosBG(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosCF(renglones,columnas,matriz))
        listaValores.append(dosCG(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        listaValores.append(dosDF(renglones,columnas,matriz))
        listaValores.append(dosDG(renglones,columnas,matriz))
        listaValores.append(dosEF(renglones,columnas,matriz))
        listaValores.append(dosEG(renglones,columnas,matriz))
        listaValores.append(dosFG(renglones,columnas,matriz))
        #Beta *  constante
        #21
        listaValores.append(dosAB(renglones,columnas,matriz)) #21
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(dosAF(renglones,columnas,matriz))
        listaValores.append(dosAG(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores
    
    if columnas == 7:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        listaValores.append(fCuadrada(renglones,columnas,matriz))
        listaValores.append(gCuadrada(renglones,columnas,matriz))
        listaValores.append(hCuadrada(renglones,columnas,matriz))
        #Beta * beta
        #7
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosBF(renglones,columnas,matriz))
        listaValores.append(dosBG(renglones,columnas,matriz))
        listaValores.append(dosBH(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosCF(renglones,columnas,matriz))
        listaValores.append(dosCG(renglones,columnas,matriz))
        listaValores.append(dosCH(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        listaValores.append(dosDF(renglones,columnas,matriz))
        listaValores.append(dosDG(renglones,columnas,matriz))
        listaValores.append(dosDH(renglones,columnas,matriz))
        listaValores.append(dosEF(renglones,columnas,matriz))
        listaValores.append(dosEG(renglones,columnas,matriz))
        listaValores.append(dosEH(renglones,columnas,matriz))
        listaValores.append(dosFG(renglones,columnas,matriz))
        listaValores.append(dosFH(renglones,columnas,matriz))
        listaValores.append(dosGH(renglones,columnas,matriz))
        #Beta *  constante 28 
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(dosAF(renglones,columnas,matriz))
        listaValores.append(dosAG(renglones,columnas,matriz))
        listaValores.append(dosAH(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores
    
    if columnas == 8:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        listaValores.append(fCuadrada(renglones,columnas,matriz))
        listaValores.append(gCuadrada(renglones,columnas,matriz))
        listaValores.append(hCuadrada(renglones,columnas,matriz))
        listaValores.append(iCuadrada(renglones,columnas,matriz))
        #Beta * beta 8
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosBF(renglones,columnas,matriz))
        listaValores.append(dosBG(renglones,columnas,matriz))
        listaValores.append(dosBH(renglones,columnas,matriz))
        listaValores.append(dosBI(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosCF(renglones,columnas,matriz))
        listaValores.append(dosCG(renglones,columnas,matriz))
        listaValores.append(dosCH(renglones,columnas,matriz))
        listaValores.append(dosCI(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        listaValores.append(dosDF(renglones,columnas,matriz))
        listaValores.append(dosDG(renglones,columnas,matriz))
        listaValores.append(dosDH(renglones,columnas,matriz))
        listaValores.append(dosDI(renglones,columnas,matriz))
        listaValores.append(dosEF(renglones,columnas,matriz))
        listaValores.append(dosEG(renglones,columnas,matriz))
        listaValores.append(dosEH(renglones,columnas,matriz))
        listaValores.append(dosEI(renglones,columnas,matriz))
        listaValores.append(dosFG(renglones,columnas,matriz))
        listaValores.append(dosFH(renglones,columnas,matriz))
        listaValores.append(dosFI(renglones,columnas,matriz))
        listaValores.append(dosGH(renglones,columnas,matriz))
        listaValores.append(dosGI(renglones,columnas,matriz))
        listaValores.append(dosHI(renglones,columnas,matriz))
        #Beta *  constante 36
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(dosAF(renglones,columnas,matriz))
        listaValores.append(dosAG(renglones,columnas,matriz))
        listaValores.append(dosAH(renglones,columnas,matriz))
        listaValores.append(dosAI(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada 44
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores


    if columnas == 9:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        listaValores.append(fCuadrada(renglones,columnas,matriz))
        listaValores.append(gCuadrada(renglones,columnas,matriz))
        listaValores.append(hCuadrada(renglones,columnas,matriz))
        listaValores.append(iCuadrada(renglones,columnas,matriz))
        listaValores.append(jCuadrada(renglones,columnas,matriz))
        #Beta * beta 9
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosBF(renglones,columnas,matriz))
        listaValores.append(dosBG(renglones,columnas,matriz))
        listaValores.append(dosBH(renglones,columnas,matriz))
        listaValores.append(dosBI(renglones,columnas,matriz))
        listaValores.append(dosBJ(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosCF(renglones,columnas,matriz))
        listaValores.append(dosCG(renglones,columnas,matriz))
        listaValores.append(dosCH(renglones,columnas,matriz))
        listaValores.append(dosCI(renglones,columnas,matriz))
        listaValores.append(dosCJ(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        listaValores.append(dosDF(renglones,columnas,matriz))
        listaValores.append(dosDG(renglones,columnas,matriz))
        listaValores.append(dosDH(renglones,columnas,matriz))
        listaValores.append(dosDI(renglones,columnas,matriz))
        listaValores.append(dosDJ(renglones,columnas,matriz))
        listaValores.append(dosEF(renglones,columnas,matriz))
        listaValores.append(dosEG(renglones,columnas,matriz))
        listaValores.append(dosEH(renglones,columnas,matriz))
        listaValores.append(dosEI(renglones,columnas,matriz))
        listaValores.append(dosEJ(renglones,columnas,matriz))
        listaValores.append(dosFG(renglones,columnas,matriz))
        listaValores.append(dosFH(renglones,columnas,matriz))
        listaValores.append(dosFI(renglones,columnas,matriz))
        listaValores.append(dosFJ(renglones,columnas,matriz))
        listaValores.append(dosGH(renglones,columnas,matriz))
        listaValores.append(dosGI(renglones,columnas,matriz))
        listaValores.append(dosGJ(renglones,columnas,matriz))
        listaValores.append(dosHI(renglones,columnas,matriz))
        listaValores.append(dosHJ(renglones,columnas,matriz))
        listaValores.append(dosIJ(renglones,columnas,matriz))
        #Beta *  constante 45
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(dosAF(renglones,columnas,matriz))
        listaValores.append(dosAG(renglones,columnas,matriz))
        listaValores.append(dosAH(renglones,columnas,matriz))
        listaValores.append(dosAI(renglones,columnas,matriz))
        listaValores.append(dosAJ(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada 54
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores


    if columnas == 10:
        #Cuadrados
        listaValores.append(renglones) #Primer valor del polinomio Beta0 al cuadrado
        listaValores.append(cCuadrada(renglones,columnas,matriz))
        listaValores.append(dCuadrada(renglones,columnas,matriz))
        listaValores.append(eCuadrada(renglones,columnas,matriz))
        listaValores.append(fCuadrada(renglones,columnas,matriz))
        listaValores.append(gCuadrada(renglones,columnas,matriz))
        listaValores.append(hCuadrada(renglones,columnas,matriz))
        listaValores.append(iCuadrada(renglones,columnas,matriz))
        listaValores.append(jCuadrada(renglones,columnas,matriz))
        listaValores.append(kCuadrada(renglones,columnas,matriz))
        #Beta * beta 10
        listaValores.append(dosBC(renglones,columnas,matriz))
        listaValores.append(dosBD(renglones,columnas,matriz))
        listaValores.append(dosBE(renglones,columnas,matriz))
        listaValores.append(dosBF(renglones,columnas,matriz))
        listaValores.append(dosBG(renglones,columnas,matriz))
        listaValores.append(dosBH(renglones,columnas,matriz))
        listaValores.append(dosBI(renglones,columnas,matriz))
        listaValores.append(dosBJ(renglones,columnas,matriz))
        listaValores.append(dosBK(renglones,columnas,matriz))
        listaValores.append(dosCD(renglones,columnas,matriz))
        listaValores.append(dosCE(renglones,columnas,matriz))
        listaValores.append(dosCF(renglones,columnas,matriz))
        listaValores.append(dosCG(renglones,columnas,matriz))
        listaValores.append(dosCH(renglones,columnas,matriz))
        listaValores.append(dosCI(renglones,columnas,matriz))
        listaValores.append(dosCJ(renglones,columnas,matriz))
        listaValores.append(dosCK(renglones,columnas,matriz))
        listaValores.append(dosDE(renglones,columnas,matriz))
        listaValores.append(dosDF(renglones,columnas,matriz))
        listaValores.append(dosDG(renglones,columnas,matriz))
        listaValores.append(dosDH(renglones,columnas,matriz))
        listaValores.append(dosDI(renglones,columnas,matriz))
        listaValores.append(dosDJ(renglones,columnas,matriz))
        listaValores.append(dosDK(renglones,columnas,matriz))
        listaValores.append(dosEF(renglones,columnas,matriz))
        listaValores.append(dosEG(renglones,columnas,matriz))
        listaValores.append(dosEH(renglones,columnas,matriz))
        listaValores.append(dosEI(renglones,columnas,matriz))
        listaValores.append(dosEJ(renglones,columnas,matriz))
        listaValores.append(dosEK(renglones,columnas,matriz))
        listaValores.append(dosFG(renglones,columnas,matriz))
        listaValores.append(dosFH(renglones,columnas,matriz))
        listaValores.append(dosFI(renglones,columnas,matriz))
        listaValores.append(dosFJ(renglones,columnas,matriz))
        listaValores.append(dosFK(renglones,columnas,matriz))
        listaValores.append(dosGH(renglones,columnas,matriz))
        listaValores.append(dosGI(renglones,columnas,matriz))
        listaValores.append(dosGJ(renglones,columnas,matriz))
        listaValores.append(dosGK(renglones,columnas,matriz))
        listaValores.append(dosHI(renglones,columnas,matriz))
        listaValores.append(dosHJ(renglones,columnas,matriz))
        listaValores.append(dosHK(renglones,columnas,matriz))
        listaValores.append(dosIJ(renglones,columnas,matriz))
        listaValores.append(dosIK(renglones,columnas,matriz))
        listaValores.append(dosJK(renglones,columnas,matriz))
        #Beta *  constante 56
        listaValores.append(dosAB(renglones,columnas,matriz))
        listaValores.append(dosAC(renglones,columnas,matriz))
        listaValores.append(dosAD(renglones,columnas,matriz))
        listaValores.append(dosAE(renglones,columnas,matriz))
        listaValores.append(dosAF(renglones,columnas,matriz))
        listaValores.append(dosAG(renglones,columnas,matriz))
        listaValores.append(dosAH(renglones,columnas,matriz))
        listaValores.append(dosAI(renglones,columnas,matriz))
        listaValores.append(dosAJ(renglones,columnas,matriz))
        listaValores.append(dosAK(renglones,columnas,matriz))
        listaValores.append(terminoIn) #a cuadrada 67
        print("\n")
        print("Polinomio: \n")
        print(listaValores)
        return listaValores

