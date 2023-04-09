import numpy as np
my = np.random.randint(0, 100, size=100)          ## Your code here
my_array = my / 100
my_array[my_array.argmax()] = 1
my_array[my_array.argmin()] = 0
print(np.max(my_array), np.min(my_array))
print(my_array)
