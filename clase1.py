import matplotlib.pyplot as plt
import numpy as np
import math

def esPar(num):
    if num%2==0:
        return True
    else:
        return False
    
def graficar(poblacion,tipo,num=False):
    plt.plot(poblacion)
    plt.plot(poblacion,"o")
    print(num)
    if num:
        plt.axhline(y=num, color='r', linestyle='-')
        plt.title(f'{tipo}: {num}')
    else:
        plt.title(f'{tipo}: {poblacion}')
    plt.ylabel("Población")
    plt.show()
    
def promedio(poblacion):
    n = len(poblacion)
    sumatoria = 0
    for i in poblacion:
        sumatoria = sumatoria+i
    media = sumatoria/n
    return media

def mediana(poblacion):
    poblacion.sort()
    totalNum = len(poblacion)
    if esPar(totalNum):
        pos = math.floor(int(totalNum/2))-1
        mediana = promedio([poblacion[pos], poblacion[pos+1]])
        return mediana
    else:
        mediana = poblacion[int((totalNum+1)/2)-1]
        return mediana

def cuartiles(poblacion):
    poblacion.sort()
    n = len(poblacion)
    p = [(n+1)*0.25, (n+1)*0.5,(n+1)*0.75]
    cuartil = []
    cuartil.append(poblacion[0])
    
    for percentil in p:
        if percentil%1:
            pos = math.floor(percentil)-1
            cuartil.append(promedio( [poblacion[pos] , poblacion[pos+1]] ))
        else:
            pos = int(percentil)-1
            cuartil.append(poblacion[pos])
            
    cuartil.append(poblacion[-1])
    return cuartil

def percentiles(poblacion,valor):
    poblacion.sort()
    n = len(poblacion)
    percentil = ((valor/100)*(n+1))
    if percentil%1:
        pos = math.floor(percentil)-1
        print(pos)
        percentil = promedio([poblacion[pos], poblacion[pos+1]])
    else:
        percentil = poblacion[int(percentil)]
    devuelto = {"percentil": percentil, "num": valor}
    return devuelto

def varianza(muestra):
    n = len(muestra)
    media = promedio(muestra)
    sumatoria = 0
    numMedia = 0
    numMediaPow = 0
    
    for num in muestra:
        numMedia = num - media
        numMediaPow = pow(numMedia,2)
        sumatoria = sumatoria+numMediaPow
        print(sumatoria)
    
    varianza = sumatoria/(n-1)
    return varianza

def desviacionEstandar(muestra):
    varian = varianza(muestra)
    return math.sqrt(varian)

poblacion = [12, 5, 8, 17, 21, 15, 9, 3, 10, 20]

#Para probar, simplemente descomentar las funciones necesarias acá abajo:

#graficar(poblacion, "Promedio", promedio(poblacion))
#graficar(poblacion, "Mediana", mediana(poblacion))
#graficar(cuartiles(poblacion), "Cuartiles")

#calcPercentiles = percentiles(poblacion,21)
#graficar(poblacion, f"Percentil de {calcPercentiles['num']}", calcPercentiles["percentil"])
