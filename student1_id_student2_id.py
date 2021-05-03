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
print("Number of rows = ", rows)
# computing number of columns
cols = len(flights_data_df.axes[1])
print("Number of columns = ", cols)

# Part B question 3
print("Columns names: ", list(flights_data_df.columns))
print("Print columns that contain NaN values", flights_data_df.columns[flights_data_df.isnull().any()].tolist())

# Part B question 4
print("The most frequent day is:", flights_data_df['Day'].value_counts().idxmax())

# Part B - queries - 1
print("The state in USA that have the most number of flights is ", flights_data_df['Carrier'].value_counts().idxmax())

# Part B - queries - 2
print("The number of flights to EWR,New-york destination is",
      flights_data_df.groupby('Dest').count()['flightId']['EWR'])

# Part B - queries - 3
print("The number of flights that departure from DCA and arrived to JFK is",
      flights_data_df[(flights_data_df['Dest'] == 'JFK') & (flights_data_df['Origin'] == 'DCA')].count()['flightId'])

# Part B - queries - 4
num_delayed_flights = flights_data_df[flights_data_df['Delayed'] == 1].count()['flightId']
print("The percentage of delayed flights out of all flights is", (num_delayed_flights/rows)*100, "%")

# Part B - queries - 5
num_delayed_flights_and_rainy = flights_data_df[(flights_data_df['Delayed'] == 1) & (flights_data_df['Weather'] == 2)].count()['flightId']
print("The percentage of delayed and cloudy flights out of all flights is", (num_delayed_flights_and_rainy/rows)*100, "%")

# Part B - queries - 6
unique_distances = flights_data_df[flights_data_df['Carrier'] == 'DH']['Dest'].unique()
print("The unique different destinations for DH Carrier are:", unique_distances)

# Part B - queries - 7
dt = flights_data_df['DepTime']
num_morning_flights = flights_data_df[(dt >= 1000) & (dt <= 1500)].count()['flightId']
print("The number of flights that departure between 10:00 to 15:00 is", num_morning_flights)

# Part B - queries - 8
dt = flights_data_df['DepTime']
num_morning_flights = flights_data_df[(dt >= 1400) & (dt <= 1700) & (flights_data_df['Day'] == 'WED')].count()['flightId']
print("The number of flights that departure between 14:00 to 17:00 and day = Wednesday is", num_morning_flights)

