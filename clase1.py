import matplotlib.pyplot as plt

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
    cuartil = []
    cuartil.append(poblacion[0])
    cuartil.append(poblacion(n+1)*0.25-1)
    cuartil.append(mediana(poblacion))
    cuartil.append((n+1)*0.75-1)
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

print(cuartiles([55,10,24,25,26,30,255]))

