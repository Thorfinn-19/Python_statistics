import numpy as np
import random as rd
x = []
for i in range(100):
    r = rd.randint(1,6)
    x.append(r)
print(f"x: {x}")
mean = np.mean(x)
print(f"mean: {mean}")
