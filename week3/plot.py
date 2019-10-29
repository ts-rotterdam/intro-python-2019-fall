import matplotlib.pyplot as plt
import numpy as np

y = [2, 3, 1, 4]
x = range(len(y))

p = plt.bar(x, y)
p = plt.xticks(x, x)
p = plt.yticks([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
plt.show(p)
