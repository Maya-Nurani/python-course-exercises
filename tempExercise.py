import numpy as np
from numpy import random
import matplotlib.pyplot as plt

#### PartA exercise1 ####
initial_temp = random.randint(20, 41)
print(initial_temp)

#### PartA exercise2 ####
temp_change = random.normal(loc=5, scale=2, size=(14, 24))
print(temp_change)

#### PartA exercise3 ####
temp_total = np.copy(temp_change)  # Using copy in order to keep temp_change ad is withput editing both arrays
temp_total[0, 0] = temp_total[0, 0] + initial_temp
temp_total = np.cumsum(temp_total)
temp_total = np.reshape(temp_total, (14, 24))
print("print total after sum")
print(temp_total)
print("Print shape", temp_total.shape)


#### Part B exercise 1 (average) ####
def average_per_day(temp_total):
    day_number = 1
    for i in temp_total:
        print("The average temperature of day", day_number, " is ", np.average(i))
        day_number += 1


print("average def:")
# average_per_day(temp_total)


#### Part B exercise 2 (max) ####
def max_temp_per_day(temp_change):
    day_number = 1
    for i in temp_total:
        print("The maximum temperature change during day", day_number, " is ", np.max(i))
        day_number += 1


print("max def:")
# max_temp_per_day(temp_change)


#### Part B exercise 3 (min) ####
def min_temp_per_day(temp_change):
    day_number = 1
    for i in temp_total:
        print("The minimum temperature change during day", day_number, " is ", np.min(i))
        day_number += 1


print("min def:")
# min_temp_per_day(temp_change)


#### Part B exercise 4 (equal temp per hour) ####
def check_hourly_temp_equal(temp_change):
    for hour in range(0, 24):
        column = temp_change[:, hour]
        print(np.round(column))  ### TODO: decide if round and if not - remove this row
        result = np.all(column == column[0])
        if result:
            print("Pattern found at hour", hour)
        else:
            print("All temp changes at hour", hour + 1, "are not the same")


check_hourly_temp_equal(temp_change)


#### Part B exercise 5 (every 3 hours) ####
def sum_three_hours_change(temp_change):
    is_bigger = False
    index = 0
    arr = new_temp_change = np.ndarray.flatten(temp_change)
    print(temp_change)

    while (is_bigger == False and (index <= arr.size - 3)):
        sum = np.sum(arr[index:index + 3])
        index += 1
        if sum > 8:
            print("Wow, it is really hot in here.")
            # TODO: remove the next print?
            print("Sum is", sum, "index from:", index - 1)
            is_bigger = True


print("every 3 hours def:")
sum_three_hours_change(temp_change)

#### Part B exercise 6 (every 3 hours) ####


### Part C exercise 1
def convertTo1d(temp_change, temp_total):
    new_temp_change = np.ndarray.flatten(temp_change)
    new_temp_total = np.ndarray.flatten(temp_total)
    return new_temp_change, new_temp_total


### convertTo1d run
temp_change, temp_total = convertTo1d(temp_change, temp_total)


### Part C exercise 2
def totalTempByHour():
    y_axis = temp_total[0:24]
    x_axis = np.arange(24)
    plt.plot(x_axis, y_axis)
    plt.xlabel("Hour")
    plt.ylabel("Temperature")
    plt.grid()
    plt.show()

totalTempByHour()


### Part C exercise 3
def changesHistogram():
    plt.hist(temp_change, bins=8)
    plt.grid()
    plt.xlabel("Temperature change histogram")
    plt.show()


### Part C exercise 4
def dailyAverage():
    new_temp_total = temp_total.reshape(14, 24)
    avg_total = new_temp_total.mean(1)
    y_axis = np.ndarray.flatten(avg_total)
    x_axis = np.arange(1,15)
    plt.plot(x_axis, y_axis)
    plt.xlabel("Day")
    plt.ylabel("Temperature Average")
    plt.grid()
    plt.show()


changesHistogram()
dailyAverage()

### Check for C-1
print(temp_change, temp_total)
print(temp_total.shape)

#### Draft ####

# np.round(x)

# for test
arr = np.arange(100)
arr.shape = (10, 10)
# print(arr)
# print(arr[ : ,0])
