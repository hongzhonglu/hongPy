# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-

# good resource from https://www.python-graph-gallery.com/


# Import packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def my_tan(x):
    return np.tan(x)

# line
x = np.linspace(-1.3, 1.3)
y_tan = my_tan(x)

plt.plot(x, y_tan, label="tan")
plt.legend()
plt.xlabel("x", size=14)
plt.ylabel("x", size=14)
plt.grid()
plt.show()


#hist
np.random.seed(10 ** 7)
n_bins = 20
x = np.random.randn(10000, 3)
colors = ['green', 'blue', 'lime']
plt.hist(x, n_bins, density=True,
         histtype='bar',
         color=colors,
         label=colors)

plt.legend(prop={'size': 10})
plt.title('matplotlib.pyplot.hist() function Example\n\n',
          fontweight="bold")
plt.show()


#bar
# Make a random dataset:
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
# Create bars
plt.bar(y_pos, height)
# Create names on the x-axis
plt.xticks(y_pos, bars)
# Show graphic
plt.show()

# heatmap
# Create a dataset
df = pd.DataFrame(np.random.random((10, 10)), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])

# plot using a color palette
sns.heatmap(df, cmap="YlGnBu")
plt.show()

sns.heatmap(df, cmap="Blues")
plt.show()

sns.heatmap(df, cmap="BuPu")
plt.show()

sns.heatmap(df, cmap="Greens")
plt.show()

# second example
# Data set
url = 'https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/mtcars.csv'
df = pd.read_csv(url)
df = df.set_index('model')
# Change color palette
sns.clustermap(df, metric="euclidean", standard_scale=1, method="ward", cmap="mako")
plt.show()
sns.clustermap(df, metric="euclidean", standard_scale=1, method="ward", cmap="viridis")
plt.show()
sns.clustermap(df, metric="euclidean", standard_scale=1, method="ward", cmap="Blues")
plt.show()

