# Metodos de regresion regulados

import numpy as np
import numpy.random as rnd
import matplotlib.pyplot as plt 

np.random.seed(42)

m = 100
X = 6 * np.random.rand(m,1) - 3
y = 0.5 * X**2 + X + 2 + np.random.randn(m,1)

plt.plot(X,y,"b.")
plt.xlabel("$x_1$",fontsize=18)
plt.ylabel("$y$",rotation=0,fontsize=18)
plt.axis([-3,3,0,10])
plt.show()

from sklearn.preprocessing import PolynomialFeatures
poly_features = PolynomialFeatures(degree=2, include_bias=False)
X_poly = poly_features.fit_transform(X)
X_poly[0]

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_poly,y)
print(lin_reg.intercept_,lin_reg.coef_)

X_new = np.linspace(-3, 3, 100).reshape(100, 1)
X_new_poly = poly_features.transform(X_new)
y_new = lin_reg.predict(X_new_poly)

plt.plot(X, y, "b.")
plt.plot(X_new, y_new, "r-", linewidth=2, label="Predictions")
plt.xlabel("$x_1$", fontsize=18)
plt.ylabel("$y$", rotation=0, fontsize=18)
plt.legend(loc="upper left", fontsize=14)
plt.axis([-3, 3, 0, 10])
plt.show()

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

model = Pipeline([
        ("poly", PolynomialFeatures(degree=3, include_bias=False)),
        ("scaler",StandardScaler()),
        ("reg", LinearRegression())])

model.fit(X,y)

y_new = model.predict(X_new)

plt.plot(X_new, y_new,'r-')

plt.plot(X,y,"b.",linewidth=3)
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.axis([-3,3,0,10])
plt.show()

# ####
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain,ytest = train_test_split(X,y)


model = Pipeline([
        ("poly", PolynomialFeatures(degree=2, include_bias=False)),
        ("scaler",StandardScaler()),
        ("reg", LinearRegression())])

model.fit(xtrain,ytrain)
print('Train: ', model.score(xtrain, ytrain))
print('Test: ', model.score(xtest, ytest))
# Dibujar
y_new = model.predict(X_new)
plt.plot(X_new, y_new,'k-')
plt.plot(xtrain,ytrain,"b.",linewidth=3)
plt.plot(xtest,ytest,"r.",linewidth=3)
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.axis([-3,3,0,10])
plt.show()

#
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

for style,width,degree in (("g-",1,300), ("k--",2,2), ("r--",2,1)):
    polybig_features = PolynomialFeatures(degree=degree, include_bias=False)
    std_scaler = StandardScaler()
    lin_reg = LinearRegression()
    polynomial_regression = Pipeline([
            ("poly_features", polybig_features),
            ("std_scaler", std_scaler),
            ("lin_reg", lin_reg),
        ])
    polynomial_regression.fit(X,y)
    y_newbig = polynomial_regression.predict(X_new)
    plt.plot(X_new, y_newbig,style,label=str(degree), linewidth=width)

plt.plot(X,y,"b.", linewidth=3)
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.axis([-3,3,0,10])
plt.show()

# ## Ridge ----

from sklearn.linear_model import Ridge

np.random.seed(42)
m = 20
X = 3 * np.random.randn(m,1)
y = 1 + 0.5 * X + np.random.randn(m,1)/1.5
X_new = np.linspace(0,3,100).reshape(100,1)

alpha = 0.01

model = Pipeline([  ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
                  ("std_scaler", StandardScaler()),
                  ("regul_reg", Ridge(alpha))])

model.fit(X,y)
y_new_regul = model.predict(X_new)
plt.plot(X_new,y_new_regul,'--r', linewidth=3,label=r"$\alpha = {}$".format(alpha))
plt.plot(X,y,'ob')
plt.legend()
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.axis([0,3,0,4])
plt.show()

from sklearn.linear_model import Lasso

alpha = 0.01

model = Pipeline([  ("poly_features",PolynomialFeatures(degree=100, include_bias=False)),
                  ("std_scaler", StandardScaler()),
                  ("regul_reg", Lasso(alpha))])
model.fit(X,y)
y_new_regul = model.predict(X_new)
plt.plot(X_new, y_new_regul, '--r', linewidth=3, label=r"$\alpha ={}$".format(alpha))
plt.plot(X,y,'ob')
plt.legend()
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.axis([0,3,0,4])
plt.show()

from sklearn.linear_model import ElasticNet

ElasticNet()
model = Pipeline([  ("poly_features", PolynomialFeatures(degree=10, include_bias=False)),
                  ("std_scaler", StandardScaler()),
                  ("regul_reg", ElasticNet(alpha=0.01, l1_ratio=0.001, random_state=42))])
model.fit(X,y)
y_new_regul = model.predict(X_new)
plt.plot(X_new, y_new_regul,'--r', linewidth=3, label=r"$\alpha = {}$".format(alpha))
plt.plot(X,y,'ob')
plt.legend()
plt.xlabel("$x_1$")
plt.ylabel("$y$")
plt.axis([0,3,0,4])
plt.show()
