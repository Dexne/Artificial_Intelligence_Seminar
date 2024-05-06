# -*- coding: utf-8 -*-
"""MNIST_con_Scaler_PCA_SVM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UTPRwIIHCPyWgZgA69KozUAeXEVQTGaj
"""

# MNIST con Scaler PCA SVM

# Importamos los modulos y librerias necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline

"""Leemos datos"""

# Specify the delimiter and error handling
data = pd.read_csv('/content/mnist_784.csv')

data

# Definimos número de muestras
n_samples = 70000 # Dependiendo de la computadora, podemos tomar menos muestras

x = np.asanyarray(data.drop(columns=['class']))[:n_samples,:]
y = np.asanyarray(data[['class']])[:n_samples].ravel()

# Dividir para entrenar y pruebas
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.1)

xtrain.shape

# Pipeline
model = Pipeline([
      ('scaler', StandardScaler()),
      ('pca', PCA(n_components=50)),
      ('svm', svm.SVC(gamma=0.0001))
])

# Entrenamos
model.fit(xtrain, ytrain)

# metricas
print('Train: ', model.score(xtrain, ytrain))
print('Test: ', model.score(xtest, ytest))
#Train:  0.9227619047619048
#Test:  0.9202857142857143

ypred = model.predict(xtest)

print('Classification report: \n', metrics.classification_report(ytest, ypred))

print('Confusion matrix: \n', metrics.confusion_matrix(ytest, ypred))

sample = np.random.randint(xtest.shape[0])
plt.imshow(xtest[sample].reshape((28,28)), cmap=plt.cm.gray)
plt.title('Prediction: %i' % ypred[sample])
plt.show()