## lee este archvi csv 
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif


#Read dataset
motor_stock = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vS2xYo-awUaesdgZ6YoOPg3MJvdDCE1liVK0YzeKMkvkGUsftUja9lShR_qJQfZE7N2C5G5r1Hh0pUx/pub?gid=391234979&single=true&output=csv')



# motor_stock_transformed = motor_stock.drop(['car_ID'], axis=1)

##quitar el car_ID y el CarName
motor_stock_transformed = motor_stock.drop(['car_ID', 'CarName'], axis=1)

##quitar espacios vacios dentro de las celdas, que solo queden numeros
motor_stock_transformed = motor_stock_transformed.replace('?', np.nan)



motor_stock_transformed = pd.get_dummies(motor_stock_transformed, columns=['CarName', 'fueltype', 'aspiration', 'doornumber', 'carbody', 'drivewheel', 'enginelocation', 'enginetype', 'cylindernumber', 'fuelsystem',], dtype=float, drop_first=True)
motor_stock_transformed.to_csv('motor_stock_transformed.csv', index=False)


# corr = motor_stock_transformed.corr()
# print(corr)
# corr.to_csv('corr.csv', index=False)

# #hacer feature selection





# #correlation plot con el nombre de las variables
# # plt.matshow(motor_stock_transformed.corr())
# # plt.xticks(range(len(motor_stock_transformed.columns)), motor_stock_transformed.columns)
# # plt.yticks(range(len(motor_stock_transformed.columns)), motor_stock_transformed.columns)
# # plt.colorbar()
# # plt.show()





# y = motor_stock_transformed['price']
# x = motor_stock_transformed.drop(['price'], axis=1)
# print("x:  ")
# print(x)



# reg = LinearRegression().fit(x, y)

# # #Beta values

# print("\nBeta:\n")
# print(reg.coef_)

# print("\nBeta0:\n")
# print(reg.intercept_)




# # new_instances = [[321, 2.19, 85.17, 47.432], [325, 100, 0.1, 372.32]]

# # print("Regression Results for each instance:")
# # reg.predict(x)
# # print("Prediccion" , reg.predict(new_instances))