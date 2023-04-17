#pip install numpy
#pip install pandas
#pip install matplotlib
#pip install openpyxl
#pip install seaborn

#https://www.youtube.com/watch?v=c_8ymNccZwU
#https://www.youtube.com/watch?v=foLHkB6W_Ww

import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns


## Datos IRIS
datos = pd.read_csv("iris.csv", index_col=0)

print(datos)

datos.info()

## DATOS POBLACIONES

data_url = 'http://bit.ly/2cLzoxH'
pobla = pd.read_csv(data_url)
print(pobla.head(3))
pobla.info()

pobla_1952=pobla[pobla.year==1952]

print(pobla_1952.head(3))
pobla_1952.info()



# MANEJO DE TABLAS
# https://www.analyticslane.com/2018/11/23/tablas-dinamicas-en-python-con-pandas/

pobla_1952.pivot_table('pop', 'continent', aggfunc=np.sum)

pobla.pivot_table('pop', ['continent', 'year'], aggfunc=np.sum)

pobla.pivot_table('pop', ['continent', 'year'], aggfunc=np.sum)

pobla.pivot_table('pop','year', 'continent', aggfunc=np.sum)

datos.pivot_table(['slength', 'swidth'], ['class'], aggfunc=np.sum)
datos.pivot_table(['slength', 'swidth'], ['class'], aggfunc=np.mean)


pobla_1952.pivot_table(index='continent', aggfunc={'pop':np.sum, 'lifeExp':np.mean})


pobla_1952.pivot_table(index='continent', 
                       values = ['pop','lifeExp'],
                       aggfunc=[np.sum, np.mean, np.median])


np.percentile(pobla_1952['lifeExp'], 5)
np.percentile(pobla_1952['lifeExp'], 25)
np.percentile(pobla_1952['lifeExp'], 50)
np.percentile(pobla_1952['lifeExp'], 75)
np.percentile(pobla_1952['lifeExp'], 95)


datos.pivot_table(index='class', 
                       values = ['slength','swidth'],
                       aggfunc=[np.mean, np.median])





#GRÁFICO DE TORTA
# https://numython.github.io/posts/graficas-de-pastel-con-matplotlib/

## USANDO IRIS
datos_agrup=datos.groupby(['class']).size().reset_index(name='q_flor')


plt.pie(datos_agrup['q_flor'], labels=["setosa","versicolor","virginica"])
plt.show()

plt.pie(datos_agrup['q_flor'], labels=["setosa","versicolor","virginica"], autopct="%0.1f %%")
plt.show()

colores = ["#EE6055","#60D394","#AAF683"]

plt.pie(datos_agrup['q_flor'], labels=["setosa","versicolor","virginica"], autopct="%0.1f %%", colors=colores)
plt.show()


## USANDO POBLACION
pobla_agrup=pobla_1952.groupby('continent')['pop'].sum()

colores_pobla = ["#EE6055","#60D394","#AAF683", "#FFD97D","#FF9B85" ]

plt.pie(pobla_agrup, labels=["Africa","Americas","Asia","Europe","Oceania"], 
        autopct="%0.1f %%", colors=colores_pobla)
plt.show()


desfase = (0, 0, 0.1, 0, 0)
plt.pie(pobla_agrup, labels=["Africa","Americas","Asia","Europe","Oceania"], 
        autopct="%0.1f %%", colors=colores_pobla, explode=desfase)

plt.axis("equal")
plt.show()



#HISTOGRAMA

plt.hist(datos['slength'], 15, color="blue",ec="black")
plt.show()


#GRAFICO DE DISPERSIÓN

#USANDO IRIS
plt.scatter(datos['slength'], datos['swidth'])
plt.show()

plt.scatter(datos['slength'], datos['swidth'], marker='*')
plt.show()


g =sns.scatterplot(x='slength', y='swidth',hue='class',data=datos)
plt.show()

g =sns.scatterplot(x='slength', y='swidth',hue='class',data=datos, palette=colores)
plt.show()

 #USANDO POBLACION

g =sns.scatterplot(x='lifeExp', y='gdpPercap',hue='continent',data=pobla_1952, palette=colores_pobla)
plt.show()


pobla_1952[pobla_1952.gdpPercap>100000]

g =sns.scatterplot(x='lifeExp', y='gdpPercap',hue='continent',data=pobla_1952[pobla_1952.gdpPercap<100000], palette=colores_pobla)
plt.show()




# GRÁFICO DE BARRAS AGRUPADAS  ----quede acá
# https://analisisydecision.es/graficos-descriptivos-basicos-con-seaborn-python/

datos['slength_mayor5'] = np.where(datos['slength'] > 5,"Si", "No")

agr = datos.groupby(['class', 'slength_mayor5']).size().reset_index().pivot(columns='slength_mayor5', index='class', values=0)
agr.plot(kind='bar', stacked=True)
plt.show()



## GRÁFICO DE BARRA EVOLUCIÓN EN EL TIEMPO
# https://www.analyticslane.com/2018/11/23/tablas-dinamicas-en-python-con-pandas/
# https://swcarpentry-ja.github.io/python-novice-gapminder/es/_episodes/09-plotting/index.html

pobla_year=pobla.groupby('year')['pop'].sum()

pobla_year.T.plot()
plt.ylabel('Población')
plt.show()


pobla_year_conti=pobla.pivot_table(index='continent', columns='year', aggfunc={'pop': np.sum})


pobla_year_conti.T.plot()
plt.ylabel('Población')
plt.xlabel('Año')
plt.show()



## BOX PLOT 
# https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/

plt.boxplot(datos[datos['class']=='setosa'].slength)
plt.show()

plt.boxplot(datos[datos['class']=='setosa'].plength)
plt.show()


datos_box=datos[datos['class']=='setosa']

datos_box=datos_box[['slength','swidth','plength','pwidth']]
# datos_box=datos_box[['slength','swidth']]

plt.boxplot(datos_box)
plt.show()

# https://towardsdatascience.com/scattered-boxplots-graphing-experimental-results-with-matplotlib-seaborn-and-pandas-81f9fa8a1801

vals, names, xs = [],[],[]
for i, col in enumerate(datos_box.columns):
    vals.append(datos_box[col].values)
    names.append(col)
    xs.append(np.random.normal(i + 1, 0.04, datos_box[col].values.shape[0]))  # adds jitter to the data points - can be adjusted

plt.boxplot(vals, labels=names)
palette = ['r', 'g', 'b', 'y']
for x, val, c in zip(xs, vals, palette):
    plt.scatter(x, val, alpha=0.4, color=c)
plt.show()   