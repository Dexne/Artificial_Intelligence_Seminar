# Regresión Lineal para predecir la esperanza de vida

Este proyecto utiliza regresión lineal para predecir la esperanza de vida en México a lo largo del tiempo.

## Requisitos
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- scikit-learn

## Instalació de dependencias
Para instalar las dependencias necesarias utilizando pip:

```
pip install pandas numpy matplotlib scikit-learn
```

## Uso

1. Descarga el archivo CSV `countries.csv` que contiene los datos de esperanza de vida por país y año.
2. Ejecuta el script `main.py` en tu entorno de Python.

## Descripción del Código

- El script importa los módulos y librerías necesarias.
- Lee los datos del archivo CSV y filtra los datos para México.
- Define las variables de entrada (año) y salida (esperanza de vida).
- Crea un modelo de regresión lineal y lo entrena con los datos de entrada y salida.
- Realiza predicciones utilizando el modelo entrenado.
- Calcula el coeficiente de determinación (R^2) como medida de la precisión del modelo.

## Contribución

Si deseas contribuir a este proyecto, ¡eres bienvenido! Siéntete libre de hacer un fork del repositorio, hacer cambios y enviar un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo `LICENSE`.