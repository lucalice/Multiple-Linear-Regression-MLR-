#Archivo funciones
def cCuadrada(renglones,columnas,matriz):
    beta1Cuad = 0
    for k in range(renglones):
        beta1Cuad += matriz[k][0]**2

    return beta1Cuad

def dCuadrada(renglones,columnas,matriz):
    beta2Cuad = 0
    for k in range(renglones):
        beta2Cuad += matriz[k][1]**2

    return beta2Cuad

def eCuadrada(renglones,columnas,matriz):
    beta3Cuad = 0
    for k in range(renglones):
        beta3Cuad += matriz[k][2]**2

    return beta3Cuad

def fCuadrada(renglones,columnas,matriz):
    beta4Cuad = 0
    for k in range(renglones):
        beta4Cuad += matriz[k][3]**2

    return beta4Cuad

def gCuadrada(renglones,columnas,matriz):
    beta5Cuad = 0
    for k in range(renglones):
        beta5Cuad += matriz[k][4]**2

    return beta5Cuad

def hCuadrada(renglones,columnas,matriz):
    beta6Cuad = 0
    for k in range(renglones):
        beta6Cuad += matriz[k][5]**2

    return beta6Cuad

def iCuadrada(renglones,columnas,matriz):
    beta7Cuad = 0
    for k in range(renglones):
        beta7Cuad += matriz[k][6]**2

    return beta7Cuad

def jCuadrada(renglones,columnas,matriz):
    beta8Cuad = 0
    for k in range(renglones):
        beta8Cuad += matriz[k][7]**2

    return beta8Cuad

def kCuadrada(renglones,columnas,matriz):
    beta9Cuad = 0
    for k in range(renglones):
        beta9Cuad += matriz[k][8]**2

    return beta9Cuad

def lCuadrada(renglones,columnas,matriz):
    beta10Cuad = 0
    for k in range(renglones):
        beta10Cuad += matriz[k][9]**2

    return beta10Cuad

def terminoIndependiente(matriz,columnas,renglones):
    terminoInde = 0
    for i in range (renglones):
        terminoInde += matriz[i][columnas-1]**2
    
    return terminoInde


def dosAB(renglones,columnas,matriz):
    beta0 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino y de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta0 += 2*matriz[k][columnas-1]*-1
    
    return beta0

def dosAC(renglones,columnas,matriz):
    beta1 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta1 += 2*matriz[k][columnas-1]*-(matriz[k][0])
    
    return beta1

def dosAD(renglones,columnas,matriz):
    beta2 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta2 += 2*matriz[k][columnas-1]*-(matriz[k][1])
    
    return beta2

def dosAE(renglones,columnas,matriz):
    beta3 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta3 += 2*matriz[k][columnas-1]*-(matriz[k][2])
    
    return beta3

def dosAF(renglones,columnas,matriz):
    beta4 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta4 += 2*matriz[k][columnas-1]*-(matriz[k][3])
    
    return beta4

def dosAG(renglones,columnas,matriz):
    beta5 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta5 += 2*matriz[k][columnas-1]*-(matriz[k][4])
    
    return beta5

def dosAH(renglones,columnas,matriz):
    beta6 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta6 += 2*matriz[k][columnas-1]*-(matriz[k][5])
    
    return beta6

def dosAI(renglones,columnas,matriz):
    beta7 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta7 += 2*matriz[k][columnas-1]*-(matriz[k][6])
    
    return beta7

def dosAJ(renglones,columnas,matriz):
    beta8 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta8 += 2*matriz[k][columnas-1]*-(matriz[k][7])
    
    return beta8

def dosAK(renglones,columnas,matriz):
    beta9 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta9 += 2*matriz[k][columnas-1]*-(matriz[k][8])
    
    return beta9

def dosAL(renglones,columnas,matriz):
    beta10 = 0
    for k in range (renglones):
        #2*a*b dónde a es el termino "y" de la matriz y b siempre será menos 1 por el modelo que tenemos
        beta10 += 2*matriz[k][columnas-1]*-(matriz[k][9])
    
    return beta10


#La primer columna de la matriz siempre será la variable que acompañe a beta 1
def dosBC(renglones,columnas,matriz):
    beta0Beta1 = 0
    for k in range(renglones):
        beta0Beta1 = beta0Beta1 + (matriz[k][0]*2) #Tercer valor del polinomio Beta0Beta1 
    
    return beta0Beta1

def dosBD(renglones,columnas,matriz):
    beta0Beta2 = 0
    for k in range(renglones):
        beta0Beta2 += -2*-matriz[k][1]
    
    return beta0Beta2

def dosBE(renglones,columnas,matriz):
    beta0Beta3 = 0
    for k in range(renglones):
        beta0Beta3 += -2*-matriz[k][2]
    
    return beta0Beta3

def dosBF(renglones,columnas,matriz):
    beta0Beta4 = 0
    for k in range(renglones):
        beta0Beta4 += -2*-matriz[k][3]
    
    return beta0Beta4

