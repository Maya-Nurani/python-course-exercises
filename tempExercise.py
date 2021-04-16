import numpy as np
from numpy import random

temp_total = np.ones([14,24])
print(temp_total)
print(temp_total.size)

initial_temp = random.randint(20, 40)

temp_change = random.normal(loc=5, scale=2, size=(14, 24))

#np.round(x)
print (initial_temp)
#temp_total[0, 0] = initial_temp + temp_change[0,0]

#print(temp_total[0, 0])
print(temp_change[0,[0]]+initial_temp)
print(temp_change[0,[1]]+temp_change[0,[0]]+initial_temp)
#print(temp_change)

