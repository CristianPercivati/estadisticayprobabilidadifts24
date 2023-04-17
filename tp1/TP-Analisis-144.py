import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('datos-144-2020.csv')

def totalCasos():
    return data.count()[0]

#def distribucionProvincias():
#   return [maxima, minima, totalProvincia]

#def distribucionEdad():
#-cantidad de menores y adultos
#-agrupación por edades
#-vínculo con el agresor
#-edad menor
#-edad mayor
#-edad promedio
#-dispersión por edades
#-moda de edad
#-mediana de edad

#def vinculoAgresor():
#-edades NNyNA y adultos
#-minima
#-máxima
#-género del agresor

#def tiposViolencia():
#-Proporciones
#-mínimo
#-máximo
#-Tipos de violencia según edad (física, sexual, laboral, económica, institucional)
#-Tipos de violencia según género (por género)
#-Tipos de violencia según vínculo (por tipo de violencia)


print(totalCasos())