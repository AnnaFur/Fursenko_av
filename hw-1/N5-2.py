import numpy as np
my_array = np.random.randint(0, 50, size= (5,6))
selected_column = my_array[:,np.argmax(my_array.max(axis=0))]
print('Shape: ',my_array.shape)
print('Array')
print(my_array)#print(selected_column)