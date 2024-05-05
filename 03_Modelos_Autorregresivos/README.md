# Modelos Autorregresivos (AR)

Este repositorio contiene un cuaderno de Google Colab que implementa un modelo autorregresivo (AR) para predecir las temperaturas diarias mínimas utilizando la biblioteca pandas, numpy y scikit-learn.

## Descripción del Contenido

El cuaderno `modelos_autorregresivos.py` contiene el código que carga los datos de temperaturas diarias mínimas desde un archivo CSV, visualiza los datos, calcula la correlación y la autocorrelación, crea una matriz de datos con valores de días anteriores para hacer predicciones, y entrena un modelo de regresión lineal para predecir las temperaturas.

## Requisitos

Para ejecutar este cuaderno, necesitas tener instaladas las siguientes bibliotecas de Python:

- pandas
- numpy
- matplotlib
- scikit-learn

Puedes instalar estas dependencias utilizando pip:

```
pip install pandas numpy matplotlib scikit-learn
```

## Uso

Puedes ejecutar el cuaderno `modelos_autorregresivos.py` en tu entorno de Google Colab. Asegúrate de tener el archivo `daily-min-temperatures.csv` en el mismo directorio que el cuaderno.

## Resultados

El cuaderno proporciona el puntaje (score) del modelo tanto en el conjunto de entrenamiento como en el conjunto de prueba.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.
