# Linear Regression

# importamos los modulos y librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# Falta el CSV
data = pd.read_csv('countries.csv')
data_mex = data[data.country == 'Mexico']
#data_mex.plot.scatter(x='year', y='lifeExp')

# Entrada y salida
x = np.asanyarray(data_mex[['year']])
y = np.asanyarray(data_mex[['lifeExp']])

# Creacion de modelo
model = linear_model.LinearRegression()
model.fit(x,y)
ypred = model.predict(x)
plt.scatter(x,y)
plt.plot(x,ypred, '--r')

# Hacemos prediccion
model.predict([[1955]])

# Calcular el error absoluto medio
#from sklearn.metrics import mean_absolute_error
#print(mean_absolute_error(y,ypred))

# Calcular el error cuadratico medio
#from sklearn.metrics import mean_squared_error
#print(mean_squared_error(y,ypred))

# Calcular el r2
from sklearn.metrics import r2_score
print(r2_score(y,ypred))