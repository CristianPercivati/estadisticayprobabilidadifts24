import matplotlib.pyplot as plt

def esPar(num):
    if num%2==0:
        return True
    else:
        return False
    
def promedio(poblacion):
    totalNum = len(poblacion)
    sumatoria = 0
    for i in poblacion:
        sumatoria = sumatoria+i
    return sumatoria / totalNum

def mediana(poblacion):
    poblacion.sort()
    totalNum = len(poblacion)
    percentil = []
    for num in poblacion:
        percentil.append(percentiles(poblacion,num))

    if esPar(totalNum):
        mediana = promedio([poblacion[int(totalNum/2)], poblacion[int((totalNum/2)+1)]])
        return mediana
    else:
        mediana = poblacion[int((totalNum+1)/2)]
        return mediana
    

def cuartiles(poblacion):
    poblacion.sort()
    n = len(poblacion)
    cuartil = []
    cuartil.append(poblacion[0])
    cuartil.append((n+1)*0.25)
    cuartil.append(mediana(poblacion))
    cuartil.append((n+1)*0.75)
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

mediana([55,10,24,25,26,30,255])

