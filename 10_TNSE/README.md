# Reducción de dimensionalidad con t-SNE (MNIST)

Este cuaderno de Jupyter implementa la técnica de reducción de dimensionalidad t-distributed Stochastic Neighbor Embedding (t-SNE) en el conjunto de datos MNIST. El objetivo es visualizar datos de alta dimensionalidad en un espacio bidimensional de manera que se conserven las relaciones entre los puntos.

## Conjunto de Datos MNIST

El conjunto de datos MNIST contiene imágenes de dígitos escritos a mano, cada una representada como una matriz de píxeles. Cada imagen tiene una etiqueta que indica el dígito que representa.

## Funcionamiento del Cuaderno

1. **Lectura de Datos:** Se lee el conjunto de datos MNIST, que incluye imágenes de dígitos y las etiquetas correspondientes.
2. **Selección de Variables:** Se selecciona un subconjunto de muestras y características del conjunto de datos para acelerar el proceso de cálculo.
3. **Reducción de Dimensionalidad:** Se aplica la técnica t-SNE para reducir la dimensionalidad del conjunto de datos a 2 dimensiones.
4. **Visualización:** Se visualiza el conjunto de datos reducido en un gráfico de dispersión, donde cada punto representa una muestra y el color indica la etiqueta del dígito.

## Bibliotecas Utilizadas

El cuaderno utiliza las siguientes bibliotecas de Python:

- **pandas:** Para la lectura y manipulación de datos tabulares.
- **numpy:** Para operaciones numéricas.
- **matplotlib:** Para la visualización de datos.
- **sklearn:** Para implementar el algoritmo t-SNE y la manipulación de datos.

## Instalación

Para ejecutar el código, asegúrate de tener instaladas las bibliotecas mencionadas. Puedes instalarlas utilizando `pip`

```
pip install scikit-learn numpy matplotlib
```

## Resultados:

![digitosAgrupados](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/10_TNSE/digitosAgrupados.png)

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.