def dosBG(renglones,columnas,matriz):
    beta0Beta5 = 0
    for k in range(renglones):
        beta0Beta5 += -2*-matriz[k][4]
    
    return beta0Beta5

def dosBH(renglones,columnas,matriz):
    beta0Beta6 = 0
    for k in range(renglones):
        beta0Beta6 += -2*-matriz[k][5]
    
    return beta0Beta6

def dosBI(renglones,columnas,matriz):
    beta0Beta7 = 0
    for k in range(renglones):
        beta0Beta7 += -2*-matriz[k][6]
    
    return beta0Beta7

def dosBJ(renglones,columnas,matriz):
    beta0Beta8 = 0
    for k in range(renglones):
        beta0Beta8 += -2*-matriz[k][7]
    
    return beta0Beta8

def dosBK(renglones,columnas,matriz):
    beta0Beta9 = 0
    for k in range(renglones):
        beta0Beta9 += -2*-matriz[k][8]
    
    return beta0Beta9

def dosBL(renglones,columnas,matriz):
    beta0Beta10 = 0
    for k in range(renglones):
        beta0Beta10 += -2*-matriz[k][9]
    
    return beta0Beta10

def dosCD(renglones,columnas,matriz):
    beta1Beta2 = 0
    for k in range(renglones):
        beta1Beta2 += 2*-matriz[k][0]*-matriz[k][1]
    
    return beta1Beta2

def dosCE(renglones,columnas,matriz):
    beta1Beta3 = 0
    for k in range(renglones):
        beta1Beta3 += 2*-matriz[k][0]*-matriz[k][2]
    
    return beta1Beta3

def dosCF(renglones,columnas,matriz):
    beta1Beta4 = 0
    for k in range(renglones):
        beta1Beta4 += 2*-matriz[k][0]*-matriz[k][3]
    
    return beta1Beta4

def dosCG(renglones,columnas,matriz):
    beta1Beta5 = 0
    for k in range(renglones):
        beta1Beta5 += 2*-matriz[k][0]*-matriz[k][4]
    
    return beta1Beta5

def dosCH(renglones,columnas,matriz):
    beta1Beta6 = 0
    for k in range(renglones):
        beta1Beta6 += 2*-matriz[k][0]*-matriz[k][5]
    
    return beta1Beta6

def dosCI(renglones,columnas,matriz):
    beta1Beta7 = 0
    for k in range(renglones):
        beta1Beta7 += 2*-matriz[k][0]*-matriz[k][6]
    
    return beta1Beta7

def dosCJ(renglones,columnas,matriz):
    beta1Beta8 = 0
    for k in range(renglones):
        beta1Beta8 += 2*-matriz[k][0]*-matriz[k][7]
    
    return beta1Beta8

def dosCK(renglones,columnas,matriz):
    beta1Beta9 = 0
    for k in range(renglones):
        beta1Beta9 += 2*-matriz[k][0]*-matriz[k][8]
    
    return beta1Beta9

def dosDE(renglones,columnas,matriz):
    beta2Beta3 = 0
    for k in range(renglones):
        beta2Beta3 += 2*-matriz[k][1]*-matriz[k][2]
    
    return beta2Beta3

def dosDF(renglones,columnas,matriz):
    beta2Beta4 = 0
    for k in range(renglones):
        beta2Beta4 += 2*-matriz[k][1]*-matriz[k][3]
    
    return beta2Beta4

def dosDG(renglones,columnas,matriz):
    beta2Beta5 = 0
    for k in range(renglones):
        beta2Beta5 += 2*-matriz[k][1]*-matriz[k][4]
    
    return beta2Beta5

def dosDH(renglones,columnas,matriz):
    beta2Beta6 = 0
    for k in range(renglones):
        beta2Beta6 += 2*-matriz[k][1]*-matriz[k][5]
    
    return beta2Beta6

def dosDI(renglones,columnas,matriz):
    beta2Beta7 = 0
    for k in range(renglones):
        beta2Beta7 += 2*-matriz[k][1]*-matriz[k][6]
    
    return beta2Beta7

def dosDJ(renglones,columnas,matriz):
    beta2Beta8 = 0
    for k in range(renglones):
        beta2Beta8 += 2*-matriz[k][1]*-matriz[k][7]
    
    return beta2Beta8

def dosDK(renglones,columnas,matriz):
    beta2Beta9 = 0
    for k in range(renglones):
        beta2Beta9 += 2*-matriz[k][1]*-matriz[k][8]
    
    return beta2Beta9

def dosDL(renglones,columnas,matriz):
    beta2Beta10 = 0
    for k in range(renglones):
        beta2Beta10 += 2*-matriz[k][1]*-matriz[k][9]
    
    return beta2Beta10


def dosEF(renglones,columnas,matriz):
    beta3Beta4 = 0
    for k in range(renglones):
        beta3Beta4 += 2*-matriz[k][2]*-matriz[k][3]
    
    return beta3Beta4

def dosEG(renglones,columnas,matriz):
    beta3Beta5 = 0
    for k in range(renglones):
        beta3Beta5 += 2*-matriz[k][2]*-matriz[k][4]
    
    return beta3Beta5

