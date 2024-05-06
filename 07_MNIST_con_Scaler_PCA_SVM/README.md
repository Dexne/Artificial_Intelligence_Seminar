# MNIST con Escalado, PCA y SVM

Este notebook implementa un clasificador para el conjunto de datos MNIST utilizando un flujo de trabajo de preprocesamiento que incluye escalado, reducción de dimensionalidad mediante PCA y un modelo SVM para la clasificación.

## Descripción

En este notebook, se carga el conjunto de datos MNIST que contiene imágenes de dígitos escritos a mano junto con sus etiquetas correspondientes. Se realiza un preprocesamiento de los datos que incluye el escalado de las características y la reducción de dimensionalidad utilizando PCA para seleccionar las características más importantes. Luego, se entrena un clasificador SVM sobre los datos preprocesados y se evalúa su rendimiento en los datos de prueba.

## Procedimiento

1. **Carga de Datos**: Se cargan los datos del conjunto de datos MNIST que contiene imágenes de dígitos escritos a mano.

2. **Preprocesamiento**: Se preprocesan los datos mediante un flujo de trabajo que incluye el escalado de las características y la reducción de dimensionalidad utilizando PCA para seleccionar las características más importantes.

3. **Entrenamiento del Modelo**: Se entrena un modelo SVM sobre los datos preprocesados utilizando un pipeline que incluye el escalado, PCA y SVM.

4. **Evaluación del Modelo**: Se evalúa el rendimiento del modelo entrenado en los datos de prueba mediante la precisión y otras métricas como el reporte de clasificación y la matriz de confusión.

## Métricas Utilizadas

1. **Precisión**: La fracción de muestras clasificadas correctamente.
  
2. **Reporte de Clasificación**: Proporciona métricas de precisión, recall, f1-score y soporte para cada clase.
  
3. **Matriz de Confusión**: Muestra el número de muestras clasificadas correctamente e incorrectamente para cada clase.

## Instrucciones de Ejecución

1. Ejecute cada celda del notebook en orden para cargar los datos, preprocesarlos, entrenar el modelo y evaluar su rendimiento.
  
2. Analice las métricas proporcionadas para comprender el rendimiento del modelo en los datos de prueba y cómo se clasifican los diferentes dígitos.

**Nota:** Este notebook utiliza la biblioteca scikit-learn para cargar el conjunto de datos MNIST, preprocesar los datos, entrenar el modelo SVM y calcular las métricas de evaluación. Asegúrese de tener esta biblioteca instalada antes de ejecutar el código.

Puedes instalarlas mediante PIP con el siguiente comando:

```
pip install numpy matplotlib scikit-learn
```

## Resultados obtenidos:

![Figure1](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/07_MNIST_con_Scaler_PCA_SVM/img/Figure_1.png)
![Figure2](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/07_MNIST_con_Scaler_PCA_SVM/img/Figure_2.png)
![Figure3](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/07_MNIST_con_Scaler_PCA_SVM/img/Figure_3.png)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.