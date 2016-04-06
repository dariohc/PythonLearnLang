__author__ = 'Dario Hermida'
import matplotlib.pyplot as plt
import numpy as np

pressure_axis = [x/100.0 for x in range(0, 250, 25)]
print(pressure_axis)
horn_25 = [0.5, 0.8, 1.1, 1.3, 1.4, 1.55, 1.65, 1.8, 1.95, 2.2]

plt.figure(1)
plt.subplot(211)
plt.plot(pressure_axis, horn_25)
plt.subplot(212)
plt.plot(pressure_axis, horn_25)

plt.show()