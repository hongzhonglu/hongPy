# -*- coding: utf-8 -*-
# -*- python 3 -*-
# -*- hongzhong Lu -*-

# good resource from https://www.python-graph-gallery.com/


# Import packages
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



# some general tips
# save figure
plt.savefig(title0, bbox_inches='tight')

# adjust the title position
plt.title(xx, y=1.01)









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


# thir example
# mutiple line
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.integrate as integrate
dx=0.01
dt=0.01
size_x=1
size_t=0.5
nx=np.int_(size_x/dx+1)
nt=np.int_(size_t/dt+1)

diffusivity=1
conc_t0=np.zeros(nx)
conc_x0=1
conc_x1=0

def diffusion_eq(t,y):
    y_constrainted=np.r_[conc_x0,y[1:-1],conc_x1]
    return diffusivity*(np.gradient(np.gradient(y_constrainted,dx),dx))

teval=np.r_[0:nt:1]*dt
sol=integrate.solve_ivp(diffusion_eq,[0,size_t],conc_t0,t_eval=teval)

plt.plot(sol.t,sol.y[np.int(0.1/dx)],marker='.',label='x=0.1')
plt.plot(sol.t,sol.y[np.int((nx-1)/2)],marker='.',label='x=0.5')
plt.plot(sol.t,sol.y[-1],marker='.',label='x=1')
plt.xlabel('Time t')
plt.ylabel('Concentration c')
plt.legend(loc='upper right')

xeval=np.r_[0:nx:1]*dx
plt.plot(xeval,sol.y[:,np.int(0.1/dt)],marker='.',label='t=0.1')
plt.plot(xeval,sol.y[:,np.int((nt-1)/2)],marker='.',label='t=0.25')
plt.plot(xeval,sol.y[:,-1],marker='.',label='t=0.5')
plt.xlabel('Position x')
plt.ylabel('Concentration c')
plt.legend(loc='lower left')

# 3D plot
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
plot = Axes3D(fig)
plot_array_t,plot_array_x=np.meshgrid(sol.t,xeval)
plot.plot_surface(plot_array_t,plot_array_x,sol.y,cmap=mpl.cm.jet)
plot.view_init(20, 60)
plot.set_xlabel('t')
plot.set_ylabel('x')
plot.set_zlabel('Concentration');


plot = plt.contourf(plot_array_t,plot_array_x,sol.y,cmap=mpl.cm.jet,levels=50)
plt.colorbar(plot)
plt.title('Concentration')
plt.xlabel('t')
plt.ylabel('x')




# add confidence interval
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# create random data
np.random.seed(0)
x = np.random.randint(0, 10, 10)
y = x + np.random.normal(0, 1, 10)

# create regression plot
ax = sns.regplot(x, y, ci=80) # 80% confidence interval is plotted
