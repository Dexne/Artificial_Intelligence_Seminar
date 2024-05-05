# Comparación de Clasificadores

Este notebook compara el rendimiento de varios clasificadores utilizando conjuntos de datos generados artificialmente.

## Descripción

En este notebook, se compara el rendimiento de varios algoritmos de clasificación utilizando tres conjuntos de datos generados artificialmente: moons, circles y linearly separable. Se exploran las fronteras de decisión generadas por los clasificadores y se evalúa su rendimiento en términos de precisión tanto en los datos de entrenamiento como en los datos de prueba.

## Clasificadores Utilizados

1. **K vecinos más cercanos (KNN)**: Un algoritmo de clasificación basado en la cercanía entre los puntos de datos en el espacio de características.
  
2. **Máquinas de Vectores de Soporte (SVM)**: Un algoritmo de clasificación que encuentra el hiperplano óptimo que separa las clases en el espacio de características.

3. **Proceso Gaussiano (GP)**: Un método probabilístico no paramétrico para la clasificación.

4. **Árbol de Decisión (DT)**: Un método de clasificación que divide iterativamente el espacio de características en regiones para separar las clases.

5. **Red Neuronal Multicapa (MLP)**: Un modelo de red neuronal artificial con múltiples capas de neuronas.

6. **Naive Bayes**: Un algoritmo de clasificación basado en el teorema de Bayes y la suposición ingenua de independencia entre las características.

## Conjuntos de Datos Utilizados

1. **Moons**: Un conjunto de datos con dos clases generadas como dos semicírculos entrelazados.
  
2. **Circles**: Un conjunto de datos con dos clases generadas como dos círculos concéntricos.
  
3. **Linearly Separable**: Un conjunto de datos con dos clases generadas linealmente separables.

## Resultados

Los clasificadores se evalúan en términos de su capacidad para separar las clases en los conjuntos de datos proporcionados. Se muestra la frontera de decisión generada por cada clasificador y se calcula la precisión en los conjuntos de datos de entrenamiento y prueba.

**KNN**

![KNN](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/05_Comparaci%C3%B3n_de_clasificadores/img/01_KNN.png)

**SVM**
![SVM](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/05_Comparaci%C3%B3n_de_clasificadores/img/02_SVM.png)

**Proceso Gaussiano**
![Proceso_Gaussiano](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/05_Comparaci%C3%B3n_de_clasificadores/img/03_Proceso_Gaussiano.png)

**Árbol de Decision**
![DecisionTree](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/05_Comparaci%C3%B3n_de_clasificadores/img/04_DecisionTree.png)

**MLP**
![MLP](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/05_Comparaci%C3%B3n_de_clasificadores/img/05_MLP.png)

**Bayes**
![Bayes](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/05_Comparaci%C3%B3n_de_clasificadores/img/06_Bayes.png)

## Instrucciones de Ejecución

1. Ejecute cada celda del notebook en orden para cargar los datos, entrenar los clasificadores y visualizar los resultados.
  
2. Analice las fronteras de decisión generadas por cada clasificador y compare su rendimiento en los diferentes conjuntos de datos.

**Nota:** Es posible que se requieran ciertas bibliotecas de Python, como scikit-learn y matplotlib, para ejecutar este notebook. Asegúrese de tenerlas instaladas antes de ejecutar el código.

Para instalar las librerías puede hacerlo mediante PIP con el siguiente comando:

```
pip install numpy matplotlib scikit-learn
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.
