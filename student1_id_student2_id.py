import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


# Part A Dataframe creation
def y(x):
    return np.power(x, 3) - 2 * np.power(x, 2)


def z(y):
    return np.sqrt(np.power(np.e, y))


x_arr = random.normal(loc=0, scale=2, size=10000)
y_arr = np.array([y(xi) for xi in x_arr])
z_arr = np.array([z(yi) for yi in y_arr])
dataset = pd.DataFrame({'x': x_arr, 'y': y_arr, 'z': z_arr})

# Part A question 1
print("The maximum value of y is: {0}".format(dataset['y'].max()))

# Part A question 2
print("The minimum value of z is: {0}".format(dataset['z'].min()))


# Part A question 3
def find_duplicates():
    return dataset[dataset['y'] == dataset['z']]


print("The values with duplication between Y and Z are: \n {0}".format(find_duplicates()))

# Part A question 4
print("The first 5 rows of X and Z columns of the dataset: \n {0}".format(dataset[['x', 'z']].head()))

# Part A question 5
dataset['newColumn'] = 2 * dataset['x'] - np.power(dataset['y'], 2)


# Part A questions 6, 7, 8
def show_scatter(a, b):
    plt.scatter(dataset[a], dataset[b], color='purple')
    plt.xlabel(str(a) + ' Axis')
    plt.ylabel(str(b) + ' Axis')
    plt.grid(color='pink')
    plt.title('{0} on {1} columns graph'.format(b, a))
    plt.show()

show_scatter('x', 'y')
show_scatter('x', 'z')

# Part A question 9
plt.scatter(np.arange(3500), dataset.sample(frac=0.35)['newColumn'], color='black')
plt.xlabel('Index')
plt.ylabel('2x-y^2')
plt.grid(color='green')
plt.title('2x-y^2 column graph')
plt.show()

# Part B

# Part B question 1
flights_data_df = pd.read_csv('flights.csv')

# Part B question 2
# Number of rows
rows = len(flights_data_df.axes[0])
print("Number of rows = ", rows)
# Computing number of columns
cols = len(flights_data_df.axes[1])
print("Number of columns = ", cols)

# Part B question 3
print("Columns names: ", list(flights_data_df.columns))
print("Print columns that contain NaN values", flights_data_df.columns[flights_data_df.isnull().any()].tolist())

# Part B question 4
print("The most frequent day is:", flights_data_df['Day'].value_counts().idxmax())

# Part B - Queries
# Part B - query 1
print("The state in USA that have the most number of flights is ", flights_data_df['Carrier'].value_counts().idxmax())

# Part B - query 2
print("The number of flights to EWR,New-york destination is",
      flights_data_df.groupby('Dest').count()['flightId']['EWR'])

# Part B - query 3
print("The number of flights that departure from DCA and arrived to JFK is",
      flights_data_df[(flights_data_df['Dest'] == 'JFK') & (flights_data_df['Origin'] == 'DCA')].count()['flightId'])

# Part B - query 4
num_delayed_flights = flights_data_df[flights_data_df['Delayed'] == 1].count()['flightId']
print("The percentage of delayed flights out of all flights is", (num_delayed_flights / rows) * 100, "%")

# Part B - query 5
num_delayed_flights_and_rainy = \
    flights_data_df[(flights_data_df['Delayed'] == 1) & (flights_data_df['Weather'] == 2)].count()['flightId']
print("The percentage of delayed and cloudy flights out of all flights is",
      (num_delayed_flights_and_rainy / rows) * 100, "%")

# Part B - query 6
unique_distances = flights_data_df[flights_data_df['Carrier'] == 'DH']['Dest'].unique()
print("The unique different destinations for DH Carrier are:", unique_distances)

# keeping 'dt' column as a variable
dt = flights_data_df['DepTime']

# Part B - query  7
num_morning_flights = flights_data_df[(dt >= 1000) & (dt <= 1500)].count()['flightId']
print("The number of flights that departure between 10:00 to 15:00 is", num_morning_flights)

# Part B - query 8
num_WED_noon_flights = flights_data_df[(dt >= 1400) & (dt <= 1700) & (flights_data_df['Day'] == 'WED')].count()[
    'flightId']
print("The number of flights that departure between 14:00 to 17:00 on Wednesday is", num_WED_noon_flights)

# Part B - query 9
num_WED_noon_JFK_flights = flights_data_df[
    (dt >= 1300) & (dt <= 1700) & (flights_data_df['Day'] == 'WED') & (flights_data_df['Dest'] == 'JFK')].count()[
    'flightId']
print("The number of flights that departure between 13:00 to 17:00 on Wednesday and arrived to JFK is",
      num_WED_noon_JFK_flights)

# Part B - query 10
latest_time = dt.max()
print("The latest departure time at the system is", latest_time)


# Part B - Visualizations
# Visualization 1: a pie chart that shows the part of the delayed flights in the total amount (query 4)
pieSlices = (num_delayed_flights, rows - num_delayed_flights)
pieTitles = ('Delayed Flights', 'Flights on time')
pieColors = ('r', 'y')
plt.title('Delayed flights percent')
plt.pie(pieSlices, labels=pieTitles, colors=pieColors, shadow=True, autopct='%1.2f%%')
plt.show()

# Visualization 2: a pie chart that show to percent of JFK flights in all afternoon Wednesday flights (query 9)
wedPieSlices = (num_WED_noon_JFK_flights, num_WED_noon_flights)
wedPieTitles = ('JFK WED FLIGHTS', 'OTHER WED FLIGHTS')
wedPieColors = ('b', 'g')
plt.title('JFK Wednesday afternoon flights percent')
plt.pie(wedPieSlices, labels=wedPieTitles, colors=wedPieColors, autopct='%1.1f%%')
plt.show()

# Visualization 3: A graph that shows the amount of flights for each carrier (query 1)
plt.plot(flights_data_df.groupby('Carrier').count()['flightId'], marker='o', color='g', markeredgecolor='g',
         linestyle='none')
plt.title('Amount of flights for each carrier')
plt.grid()
plt.show()

# Part C question 1
print(flights_data_df.groupby('Delayed').count()['flightId'])

# Part C question 2&3
# The sum of the boolean values in 'Delayed' column shows us the number of the delayed flights,
# because it counts 1 for every delayed flight
print('The sum of Delayed flights column is: {0}'.format(flights_data_df['Delayed'].sum()))

# Part C question 4
# The average of the the binaric values shows us the percent of '1' values in the total number of values,
# i.e the percent of delayed flights in the total number of flights
print('The average of Delayed flights column is: {0}'.format(flights_data_df['Delayed'].mean()))

# Part C question 5
rand_arr = np.random.uniform(0, 1, size=20)
rand_arr[rand_arr < 0.5] = 0
rand_arr[rand_arr >= 0.5] = 1
# The percent of the values bigger from 0.5 is equal to the average of the array
print('The average of the random array is: {0}'.format(rand_arr.mean()))


# Part C question 6
def sort_max_to_min(arr):
    arr.sort()
    arr = arr[::-1]
    return arr


rand_arr = sort_max_to_min(rand_arr)
