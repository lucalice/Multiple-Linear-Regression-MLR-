import numpy as np
import csv, operator
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from matriz import minimosCuarados, readFile, mat
from gauss import convertirCeros, convertirUnos

def ecuacionesParciales(polinomio,columnas,renglones):
    dB0 = []
    dB1 = []
    dB2 = []
    dB3 = []
    dB4 = []
    dB5 = []
    dB6 = []
    dB7 = []
    dB8 = []
    dB9 = []
    dB10 = []
    betas = []
    print("\n")
    if columnas == 2:
        #Vamos a derivar con respecto a B0
        dB0.append(polinomio[0]*2)
        dB0.append(polinomio[columnas])
        dB0.append(polinomio[columnas+1])
        dB1.append(polinomio[columnas])
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[columnas+2])

        betas.append(dB0)
        betas.append(dB1)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        # betas

    if columnas == 3:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1
        dB0.append(polinomio[3])
        dB0.append(polinomio[4])
        dB0.append(polinomio[6])
        dB1.append(polinomio[3])  #Beta 0 renglon 2
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[5])
        dB1.append(polinomio[7])
        dB2.append(polinomio[4]) #Beta 0 renglon 3
        dB2.append(polinomio[5])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[8])
        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        
        #return dB0,dB1,dB2

    if columnas == 4:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1
        dB0.append(polinomio[4])
        dB0.append(polinomio[5])
        dB0.append(polinomio[6])
        dB0.append(polinomio[10])
        dB1.append(polinomio[4])  #Beta 0 renglon 2
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[7])
        dB1.append(polinomio[8])
        dB1.append(polinomio[11])
        dB2.append(polinomio[5]) #Beta 0 renglon 3
        dB2.append(polinomio[7])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[9])
        dB2.append(polinomio[12])
        dB3.append(polinomio[6]) #Beta 0 en renglon 4
        dB3.append(polinomio[8])
        dB3.append(polinomio[9])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[13])

        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3

    if columnas == 5:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1
        dB0.append(polinomio[5])
        dB0.append(polinomio[6])
        dB0.append(polinomio[7])
        dB0.append(polinomio[8])
        dB0.append(polinomio[15])
        dB1.append(polinomio[5])  #Beta 0 renglon 2
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[9])
        dB1.append(polinomio[10])
        dB1.append(polinomio[11])
        dB1.append(polinomio[16])
        dB2.append(polinomio[6]) #Beta 0 renglon 3 D
        dB2.append(polinomio[9])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[12])
        dB2.append(polinomio[13])
        dB2.append(polinomio[17])
        dB3.append(polinomio[7]) #Beta 0 en renglon 4
        dB3.append(polinomio[10])
        dB3.append(polinomio[12])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[14])
        dB3.append(polinomio[18])
        dB4.append(polinomio[8]) #Beta 0 renglon 5
        dB4.append(polinomio[11])
        dB4.append(polinomio[13])
        dB4.append(polinomio[14])
        dB4.append(polinomio[4]*2)
        dB4.append(polinomio[19])

        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        betas.append(dB4)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3,dB4

    if columnas == 6:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1
        dB0.append(polinomio[6])
        dB0.append(polinomio[7])
        dB0.append(polinomio[8])
        dB0.append(polinomio[9])
        dB0.append(polinomio[10])
        dB0.append(polinomio[21])
        dB1.append(polinomio[6])  #Beta 0 renglon 2
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[11])
        dB1.append(polinomio[12])
        dB1.append(polinomio[13])
        dB1.append(polinomio[14])
        dB1.append(polinomio[22])
        dB2.append(polinomio[7]) #Beta 0 renglon 3
        dB2.append(polinomio[11])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[15])
        dB2.append(polinomio[16])
        dB2.append(polinomio[17])
        dB2.append(polinomio[23])
        dB3.append(polinomio[8]) #Beta 0 en renglon 4
        dB3.append(polinomio[12])
        dB3.append(polinomio[15])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[18])
        dB3.append(polinomio[19])
        dB3.append(polinomio[24])
        dB4.append(polinomio[9]) #Beta 0 renglon 5
        dB4.append(polinomio[13])
        dB4.append(polinomio[16])
        dB4.append(polinomio[18])
        dB4.append(polinomio[4]*2)
        dB4.append(polinomio[20])
        dB4.append(polinomio[25])
        dB5.append(polinomio[10]) #Beta 0 renglon 6
        dB5.append(polinomio[14])
        dB5.append(polinomio[17])
        dB5.append(polinomio[19])
        dB5.append(polinomio[20])
        dB5.append(polinomio[5]*2)
        dB5.append(polinomio[26])

        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        betas.append(dB4)
        betas.append(dB5)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3,dB4,dB5

    if columnas == 7:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1
        dB0.append(polinomio[7])
        dB0.append(polinomio[8])
        dB0.append(polinomio[9])
        dB0.append(polinomio[10])
        dB0.append(polinomio[11])
        dB0.append(polinomio[12])
        dB0.append(polinomio[28])
        dB1.append(polinomio[7])  #Beta 0 renglon 2
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[13])
        dB1.append(polinomio[14])
        dB1.append(polinomio[15])
        dB1.append(polinomio[16])
        dB1.append(polinomio[17])
        dB1.append(polinomio[29])
        dB2.append(polinomio[8]) #Beta 0 renglon 3 D
        dB2.append(polinomio[13])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[18])
        dB2.append(polinomio[19])
        dB2.append(polinomio[20])
        dB2.append(polinomio[21])
        dB2.append(polinomio[30])
        dB3.append(polinomio[9]) #Beta 0 en renglon 4 E
        dB3.append(polinomio[14])
        dB3.append(polinomio[18])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[22])
        dB3.append(polinomio[23])
        dB3.append(polinomio[24])
        dB3.append(polinomio[31])
        dB4.append(polinomio[10]) #Beta 0 renglon 5 F
        dB4.append(polinomio[15])
        dB4.append(polinomio[19])
        dB4.append(polinomio[22])
        dB4.append(polinomio[4]*2)
        dB4.append(polinomio[25])
        dB4.append(polinomio[26])
        dB4.append(polinomio[32])
        dB5.append(polinomio[11]) #Beta 0 renglon 6 G
        dB5.append(polinomio[16])
        dB5.append(polinomio[20])
        dB5.append(polinomio[23])
        dB5.append(polinomio[25])
        dB5.append(polinomio[5]*2)
        dB5.append(polinomio[27])
        dB5.append(polinomio[33])
        dB6.append(polinomio[12]) #Beta 0 renglon 7 H
        dB6.append(polinomio[17])
        dB6.append(polinomio[21])
        dB6.append(polinomio[24])
        dB6.append(polinomio[26])
        dB6.append(polinomio[27])
        dB6.append(polinomio[6]*2)
        dB6.append(polinomio[34])

        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        betas.append(dB4)
        betas.append(dB5)
        betas.append(dB6)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3,dB4,dB5,dB6


    if columnas == 8:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1 B
        dB0.append(polinomio[8])
        dB0.append(polinomio[9])
        dB0.append(polinomio[10])
        dB0.append(polinomio[11])
        dB0.append(polinomio[12])
        dB0.append(polinomio[13])
        dB0.append(polinomio[14])
        dB0.append(polinomio[36])
        dB1.append(polinomio[8])  #Beta 0 renglon 2 C
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[15])
        dB1.append(polinomio[16])
        dB1.append(polinomio[17])
        dB1.append(polinomio[18])
        dB1.append(polinomio[19])
        dB1.append(polinomio[20])
        dB1.append(polinomio[37])
        dB2.append(polinomio[9]) #Beta 0 renglon 3 D
        dB2.append(polinomio[15])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[21])
        dB2.append(polinomio[22])
        dB2.append(polinomio[23])
        dB2.append(polinomio[24])
        dB2.append(polinomio[25])
        dB2.append(polinomio[38])
        dB3.append(polinomio[10]) #Beta 0 en renglon 4 E
        dB3.append(polinomio[16])
        dB3.append(polinomio[21])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[26])
        dB3.append(polinomio[27])
        dB3.append(polinomio[28])
        dB3.append(polinomio[29])
        dB3.append(polinomio[39])
        dB4.append(polinomio[11]) #Beta 0 renglon 5 F
        dB4.append(polinomio[17])
        dB4.append(polinomio[22])
        dB4.append(polinomio[26])
        dB4.append(polinomio[4]*2)
        dB4.append(polinomio[30])
        dB4.append(polinomio[31])
        dB4.append(polinomio[32])
        dB4.append(polinomio[40])
        dB5.append(polinomio[12]) #Beta 0 renglon 6 G
        dB5.append(polinomio[18])
        dB5.append(polinomio[23])
        dB5.append(polinomio[27])
        dB5.append(polinomio[30])
        dB5.append(polinomio[5]*2)
        dB5.append(polinomio[33])
        dB5.append(polinomio[34])
        dB5.append(polinomio[41])
        dB6.append(polinomio[13]) #Beta 0 renglon 7 H
        dB6.append(polinomio[19])
        dB6.append(polinomio[24])
        dB6.append(polinomio[28])
        dB6.append(polinomio[31])
        dB6.append(polinomio[33])
        dB6.append(polinomio[6]*2)
        dB6.append(polinomio[35])
        dB6.append(polinomio[42])
        dB7.append(polinomio[14]) #Beta 0 renglon 8 I
        dB7.append(polinomio[20]) 
        dB7.append(polinomio[25])
        dB7.append(polinomio[29])
        dB7.append(polinomio[32])
        dB7.append(polinomio[34])
        dB7.append(polinomio[35])
        dB7.append(polinomio[7]*2)
        dB7.append(polinomio[43])


        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        betas.append(dB4)
        betas.append(dB5)
        betas.append(dB6)
        betas.append(dB7)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3,dB4,dB5,dB6,dB7

    if columnas == 9:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1 B
        dB0.append(polinomio[9])
        dB0.append(polinomio[10])
        dB0.append(polinomio[11])
        dB0.append(polinomio[12])
        dB0.append(polinomio[13])
        dB0.append(polinomio[14])
        dB0.append(polinomio[15])
        dB0.append(polinomio[16])
        dB0.append(polinomio[45])
        dB1.append(polinomio[9])  #Beta 0 renglon 2 C
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[17])
        dB1.append(polinomio[18])
        dB1.append(polinomio[19])
        dB1.append(polinomio[20])
        dB1.append(polinomio[21])
        dB1.append(polinomio[22])
        dB1.append(polinomio[23])
        dB1.append(polinomio[46])
        dB2.append(polinomio[10]) #Beta 0 renglon 3 D
        dB2.append(polinomio[17])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[24])
        dB2.append(polinomio[25])
        dB2.append(polinomio[26])
        dB2.append(polinomio[27])
        dB2.append(polinomio[28])
        dB2.append(polinomio[29])
        dB2.append(polinomio[47])
        dB3.append(polinomio[11]) #Beta 0 en renglon 4 E
        dB3.append(polinomio[18])
        dB3.append(polinomio[24])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[30])
        dB3.append(polinomio[31])
        dB3.append(polinomio[32])
        dB3.append(polinomio[33])
        dB3.append(polinomio[34])
        dB3.append(polinomio[48])
        dB4.append(polinomio[12]) #Beta 0 renglon 5 F
        dB4.append(polinomio[19])
        dB4.append(polinomio[25])
        dB4.append(polinomio[30])
        dB4.append(polinomio[4]*2)
        dB4.append(polinomio[35])
        dB4.append(polinomio[36])
        dB4.append(polinomio[37])
        dB4.append(polinomio[38])
        dB4.append(polinomio[49])
        dB5.append(polinomio[13]) #Beta 0 renglon 6 G
        dB5.append(polinomio[20])
        dB5.append(polinomio[26])
        dB5.append(polinomio[31])
        dB5.append(polinomio[35])
        dB5.append(polinomio[5]*2)
        dB5.append(polinomio[39])
        dB5.append(polinomio[40])
        dB5.append(polinomio[41])
        dB5.append(polinomio[50])
        dB6.append(polinomio[14]) #Beta 0 renglon 7 H
        dB6.append(polinomio[21])
        dB6.append(polinomio[27])
        dB6.append(polinomio[32])
        dB6.append(polinomio[36])
        dB6.append(polinomio[39])
        dB6.append(polinomio[6]*2)
        dB6.append(polinomio[42])
        dB6.append(polinomio[43])
        dB6.append(polinomio[51])
        dB7.append(polinomio[15]) #Beta 0 renglon 8 I
        dB7.append(polinomio[22]) 
        dB7.append(polinomio[28])
        dB7.append(polinomio[33])
        dB7.append(polinomio[37])
        dB7.append(polinomio[40])
        dB7.append(polinomio[42])
        dB7.append(polinomio[7]*2)
        dB7.append(polinomio[44])
        dB7.append(polinomio[52])
        dB8.append(polinomio[16]) #Beta 0 renglon 9 J
        dB8.append(polinomio[23])
        dB8.append(polinomio[29])
        dB8.append(polinomio[34])
        dB8.append(polinomio[38])
        dB8.append(polinomio[41])
        dB8.append(polinomio[43])
        dB8.append(polinomio[44])
        dB8.append(polinomio[8]*2)
        dB8.append(polinomio[53])

        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        betas.append(dB4)
        betas.append(dB5)
        betas.append(dB6)
        betas.append(dB7)
        betas.append(dB8)
        print("Hola")
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3,dB4,dB5,dB6,dB7,dB8

    
    if columnas == 10:
        dB0.append(polinomio[0]*2) #Beta 0 renglon 1 B
        dB0.append(polinomio[10])
        dB0.append(polinomio[11])
        dB0.append(polinomio[12])
        dB0.append(polinomio[13])
        dB0.append(polinomio[14])
        dB0.append(polinomio[15])
        dB0.append(polinomio[16])
        dB0.append(polinomio[17])
        dB0.append(polinomio[18])
        dB0.append(polinomio[56])
        dB1.append(polinomio[10])  #Beta 0 renglon 2 C
        dB1.append(polinomio[1]*2)
        dB1.append(polinomio[19])
        dB1.append(polinomio[20])
        dB1.append(polinomio[21])
        dB1.append(polinomio[22])
        dB1.append(polinomio[23])
        dB1.append(polinomio[24])
        dB1.append(polinomio[25])
        dB1.append(polinomio[26])
        dB1.append(polinomio[57])
        dB2.append(polinomio[11]) #Beta 0 renglon 3 D
        dB2.append(polinomio[19])
        dB2.append(polinomio[2]*2)
        dB2.append(polinomio[27])
        dB2.append(polinomio[28])
        dB2.append(polinomio[29])
        dB2.append(polinomio[30])
        dB2.append(polinomio[31])
        dB2.append(polinomio[32])
        dB2.append(polinomio[33])
        dB2.append(polinomio[58])
        dB3.append(polinomio[12]) #Beta 0 en renglon 4 E
        dB3.append(polinomio[20])
        dB3.append(polinomio[27])
        dB3.append(polinomio[3]*2)
        dB3.append(polinomio[34])
        dB3.append(polinomio[35])
        dB3.append(polinomio[36])
        dB3.append(polinomio[37])
        dB3.append(polinomio[38])
        dB3.append(polinomio[39])
        dB3.append(polinomio[59])
        dB4.append(polinomio[13]) #Beta 0 renglon 5 F
        dB4.append(polinomio[21])
        dB4.append(polinomio[28])
        dB4.append(polinomio[34])
        dB4.append(polinomio[4]*2)
        dB4.append(polinomio[40])
        dB4.append(polinomio[41])
        dB4.append(polinomio[42])
        dB4.append(polinomio[43])
        dB4.append(polinomio[44])
        dB4.append(polinomio[60])
        dB5.append(polinomio[14]) #Beta 0 renglon 6 G
        dB5.append(polinomio[22])
        dB5.append(polinomio[29])
        dB5.append(polinomio[35])
        dB5.append(polinomio[40])
        dB5.append(polinomio[5]*2)
        dB5.append(polinomio[45])
        dB5.append(polinomio[46])
        dB5.append(polinomio[47])
        dB5.append(polinomio[48])
        dB5.append(polinomio[61])
        dB6.append(polinomio[15]) #Beta 0 renglon 7 H
        dB6.append(polinomio[23])
        dB6.append(polinomio[30])
        dB6.append(polinomio[36])
        dB6.append(polinomio[41])
        dB6.append(polinomio[45])
        dB6.append(polinomio[6]*2)
        dB6.append(polinomio[49])
        dB6.append(polinomio[50])
        dB6.append(polinomio[51])
        dB6.append(polinomio[62])
        dB7.append(polinomio[16]) #Beta 0 renglon 8 I
        dB7.append(polinomio[24]) 
        dB7.append(polinomio[31])
        dB7.append(polinomio[37])
        dB7.append(polinomio[42])
        dB7.append(polinomio[46])
        dB7.append(polinomio[49])
        dB7.append(polinomio[7]*2)
        dB7.append(polinomio[52])
        dB7.append(polinomio[53])
        dB7.append(polinomio[63])
        dB8.append(polinomio[17]) #Beta 0 renglon 9 J
        dB8.append(polinomio[25])
        dB8.append(polinomio[32])
        dB8.append(polinomio[38])
        dB8.append(polinomio[43])
        dB8.append(polinomio[47])
        dB8.append(polinomio[50])
        dB8.append(polinomio[52])
        dB8.append(polinomio[8]*2)
        dB8.append(polinomio[54])
        dB8.append(polinomio[64])
        dB9.append(polinomio[18]) #Beta 0 renglon K
        dB9.append(polinomio[26])
        dB9.append(polinomio[33])
        dB9.append(polinomio[39])
        dB9.append(polinomio[44])
        dB9.append(polinomio[48])
        dB9.append(polinomio[51])
        dB9.append(polinomio[53])
        dB9.append(polinomio[54])
        dB9.append(polinomio[9]*2)
        dB9.append(polinomio[65])
        
        betas.append(dB0)
        betas.append(dB1)
        betas.append(dB2)
        betas.append(dB3)
        betas.append(dB4)
        betas.append(dB5)
        betas.append(dB6)
        betas.append(dB7)
        betas.append(dB8)
        betas.append(dB9)
        print(betas)
        return mat(betas,len(betas),len(betas)+1)
        #return dB0,dB1,dB2,dB3,dB4,dB5,dB6,dB7,dB8,dB9


def solve(matriz,renglones,columnas):
    print("Comienza la resolución: \n")
    for i in range(renglones-1):
        for j in range(columnas):
            if i != j:
                matriz = convertirCeros(matriz,i,i,j)
    
    convertirUnos(matriz,renglones,columnas)
    print("\n")
    print(matriz)
    return matriz


#main
'''
matriz, renglones, columnas = readFile()
print(readFile())
polinomio = minimosCuarados(matriz,renglones,columnas)
sel = ecuacionesParciales(polinomio,columnas,renglones)
ren = len(sel[0,:])
col = len(sel[:,0]) 
'''
#Como tenemos las ecuaciones de la forma Ax + Bx + C = 0
#Multiplicamos por un menos 1 la ultima columna para resolver el sistema
'''
sel[:,col] *= -1
print("Sistema de ecuaciones lineales 3x3")

print(sel)
solucion = solve(sel,ren,col)
renglones = len(solucion[:,0])
columnas = len(solucion[0,:])
print("\nbetas: \n")
print(solucion[:,columnas-1])
betas = solucion[:,columnas-1]

if len(betas) == 2:
    print("y = ",betas[0]," + ",betas[1],"x")

'''


