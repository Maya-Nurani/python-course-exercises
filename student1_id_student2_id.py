import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


# Part A Dataframe creation
def y(x):
    return np.power(x, 3) - 2 * np.power(x, 2);


def z(y):
    return np.sqrt(np.power(np.e, y))


x_arr = random.normal(loc=0, scale=2, size=(10000))
y_arr = np.array([y(xi) for xi in x_arr])
z_arr = np.array([z(yi) for yi in y_arr])
dataset = pd.DataFrame({'x': x_arr, 'y': y_arr, 'z': z_arr})

# Check for dataset (DELETE AT FINISH)
print(dataset)

# Part A question 1
print("The maximum value of y is: {0}".format(dataset['y'].max()))

# Part A question 2
print("The minimum value of z is: {0}".format(dataset['z'].min()))


# Part A question 3
def find_duplicates():
    return dataset[dataset['x'] == dataset['y']]


print("The duplicates between Y and Z are: \n {0}".format(find_duplicates()))

# Part A question 4
print("The first 5 rows of X and Z columns of the dataset: \n {0}".format(dataset[['x', 'z']].head()))

# Part A question 5
dataset['newColumn'] = new_column = 2*dataset['x'] - np.power(dataset['y'], 2)


# Part A questions 6, 7, 8
def show_scatter(a,b):
    plt.scatter(dataset[a], dataset[b], color='purple')
    plt.xlabel(str(a) + ' Axis')
    plt.ylabel(str(b) + ' Axis')
    plt.grid(color='pink')
    plt.show()

show_scatter('x', 'y')
show_scatter('x', 'z')

print(dataset)

# Part A question 9
plt.scatter(np.arange(3500), dataset.sample(frac=0.35)['newColumn'], color='black')
plt.xlabel('Index')
plt.ylabel('2x-y^2')
plt.grid(color='green')
plt.show()

# Part B question 1
flights_data_df = pd.read_csv('flights.csv')

# Part B question 2
# number of rows
rows = len(flights_data_df.axes[0])
print(rows)
# computing number of columns
cols = len(flights_data_df.axes[1])
print(cols)

# Part B question 3
print("columns names: ", list(flights_data_df.columns))
