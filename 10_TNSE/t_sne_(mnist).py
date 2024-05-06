# -*- coding: utf-8 -*-
"""t-SNE (MNIST).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12rN6d0jCnCbRSWd3VWovcbWfMicTKKDB
"""

# t-SNE(MNIST)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Leer datos
data = pd.read_csv('/content/mnist_784.csv')
n_samples = 5000

# Elegir variables
x = np.asanyarray(data.drop(columns=['class']))[:n_samples,:]
y = np.asanyarray(data[['class']])[:n_samples].ravel()

model = TSNE(n_components=2, n_iter=2000)

# Entrenamos
x_2d = model.fit_transform(x)
x_2d.shape

# Mostramos el gráfico
plt.scatter(x_2d[:,0], x_2d[:,1], c=y, cmap=plt.cm.tab10)
# Los colores son presentados por un color