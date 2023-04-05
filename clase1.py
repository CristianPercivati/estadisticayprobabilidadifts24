import matplotlib.pyplot as plt
import math

def esPar(num):
    if num%2==0:
        return True
    else:
        return False
    
def promedio(poblacion):
    n = len(poblacion)
    sumatoria = 0
    for i in poblacion:
        sumatoria = sumatoria+i
    media = sumatoria/n
    plt.plot(poblacion)
    plt.axhline(y=media, color='r', linestyle='-')
    plt.title("Promedio: "+str(media))
    plt.ylabel("Población")
    plt.show()
    return media

def mediana(poblacion):
    poblacion.sort()
    totalNum = len(poblacion)
    percentil = []
    for num in poblacion:
        percentil.append(percentiles(poblacion,num))

    if esPar(totalNum):
        mediana = promedio([poblacion[int(totalNum/2)], poblacion[int((totalNum/2)+1)]])
        plt.plot(poblacion)
        plt.axhline(y=mediana, color='r', linestyle='-')
        plt.title("Mediana: "+str(mediana))
        plt.ylabel("Población")
        plt.show()
        return mediana
    else:
        mediana = poblacion[int((totalNum+1)/2)-1]
        plt.plot(poblacion)
        plt.axhline(y=mediana, color='r', linestyle='-')
        plt.title("Mediana: "+str(mediana))
        plt.ylabel("Población")
        plt.show()
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
            print (percentil, pos)
            cuartil.append(promedio([poblacion[pos],poblacion[pos+1]]))
        else:
            pos = int(percentil)-1
            cuartil.append(poblacion[pos])
            
    cuartil.append(poblacion[-1])
    return cuartil

def percentiles(poblacion,valor):
    n = len(poblacion)
    try:
        posDato = poblacion.index(valor)
    except:
        return False
    percentil = ((posDato-0.5)/n)*100
    return percentil

print(cuartiles([12, 5, 8, 17, 21, 15, 9, 3, 10, 20]))

