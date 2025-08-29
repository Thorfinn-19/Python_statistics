import numpy as np
import random as rd
import matplotlib.pyplot as plt
x_normal = []
x_random = []
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            x_normal.append(i + j + k)
for i in range(216):
    r1 = rd.randint(1, 6)
    r2 = rd.randint(1, 6)
    r3 = rd.randint(1, 6)
    x_random.append(r1 + r2 + r3)
mean_normal = np.mean(x_normal)
mean_random = np.mean(x_random)
print(f"mean normal: {mean_normal}, mean random: {mean_random}")
median_normal = np.median(x_normal)
median_random = np.median(x_random)
print(f"median normal: {median_normal}, median_random: {median_random}")
std_normal = np.std(x_normal)
std_random = np.std(x_random)
print(f"std deviation normal: {std_normal}, std deviation random: {std_random}")
plt.hist(x_normal, bins=16, edgecolor='black')
plt.show()
plt.hist(x_random, bins=16, edgecolor='black')
plt.show()
