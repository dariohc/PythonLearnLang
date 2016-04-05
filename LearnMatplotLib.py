__author__ = 'Dario Hermida'
import matplotlib.pyplot as plt
import math


# creation of my input plot 3 manual regions
my_function = []
my_axis = []
value = 0.0
index = 0.01
index_step = 0.1
T_cero = 0.2
# range creation
limit_1_low = 0.0
limit_1_up = 1/(5*T_cero)
limit_2_up = 1/T_cero
limit_3_up = 33.0

while index < limit_1_up:
    value = index*5*T_cero
    my_function.append(value)
    my_axis.append(math.log10(index/0.1)+1.1)
    index += index_step

while index < limit_2_up:
    value = 1
    my_function.append(value)
    my_axis.append(math.log10(index/0.1)+1.1)
    index += index_step

while index < limit_3_up:
    value = 0.6/(index*T_cero) + 0.4
    my_function.append(value)
    my_axis.append(math.log10(index/0.1)+1.1)
    index += index_step

# plt.plot(my_function, 'bo')
# plt.ylabel('some numbers')
# plt.show()

# second function
my_function2 = []
value = 0.0
index = 0
index_step = 0.1
T_cero = 0.2
# range creation
limit_1_low = 0.0
limit_1_up = 1.3
limit_2_up = 8.3
limit_3_up = 33.0

while index < limit_1_up:
    value = (index/1.3)**0.9
    my_function2.append(value)
    index += index_step

while index < limit_2_up:
    value = 1
    my_function2.append(value)
    index += index_step

while index < limit_3_up:
    value = (8.3/index)**0.67
    my_function2.append(value)
    index += index_step
#create your x-axis
plt.figure(1)
plt.subplot(211)
plt.plot(my_axis, my_function, 'b-')
plt.ylabel('IEEE 693 standard Sa')

plt.subplot(212)
plt.plot(my_axis, my_function2, 'y-')
plt.ylabel('ICBO ES standard Sa')
plt.show()
