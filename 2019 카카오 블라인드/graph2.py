"""
Description: In this script, I plot the benchmark result of lambda compared
to itemgetter in the operator package. We sort a list of tuple (which has two
elements) to benchmark. The list element number ranges from 100 to 1000000.
"""
# import numpy as np
import matplotlib
import matplotlib.pyplot as plt

colors = ["#e6194b",
          "#3cb44b"]

# the number of tuple in list
N = [100, 1000, 10000, 100000, 1000000]

# time for lambda
t1 = [8.19, 81.4, 855, 14600, 172000]

# time for itemgetter
t2 = [5.09, 47, 498, 10100, 131000]

fig, ax = plt.subplots(figsize=(10, 6))
ax.semilogx(N, t1, marker='.',  label="lambda")
ax.semilogx(N, t2, marker='.', label="itemgetter")

ax.set_xlabel("The number of elements in list")
ax.set_ylabel("Time to sort the list " + r"(in $\mu s$)")

ax.set_xticks(N)
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.legend()

# use the following method to turn off minor ticks
ax.tick_params(axis='x', which='minor', bottom='off')
# ax.minorticks_off()  # or use minorticks_off method
# turn grid on
ax.grid(linestyle='--')

plt.savefig("test.jpg")
plt.show()