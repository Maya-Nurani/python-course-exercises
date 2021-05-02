import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def y(x):
    return np.power(x, 3) - 2*np.power(x, 2);

def z(y):
    return np.sqrt(np.power(np.e,y))


#x_arr = random.normal(loc=0, scale=2, size=(10000))
x_arr = [1,2,3,4,5]
y_arr = np.array([y(xi) for xi in x_arr])
z_arr = np.array([z(yi) for yi in y_arr])

print (x_arr)
print (y_arr)
print (x_arr)
print (z_arr)