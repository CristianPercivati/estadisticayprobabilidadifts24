import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/content/drive/MyDrive/Estadística y Probabilidad/TP1/dataset2020.csv')

def totalCasos():
    return df.count()[0]

def agruparPorEdad():
  edades = ["de 0 a 10 años","de 10 a 20 años","de 20 a 30 años", "de 30 a 40 años", "de 40 a 50 años", "de 50 a 60 años", "más de 60 años"]
  cond = [(df['edad_persona_en_situacion_de_violencia']<10),(df['edad_persona_en_situacion_de_violencia']<20),(df['edad_persona_en_situacion_de_violencia']<30),(df['edad_persona_en_situacion_de_violencia']<40),(df['edad_persona_en_situacion_de_violencia']<50),(df['edad_persona_en_situacion_de_violencia']<=60),(df['edad_persona_en_situacion_de_violencia']>6)]
  df['grupo_edad'] = np.select(cond,edades)

def edadPromedio():
  return df['edad_persona_en_situacion_de_violencia'].mean()

def edadMax():
  return df['edad_persona_en_situacion_de_violencia'].max()

def edadMin():
  return df['edad_persona_en_situacion_de_violencia'].min()

def contarMenores():
  return df[(df.edad_persona_en_situacion_de_violencia<18) & (df.edad_persona_en_situacion_de_violencia>0)].count()[0]

def contarAdultos():
  return df[df.edad_persona_en_situacion_de_violencia>17].count()[0]

def contarEdadNoInformada():
  return df[df.edad_persona_en_situacion_de_violencia==0].count()[0]

def vinculoAgresorPorEdad():
  menores = df[(df.edad_persona_en_situacion_de_violencia<18) & (df.edad_persona_en_situacion_de_violencia>0)]
  mayores = df[df.edad_persona_en_situacion_de_violencia>17]

def totalProvincia():
  totalesPorProv = df.groupby('Ubicación').genero_persona_en_situacion_de_violencia.count()
  return totalesPorProv

def maxProvincia():
  totalesPorProv = df.groupby('Ubicación').genero_persona_en_situacion_de_violencia.count()
  return [totalesPorProv.idxmax(), totalesPorProv.max()]

def minProvincia():
  totalesPorProv = df.groupby('Ubicación').genero_persona_en_situacion_de_violencia.min()[1]
  return totalesPorProv


print(maxProvincia())


#def distribucionProvincias():
#   return [maxima, minima, totalProvincia]

#def distribucionEdad():
#-cantidad de menores y adultos
#-vínculo con el agresor
#-edad menor
#-edad mayor
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

#¿Cuál es la distribución de las llamadas por edad y género de la víctima? ¿Hay grupos de edad o género que llaman con más frecuencia?
#¿Cuál es la distribución geográfica de las llamadas, es decir, cuáles son las provincias con mayor cantidad de llamadas al 144? ¿Hay diferencias significativas en la distribución de llamadas entre provincias?
#¿Cuáles son los tipos de violencia más frecuentes mencionados en las llamadas? ¿Hay diferencias en los tipos de violencia reportados según el género de la víctima o el vínculo con el agresor?
#¿Hay patrones significativos en el género del victimario reportado en las llamadas? ¿Hay diferencias en el género del victimario según el género de la víctima o el tipo de violencia reportado?
#Análisis de tendencias: ¿Hubo un aumento o disminución en la cantidad de llamadas recibidas en el 144 a lo largo del año 2020? ¿Hay patrones estacionales en la cantidad de llamadas, por ejemplo, más llamadas en ciertos meses del año que en otros?
#Análisis de asociación: ¿Hay asociaciones entre la edad de la víctima y el tipo de violencia reportado en las llamadas? ¿O entre el género de la víctima y el tipo de violencia? ¿Cómo se relaciona el tipo de violencia reportado con el vínculo con el agresor?
#Análisis de modelos predictivos: ¿Es posible predecir la probabilidad de que una llamada al 144 reporte un tipo de violencia específico en función de ciertas variables, como la edad o el género de la víctima, el vínculo con el agresor o la provincia donde se realiza la llamada?
#Análisis de correlación espacial: ¿Hay una correlación geográfica entre la cantidad de llamadas realizadas en una determinada provincia y los niveles de violencia de género informados en esa misma provincia en otros indicadores estadísticos, como denuncias en comisarías o casos de femicidio?
#Análisis de texto: ¿Es posible extraer patrones o temas recurrentes en los comentarios o descripciones incluidos en las llamadas al 144, utilizando técnicas de análisis de texto o minería de datos?

print(totalCasos())
