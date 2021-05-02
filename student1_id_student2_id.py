import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def y(x):
    return np.power(x, 3) - 2*np.power(x, 2);

def z(y):
    return np.sqrt(np.power(np.e,y))


#x_arr = random.normal(loc=0, scale=2, size=(10000))
#x array for an easy check of y and z
x_arr = [-2,0,2,3,4,5]
y_arr = np.array([y(xi) for xi in x_arr])
z_arr = np.array([z(yi) for yi in y_arr])
dataset = pd.DataFrame({'x': x_arr, 'y': y_arr, 'z':z_arr})

#Check for dataset (DELETE AT FINISH)
print (dataset)

#Check for x,y and z arrays (DELETE AT FINISH)
print (x_arr)
print (y_arr)
print (z_arr)

#Part A question 1
print("The maximum value of y is: {0}".format(dataset['y'].max()))

#Part A question 2
print("The minimum value of z is: {0}".format(dataset['z'].min()))

#Part A question 3 - NOT WORKING YET
print(dataset['y'].equals(dataset['x']))

#Part A question 4
print("The first 5 rows of X and Z columns of the dataset: \n {0}" .format(dataset[['x','z']].head()))

#Part A question 5
#def new_column_creation(x,y):
 #   return 2*x-np.power(x,2)
#new_column = np.array([new_column_creation(i) for i in x_arr])