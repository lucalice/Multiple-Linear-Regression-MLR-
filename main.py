import numpy as np
import csv, operator
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from matriz import minimosCuarados, readFile, mat
from gauss import convertirCeros, convertirUnos
from sistemasEcuaciones import ecuacionesParciales,solve

matriz, renglones, columnas = readFile()
readFile()
polinomio = minimosCuarados(matriz,renglones,columnas)
sel = ecuacionesParciales(polinomio,columnas,renglones)
ren = len(sel[0,:])
col = len(sel[:,0])
#Como tenemos las ecuaciones de la forma Ax + Bx + C = 0
#Multiplicamos por un menos 1 la ultima columna para resolver el sistema

sel[:,col] *= -1
print("\nSistema de ecuaciones lineales 3x3\n")
print("\n")
print(sel)
print("\n")
solucion = solve(sel,ren,col)
renglones = len(solucion[:,0])
columnas = len(solucion[0,:])
print("\nbetas: \n")
print(solucion[:,columnas-1])
betas = solucion[:,columnas-1]

if len(betas) == 2:
    print("y = ",betas[0]," + (",betas[1],")x")
if len(betas) == 3:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1")
if len(betas) == 4:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1 + (",betas[3],")x2")
if len(betas) == 5:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],"(x1 + (",betas[3],")x2 + (",betas[4],")x3")
if len(betas) == 6:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1 + (",betas[3],")x2 + (",betas[4],")x3 + (",betas[5],")x4")
if len(betas) == 7:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1 + (",betas[3],")x2 + (",betas[4],")x3 + (",betas[5],")x4 + (",betas[6],")x5")
if len(betas) == 8:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1 + (",betas[3],")x2 + (",betas[4],")x3 + (",betas[5],")x4 + (",betas[6],")x5 + (",betas[7],")x6")
if len(betas) == 9:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1 + (",betas[3],")x2 + (",betas[4],")x3 + (",betas[5],")x4 + (",betas[6],")x5 + (",betas[7],")x6 + (",betas[8],")x7")
if len(betas) == 10:
    print("y = ",betas[0]," + (",betas[1],")x + (",betas[2],")x1 + (",betas[3],")x2 + (",betas[4],")x3 + (",betas[5],")x4 + (",betas[6],")x5 + (",betas[7],")x6 + (",betas[8],")x7 + (",betas[9],")x8")