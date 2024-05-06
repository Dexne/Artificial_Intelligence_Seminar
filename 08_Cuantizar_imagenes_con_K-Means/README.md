# Técnicas de Clustering

En este notebook se explora una técnica de clustering llamada K-means para cuantizar una imagen. El objetivo es reducir el número de colores en una imagen manteniendo su apariencia visual lo más cercana posible a la original.

## Descripción

El proceso de cuantización de imagen con K-means implica agrupar los píxeles de una imagen en un número predefinido de clusters (representativos de colores) de acuerdo con su similitud. Cada píxel en la imagen se asigna al cluster más cercano en términos de distancia euclidiana en el espacio de color RGB.

## Procedimiento

1. **Carga de la Imagen**: Se carga la imagen que se va a cuantizar y se normaliza para que los valores de los píxeles estén en el rango [0, 1].

2. **Reducción de Dimensionalidad**: Se redimensiona la imagen para obtener una matriz de píxeles (muestras) y se toma una muestra aleatoria de píxeles para acelerar el proceso de clustering.

3. **Clustering con K-means**: Se aplica el algoritmo K-means a la muestra de píxeles para identificar los clusters representativos de colores.

4. **Asignación de Colores**: Se asigna a cada píxel de la imagen original el color del centroide del cluster al que pertenece.

5. **Visualización**: Se visualiza la imagen original y la imagen cuantizada con K-means para comparar los resultados.

## Instrucciones de Ejecución

1. Ejecute cada celda del notebook en orden para cargar la imagen, realizar la cuantización con K-means y visualizar los resultados.
  
2. Ajuste el parámetro `n_classes` para cambiar el número de colores en la imagen cuantizada.

3. Analice la imagen cuantizada para observar cómo se reducen los colores manteniendo una apariencia visual similar a la original.

**Nota:** Este notebook utiliza la biblioteca scikit-learn para aplicar el algoritmo K-means y la biblioteca matplotlib para visualizar la imagen original y la imagen cuantizada. Asegúrese de tener estas bibliotecas instaladas antes de ejecutar el código.

Puedes instalarlas mediante PIP con el siguiente comando:

```
pip install numpy matplotlib scikit-learn
```

## Resultados:

Imagen original

![Original](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/08_Cuantizar_imagenes_con_K-Means/img/frutas.jpg)

Imagen con dos colores

![dosColores](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/08_Cuantizar_imagenes_con_K-Means/img/Quantized_image_2_colores.png)

Imagen con ocho colores

![ochoColores](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/08_Cuantizar_imagenes_con_K-Means/img/Quantized_image_2_colores.png)

Imagen con 32 colores

![colores32](https://github.com/Dexne/Artificial_Intelligence_Seminar/blob/main/08_Cuantizar_imagenes_con_K-Means/img/Quantized_image_32_colores.png)


## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevas características, siéntete libre de abrir un issue o enviar un pull request.
