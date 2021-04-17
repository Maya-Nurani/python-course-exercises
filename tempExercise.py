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
temp_total = temp_change
print(temp_total)
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
average_per_day(temp_total)


#### Part B exercise 2 (max) ####
def max_temp_per_day(temp_change):
    day_number = 1
    for i in temp_total:
        print("The maximum temperature change during day", day_number, " is ", np.max(i))
        day_number += 1


print("max def:")
max_temp_per_day(temp_change)


#### Part B exercise 3 (min) ####
def min_temp_per_day(temp_change):
    day_number = 1
    for i in temp_total:
        print("The minimum temperature change during day", day_number, " is ", np.min(i))
        day_number += 1


print("min def:")
min_temp_per_day(temp_change)


#### Part B exercise 4 (equal temp per hour) ####
def check_hourly_temp_equal(temp_change):
    for hour in range(0, 24):
        column = temp_change[:, hour]
        print(np.round(column))  ### TODO: decide if round and if not - remove this row
        result = np.all(column == column[0])
        if result:
            print("Pattern found at hour", hour)
        else:
            print("All temp changes at hour", hour+1, "are not the same")


check_hourly_temp_equal(temp_change)


### Part C-1
def convertTo1d(temp_change, temp_total):
    new_temp_change = np.ndarray.flatten(temp_change)
    new_temp_total = np.ndarray.flatten(temp_total)
    return new_temp_change, new_temp_total


### convertTo1d run
temp_change, temp_total = convertTo1d(temp_change, temp_total)


### Check for C-1
print(temp_change, temp_total)
print(temp_total.shape)


#### Draft ####

# np.round(x)
# temp_total[0, 0] = initial_temp + temp_change[0,0]

# print(temp_total[0, 0])
# print(temp_change[0,[0]]+initial_temp)
# print(temp_change[0,[1]]+temp_change[0,[0]]+initial_temp)
# print(temp_change)

# for test
arr = np.arange(100)
arr.shape = (10, 10)
# print(arr)
# print(arr[ : ,0])
