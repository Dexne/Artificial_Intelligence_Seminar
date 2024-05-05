# Modelos de Regresión No Lineal

Este cuaderno de Google Colab que contiene la implementación de varios modelos de regresión no lineal utilizando diferentes algoritmos de aprendizaje automático como árboles de decisión, k vecinos más cercanos (KNN), máquinas de vectores de soporte (SVM), kernel ridge, y redes neuronales artificiales (MLP).

## Descripción del Contenido

El cuaderno `Modelos_de_Regresion_No_Lineal.ipynb` presenta la implementación de los siguientes modelos de regresión no lineal:

- Árbol de decisión
- K vecinos más cercanos (KNN)
- Máquinas de vectores de soporte (SVM)
- Kernel Ridge
- Redes Neuronales Artificiales (MLP)

## Descripción de los algoritmos:

- **Árbol de decisión**: Un árbol de decisión es un modelo de aprendizaje automático que toma decisiones basadas en una estructura de árbol. Cada nodo interno representa una característica (o atributo), cada rama representa una regla de decisión y cada nodo hoja representa el resultado de la decisión. Los árboles de decisión son útiles para problemas de clasificación y regresión, y son fáciles de interpretar.

![Foto1](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/04_Modelos_de_Regresion_No_Lineal/img/DecisionTreeRegressor.png)

- **K vecinos más cercanos (KNN)**: KNN es un algoritmo de aprendizaje automático que clasifica un punto de datos en función de la mayoría de los votos de sus vecinos más cercanos. Es un método no paramétrico, lo que significa que no hace suposiciones explícitas sobre la forma funcional de los datos. KNN es simple y fácil de entender, pero puede volverse computacionalmente costoso para conjuntos de datos grandes.

![Foto2](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/04_Modelos_de_Regresion_No_Lineal/img/KNeighborsRegressor.png)

- **Máquinas de vectores de soporte (SVM)**: SVM es un algoritmo de aprendizaje supervisado que se utiliza tanto para problemas de clasificación como de regresión. El objetivo de SVM es encontrar el hiperplano óptimo que mejor separa las clases en el espacio de características. SVM es efectivo en espacios de alta dimensionalidad y es útil cuando hay una clara separación entre las clases.

![Foto3](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/04_Modelos_de_Regresion_No_Lineal/img/SVR.png)

- **Kernel Ridge**: Kernel Ridge es un método de regresión que combina la regresión ridge con la técnica del kernel. Utiliza una función de kernel para proyectar los datos en un espacio de características de mayor dimensionalidad, donde se pueden encontrar relaciones no lineales entre las características. Kernel Ridge es útil para problemas de regresión no lineal y puede manejar datos con alta complejidad.

![Kernel Ridge](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/04_Modelos_de_Regresion_No_Lineal/img/KernelRidge.png)

- **Redes Neuronales Artificiales (MLP)**: MLP es un modelo de aprendizaje profundo que consiste en múltiples capas de neuronas interconectadas. Cada neurona en una capa está conectada a todas las neuronas de la capa anterior y posterior. MLP utiliza una función de activación no lineal para aprender relaciones complejas en los datos. Es altamente adaptable y puede ser utilizado para una amplia gama de problemas de clasificación y regresión.

![MLPRegressor](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/04_Modelos_de_Regresion_No_Lineal/img/MLPRegressor.png)
## Requisitos

Para ejecutar este cuaderno, necesitas tener instaladas las siguientes bibliotecas de Python:

- numpy
- matplotlib
- scikit-learn

Puedes instalar estas dependencias utilizando pip:

```
pip install numpy matplotlib scikit-learn

```


## Uso

Puedes ejecutar el cuaderno `Modelos_de_Regresion_No_Lineal.ipynb` en tu entorno de Jupyter Notebook o en Google Colab. Asegúrate de tener instaladas todas las dependencias necesarias.

## Resultados

Se presentan los puntajes (scores) de cada modelo tanto en el conjunto de entrenamiento como en el conjunto de prueba. Además, se muestra la visualización de las predicciones de cada modelo en comparación con los datos de entrenamiento y prueba.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.
