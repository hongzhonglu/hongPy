# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-


# Import packages
import numpy as np
import matplotlib.pyplot as plt

def my_tan(x):
    return np.tan(x)

x = np.linspace(-1.3, 1.3)
y_tan = my_tan(x)

plt.plot(x, y_tan, label="tan")
plt.legend()
plt.xlabel("x", size=14)
plt.ylabel("x", size=14)
plt.grid()
plt.show()


