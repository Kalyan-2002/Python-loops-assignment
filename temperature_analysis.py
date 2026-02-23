#task 1
import numpy as np
temps_celsius = np.array([22,25,28,24,26])
temp_fahrenheit = temps_celsius * 1.8 + 32

print(f"temperature in celsius: {temps_celsius}")
print(f"temperature in fahrenheit: {temp_fahrenheit}")

average_fahrenheit = np.mean(temp_fahrenheit)
print(f"average fahrenheit: {average_fahrenheit}")

#task 2

arr = np.array([85,90,78,92,88,76,95,82,89,91,87,84])

print(f"Shape: {arr.shape}")
print(f"Total elements: {len(arr)}")
highest_score = np.max(arr)
lowest_score = np.min(arr)
print(f"Highest score: {highest_score}")
print(f"Lowest score: {lowest_score}")
print(f"Range of scores: {highest_score - lowest_score}")



#task 3

import numpy as np
import time

python_list = list(__builtins__.range(1, 50001))
numpy_array = np.arange(1, 50001)
#python list
start = time.time()
sum1 = __builtins__.sum(python_list)
python_time = time.time() - start
 #numpy
start = time.time()
sum2 = np.sum(numpy_array)
numpy_time =time.time() - start

print(f"Numpy sum: {sum1}")
print(f"Python sum: {sum2}")
print(f"Numpy Time: {numpy_time: .4f}")
print(f"Python Time: {python_time: .4f}")
print(f"Numpy is {python_time/numpy_time: .1f} faster")