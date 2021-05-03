import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


def y(x):
    return np.power(x, 3) - 2 * np.power(x, 2);


def z(y):
    return np.sqrt(np.power(np.e, y))


# x_arr = random.normal(loc=0, scale=2, size=(10000))
# x array for an easy check of y and z
x_arr = [-2, 0, 2, 3, 4, 5]
y_arr = np.array([y(xi) for xi in x_arr])
z_arr = np.array([z(yi) for yi in y_arr])
dataset = pd.DataFrame({'x': x_arr, 'y': y_arr, 'z': z_arr})

# Check for dataset (DELETE AT FINISH)
print(dataset)

# Check for x,y and z arrays (DELETE AT FINISH)
print(x_arr)
print(y_arr)
print(z_arr)

# Part A question 1
print("The maximum value of y is: {0}".format(dataset['y'].max()))

# Part A question 2
print("The minimum value of z is: {0}".format(dataset['z'].min()))


# Part A question 3
def findDuplicates():
    return dataset[dataset['x'] == dataset['y']]


print("The duplicates between Y and Z are: \n {0}".format(findDuplicates()))

# Part A question 4
print("The first 5 rows of X and Z columns of the dataset: \n {0}".format(dataset[['x', 'z']].head()))

# Part A question 5
# def new_column_creation(x,y):
#   return 2*x-np.power(x,2)
# new_column = np.array([new_column_creation(i) for i in x_arr])

# Part B question 1
flights_data_df = pd.read_csv('flights.csv')

# Part B question 2
# number of rows
rows = len(flights_data_df.axes[0])
print("Number of rows = ", rows)
# computing number of columns
cols = len(flights_data_df.axes[1])
print("Number of columns = ", cols)

# Part B question 3
print("Columns names: ", list(flights_data_df.columns))
print("Print columns that contain NaN values", flights_data_df.columns[flights_data_df.isnull().any()].tolist())

# Part B question 4
print("The most frequent day is:", flights_data_df['Day'].value_counts().idxmax())

# Part C question 1
print("The state in USA that have the most number of flights is ", flights_data_df['Carrier'].value_counts().idxmax())

# Part C question 2
print("The number of flights to EWR,New-york destination is",
      flights_data_df.groupby('Dest').count()['flightId']['EWR'])

# Part C question 3
print("The number of flights that departure from DCA and arrived to JFK is",
      flights_data_df[(flights_data_df['Dest'] == 'JFK') & (flights_data_df['Origin'] == 'DCA')].count()['flightId'])
