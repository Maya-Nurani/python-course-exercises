import numpy as np
from numpy import random

#### PartA exercise1 ####
initial_temp = random.randint(20, 41)
print (initial_temp)


#### PartA exercise2 ####
temp_change = random.normal(loc=5, scale=2, size=(14, 24))
print(temp_change)


#### PartA exercise3 ####
temp_total = temp_change
print(temp_total)
temp_total[0,0]=temp_total[0,0]+initial_temp
temp_total = np.cumsum(temp_total)
print(temp_total)

#### Part B exercise 4 ####
def check_hourly_temp_equal(temp_change):
    for i in range(0,10):
        column = temp_change[ : ,i]
        result = np.all(column == column[0])
        if result:
            print('All Values in column are same / equal')
        else:
            print('All Values in column are not same')



#### Draft ####

temp_total = np.ones([14,24])
print(temp_total)
print(temp_total.size)

#np.round(x)
#temp_total[0, 0] = initial_temp + temp_change[0,0]

#print(temp_total[0, 0])
print(temp_change[0,[0]]+initial_temp)
print(temp_change[0,[1]]+temp_change[0,[0]]+initial_temp)
#print(temp_change)

## for test
arr = np.arange(100)
arr.shape = (10,10)
print(arr)
print(arr[ : ,0])
check_hourly_temp_equal(arr)
