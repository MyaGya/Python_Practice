
import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
import math
from operator import itemgetter

a = list(range(1000))
b = list(range(1000))
random.shuffle(a)
random.shuffle(b)
c = list(zip(a, b))

data_lambda = []
data_itemgetter = []
result1 = []
result2 = []
for i in range(10):
    for i in range(10):
        start = timeit.default_timer()
        c.sort(key=lambda x: x[1])
        end = timeit.default_timer()
        data_lambda.append(end-start)
        random.shuffle(c)
    for i in range(10):
        start = timeit.default_timer()
        c.sort(key=itemgetter(1))
        end = timeit.default_timer()
        data_itemgetter.append(end-start)
        random.shuffle(c)
    result1.append(sum(data_lambda) / len(data_lambda))
    result2.append(sum(data_itemgetter) / len(data_itemgetter))

plt.title("rambda VS itemgetter")
plt.plot(range(1,11),result1, 'g', label = "rambda")
plt.plot(range(1,11),result2, 'r', label = "itemgetter")
plt.xlabel("Roof")
plt.ylabel("Time")
plt.grid(True)
plt.legend()
plt.show()