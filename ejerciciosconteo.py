import numpy as np

# permutaciones: m!
# variaciones: m!/ (m-n)!
# combinaciones: m! / (m-n)!n!
# m: total del grupo. n: porción del grupo.

def permutacion(m):
  return np.math.factorial(m)

def variacion(m,n):
  res = np.math.factorial(m) / np.math.factorial(m-n)
  return res

def combinacion(m,n):
  res = np.math.factorial(m) / (np.math.factorial(m-n) * np.math.factorial(n))
  return res

#Ejercicio 1. ¿De cuántos modos diferentes se pueden ordenar los colores del arcoíris?
#Respuesta: 5040.
#print(permutacion(7))

#Ejercicio 2. ¿De cuántas formas distintas se pueden ordenar 10 libros en una biblioteca?
#Respuesta: 3.628.800.
#print(permutacion(10))


#Ejercicio 3. Un comité de ocho personas debe elegir un presidente, un vicepresidente y
#un secretario. ¿De cuántas maneras se puede hacer esta selección?
#Respuesta: 336
#print(variacion(8,3))

#Ejercicio 4. Un ingeniero químico está diseñando un experimento para determinar el
#efecto de temperatura, la razón de activación y el tipo de catalizador en la producción
#de reacción dada. Quiere estudiar cinco temperaturas diferentes de reacción, dos
#razones de activación distintas y cuatro catalizadores diferentes. Si cada operación del
#experimento implica la elección de una temperatura, una razón de activación y un
#catalizador, ¿cuántas operaciones diferentes son posibles?
#Respuesta: 40

#Ejercicio 5. Dado 9 puntos en un plano, ¿cuántos segmento diferentes que tengan 2 de
#esos puntos por extremos se pueden determinar?
#print(combinacion(9,2))
#Respuesta: 36

'''  
Ejercicio 6. Diez ingenieros han solicitado un puesto administrativo en una gran
empresa. Se seleccionará a cuatro de ellos como finalistas para el puesto. ¿De cuántas
maneras se puede hacer esta selección?

Respuesta: 210
Ejercicio 7. ¿Cuántos números pares de 5 cifras pueden formarse con: 1, 3, 2, 5, 9?

2
Respuesta: 24
Ejercicio 8. Alrededor de una mesa hay 6 sillas fijas. ¿De cuántas formas diferentes
pueden sentar 4 personas?

Respuesta: 360
Ejercicio 9. ¿Cuántos triángulos pueden formarse que tengan por vértices tres de los
vértices de un heptágono?

Respuesta: 35
Ejercicio 10. En cada una de las 4 secciones de un supermercado hay una vacante de
vendedor. Se presentan 20 personas a la entrevista. ¿En cuántas formas diferentes
pueden llenarse los puestos?

Respuesta: 116.280
Ejercicio 11. Entre 10 ingenieros y 8 abogados deben elegirse una comisión de 5
miembros integrada por 3 ingenieros y 2 abogados. ¿Cuántas comisiones distintas
pueden resultar?

Respuesta: 3.360

Ejercicios un poco diferentes para pensar.
Ejercicio 12. Una prueba consta de 15 preguntas. Diez son preguntas verdadero - falso
y cinco son de elección múltiple que tienen cuatro opciones cada una. Un estudiante
debe seleccionar una respuesta para cada pregunta. ¿De cuántas maneras se puede
hacer esta prueba?

Respuesta: 1.048.576
Ejercicio 13. Las placas constan de tres letras (elegidas entre 27 letras) seguidas de tres
números.
a) ¿Cuántas placas diferentes se pueden hacer?

3
Respuesta: 19.683.000

b) ¿Cuántas placas diferentes se pueden hacer de tal forma que ninguna letra o
número aparezca más de una vez?

Respuesta: 12.636.000
'''
