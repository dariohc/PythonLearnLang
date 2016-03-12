__author__ = 'Dario Hermida'
import numpy as np
import matplotlib.pyplot as plt

time_limit = 10000
my_function = []
my_difference = []

# create time axis for the plot
time = np.arange(0, time_limit, 1)

for x in range(0, time_limit):
    my_function.append((2 * (x**2) - 3*x + 7) / ((x**2) + 47*x + 1))
    my_difference.append(2 - my_function[x])

plt.plot(my_function, 'g--', my_difference, 'r--')
plt.show()