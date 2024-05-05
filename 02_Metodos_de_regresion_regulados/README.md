# Métodos de Regresión Regulados

Este repositorio contiene código en Python que implementa varios métodos de regresión regulados, incluyendo Ridge, Lasso y ElasticNet, utilizando la biblioteca de scikit-learn.

Los métodos de regresión regularizados, como Ridge, Lasso y ElasticNet, son técnicas utilizadas en el aprendizaje automático para evitar el sobreajuste y mejorar la generalización del modelo. 

- **Ridge Regression**: Añade una penalización a los coeficientes del modelo, lo que ayuda a reducir la complejidad del modelo y a prevenir el sobreajuste. Es útil cuando hay multicolinealidad en los datos, es decir, cuando las variables independientes están correlacionadas entre sí.

- **Lasso Regression**: Similar a Ridge, pero además de penalizar la magnitud de los coeficientes, también puede reducir algunos de ellos a cero. Esto hace que Lasso sea útil para la selección automática de características, ya que puede eliminar variables irrelevantes.

- **ElasticNet**: Combina las penalizaciones de Ridge y Lasso, lo que permite abordar los problemas de multicolinealidad y la selección de características simultáneamente. Es especialmente útil cuando hay un gran número de características y muchas de ellas están altamente correlacionadas.

## Requisitos

Para ejecutar este script, es necesario tener instaladas las siguientes bibliotecas de python:

- Numpy
- Matplotlib
- scikit-learn

Puedes instalar estas dependecias usando pip:

```
pip install numpy matplotlib scikit-learn
```

## Uso

Puedes ejecutar el script `main.py` directamente desde la linea de comando o desde un entorno de desarrollo python.

Por ejemplo, para ejecutar el script, puedes usar el siguiente comando

- Si estas en Windows:

```
python main.py
```

- Si estas en Linux:

```
python3 main.py
```


## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el código o agregar nuevos métodos de regresión regulados, siéntete libre de abrir un issue o enviar un pull request.
