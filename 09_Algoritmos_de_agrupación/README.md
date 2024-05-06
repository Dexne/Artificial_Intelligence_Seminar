# Comparación de Algoritmos de Agrupación

Este proyecto realiza una comparación de diferentes algoritmos de agrupación utilizando conjuntos de datos generados artificialmente. Se utilizan diversos algoritmos de agrupación, incluidos K-Means, Birch, Spectral Clustering, Gaussian Mixture, OPTICS y DBSCAN, para agrupar conjuntos de datos con diferentes estructuras y distribuciones.

## Conjuntos de Datos Utilizados

Se utilizan seis conjuntos de datos generados artificialmente para evaluar el rendimiento de los algoritmos de agrupación:

1. **Círculos Concéntricos:** Conjunto de datos con dos círculos concéntricos.
2. **Lunas:** Conjunto de datos con dos lunas intercaladas.
3. **Blobs:** Conjunto de datos con tres grupos de puntos distribuidos aleatoriamente.
4. **Plano sin Agrupaciones:** Conjunto de datos con puntos distribuidos uniformemente en un plano.
5. **Blobs con Deformación Anisotrópica:** Conjunto de datos con tres grupos de puntos con deformación anisotrópica.
6. **Blobs con Varias Varianzas:** Conjunto de datos con tres grupos de puntos con diferentes varianzas.

## Resultados y Visualización

Los resultados de los diferentes algoritmos de agrupación se visualizan en gráficos para cada conjunto de datos. Se comparan las agrupaciones obtenidas por cada algoritmo y se evalúa su rendimiento utilizando métricas como la homogeneidad, la completitud y la puntuación Fowlkes-Mallows.

Datos
![Normal]()

KMeans
![Kmeans]()

Birch
![Birch]()

SpectralClustering
![SpectralClustering]()

GaussianMixture
![GaussianMixture]()

OPTICS
![OPTICS]()

BDSCAN
![BDSCAN]()


## Bibliotecas Utilizadas

El proyecto utiliza las siguientes bibliotecas de Python:

- **scikit-learn:** Para la implementación de los algoritmos de agrupación y la generación de datos artificiales.
- **numpy:** Para operaciones numéricas.
- **matplotlib:** Para la visualización de datos.
- **StandardScaler:** De scikit-learn, para estandarizar los conjuntos de datos.
- **mixture:** De scikit-learn, para implementar el algoritmo de mezcla gaussiana.
- **SpectralClustering:** De scikit-learn, para implementar el agrupamiento espectral.
- **DBSCAN:** De scikit-learn, para implementar el algoritmo de agrupamiento basado en densidad.

## Instalación

Para ejecutar el código, es necesario tener instaladas las bibliotecas mencionadas. Puedes instalarlas utilizando `pip`:

```
pip install scikit-learn numpy matplotlib
```

---


## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.