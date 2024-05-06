# Clasificación de Dígitos

Este notebook implementa un clasificador de dígitos utilizando el conjunto de datos de dígitos de la biblioteca scikit-learn. Se utiliza una Máquina de Vectores de Soporte (SVM) como modelo de clasificación y se evalúa su rendimiento utilizando varias métricas de evaluación.

## Descripción

En este notebook, se carga el conjunto de datos de dígitos y se muestra una imagen de un dígito de manera aleatoria. Luego, se preparan los datos para el entrenamiento del modelo aplanando las imágenes y dividiendo el conjunto de datos en conjuntos de entrenamiento y prueba. Se utiliza una SVM como clasificador y se entrena sobre los datos de entrenamiento. Se evalúa el rendimiento del modelo en los datos de entrenamiento y prueba utilizando la precisión como métrica. Además, se generan métricas adicionales como el reporte de clasificación y la matriz de confusión para evaluar el rendimiento del modelo en detalle.

## Métricas Utilizadas

1. **Precisión**: La fracción de muestras clasificadas correctamente.
  
2. **Reporte de Clasificación**: Proporciona métricas de precisión, recall, f1-score y soporte para cada clase.
  
3. **Matriz de Confusión**: Muestra el número de muestras clasificadas correctamente e incorrectamente para cada clase.

## Instrucciones de Ejecución

1. Ejecute cada celda del notebook en orden para cargar los datos, entrenar el modelo y evaluar su rendimiento.
  
2. Analice las métricas proporcionadas para comprender el rendimiento del modelo en los datos de prueba y cómo se clasifican los diferentes dígitos.

**Nota:** Este notebook utiliza la biblioteca scikit-learn para cargar el conjunto de datos de dígitos, entrenar el modelo SVM y calcular las métricas de evaluación. Asegúrese de tener esta biblioteca instalada antes de ejecutar el código.

Puedes instalarlas mediante PIP con el siguiente comando:

```
pip install numpy matplotlib scikit-learn
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.