def dosEH(renglones,columnas,matriz):
    beta3Beta6 = 0
    for k in range(renglones):
        beta3Beta6 += 2*-matriz[k][2]*-matriz[k][5]
    
    return beta3Beta6

def dosEI(renglones,columnas,matriz):
    beta3Beta7 = 0
    for k in range(renglones):
        beta3Beta7 += 2*-matriz[k][2]*-matriz[k][6]
    
    return beta3Beta7

def dosEJ(renglones,columnas,matriz):
    beta3Beta8 = 0
    for k in range(renglones):
        beta3Beta8 += 2*-matriz[k][2]*-matriz[k][7]
    
    return beta3Beta8

def dosEK(renglones,columnas,matriz):
    beta3Beta9 = 0
    for k in range(renglones):
        beta3Beta9 += 2*-matriz[k][2]*-matriz[k][8]
    
    return beta3Beta9

def dosEL(renglones,columnas,matriz):
    beta3Beta10 = 0
    for k in range(renglones):
        beta3Beta10 += 2*-matriz[k][2]*-matriz[k][9]
    
    return beta3Beta10

def dosFG(renglones,columnas,matriz):
    beta4Beta5 = 0
    for k in range(renglones):
        beta4Beta5 += 2*-matriz[k][3]*-matriz[k][4]
    
    return beta4Beta5

def dosFH(renglones,columnas,matriz):
    beta4Beta6 = 0
    for k in range(renglones):
        beta4Beta6 += 2*-matriz[k][3]*-matriz[k][5]
    
    return beta4Beta6

def dosFI(renglones,columnas,matriz):
    beta4Beta7 = 0
    for k in range(renglones):
        beta4Beta7 += 2*-matriz[k][3]*-matriz[k][6]
    
    return beta4Beta7

def dosFJ(renglones,columnas,matriz):
    beta4Beta8 = 0
    for k in range(renglones):
        beta4Beta8 += 2*-matriz[k][3]*-matriz[k][7]
    
    return beta4Beta8

def dosFK(renglones,columnas,matriz):
    beta4Beta9 = 0
    for k in range(renglones):
        beta4Beta9 += 2*-matriz[k][3]*-matriz[k][8]
    
    return beta4Beta9

def dosFL(renglones,columnas,matriz):
    beta4Beta10 = 0
    for k in range(renglones):
        beta4Beta10 += 2*-matriz[k][3]*-matriz[k][9]
    
    return beta4Beta10

def dosGH(renglones,columnas,matriz):
    beta5Beta6 = 0
    for k in range(renglones):
        beta5Beta6 += 2*-matriz[k][4]*-matriz[k][5]
    
    return beta5Beta6

def dosGI(renglones,columnas,matriz):
    beta5Beta7 = 0
    for k in range(renglones):
        beta5Beta7 += 2*-matriz[k][4]*-matriz[k][6]
    
    return beta5Beta7

def dosGJ(renglones,columnas,matriz):
    beta5Beta8 = 0
    for k in range(renglones):
        beta5Beta8 += 2*-matriz[k][4]*-matriz[k][7]
    
    return beta5Beta8

def dosGK(renglones,columnas,matriz):
    beta5Beta9 = 0
    for k in range(renglones):
        beta5Beta9 += 2*-matriz[k][4]*-matriz[k][8]
    
    return beta5Beta9

def dosGL(renglones,columnas,matriz):
    beta5Beta10 = 0
    for k in range(renglones):
        beta5Beta10 += 2*-matriz[k][4]*-matriz[k][9]
    
    return beta5Beta10

def dosHI(renglones,columnas,matriz):
    beta6Beta7 = 0
    for k in range(renglones):
        beta6Beta7 += 2*-matriz[k][5]*-matriz[k][6]
    
    return beta6Beta7

#duda
def dosIJ(renglones,columnas,matriz):
    beta7Beta8 = 0
    for k in range(renglones):
        beta7Beta8 += 2*-matriz[k][6]*-matriz[k][7]
    
    return beta7Beta8

def dosHJ(renglones,columnas,matriz):
    beta6Beta8 = 0
    for k in range(renglones):
        beta6Beta8 += 2*-matriz[k][5]*-matriz[k][7]
    
    return beta6Beta8

def dosHK(renglones,columnas,matriz):
    beta6Beta9 = 0
    for k in range(renglones):
        beta6Beta9 += 2*-matriz[k][5]*-matriz[k][8]
    
    return beta6Beta9

def dosHL(renglones,columnas,matriz):
    beta6Beta10 = 0
    for k in range(renglones):
        beta6Beta10 += 2*-matriz[k][5]*-matriz[k][9]
    
    return beta6Beta10

def dosIK(renglones,columnas,matriz):
    beta7Beta9 = 0
    for k in range(renglones):
        beta7Beta9 += 2*-matriz[k][6]*-matriz[k][8]
    
    return beta7Beta9


def dosJK(renglones,columnas,matriz):
    beta8Beta9 = 0
    for k in range(renglones):
        beta8Beta9 += 2*-matriz[k][7]*-matriz[k][8]
    
    return beta8Beta9


