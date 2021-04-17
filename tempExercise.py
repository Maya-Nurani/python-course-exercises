import numpy as np
from numpy import random

#### PartA exercise1 ####
initial_temp = random.randint(20, 40)
print (initial_temp)


#### PartA exercise2 ####
temp_change = random.normal(loc=5, scale=2, size=(14, 24))


#### PartA exercise3 ####

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
