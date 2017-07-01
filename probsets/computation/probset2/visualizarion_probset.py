'''
This script is for week2 visualization problem sets
'''
# problem 1
# load in the data first
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import gridspec as gs
import scipy as sp
from scipy import special
from matplotlib.colors import LogNorm

anscombe_data = np.load('anscombe.npy')

#plotting
x = np.linspace(0, 20, 1000)
y = 0.5*x + 3
plt.subplot(221)
plt.plot(x, y)
plt.plot(anscombe_data[: , 0], anscombe_data[: , 1], "bo", markersize = 2)

plt.subplot(222)
plt.plot(x, y)
plt.plot(anscombe_data[: , 2], anscombe_data[: , 3], "go", markersize = 2)

plt.subplot(223)
plt.plot(x, y)
plt.plot(anscombe_data[: , 4], anscombe_data[: , 5], "ro", markersize = 2)

plt.subplot(224)
plt.plot(x, y)
plt.plot(anscombe_data[: , 6], anscombe_data[: , 7], "mo", markersize = 2)

plt.show()

# problem 2
# we firstly define the Bernstein basis polynominals
def BSpoly(n, v, x):
    poly = sp.special.binom(n, v)*(x**v)*((1 - x)**(n - v))
    return poly
x_val = np.linspace(0, 1, 100)
y_val = np.zeros_like(x_val)

# design the layout of the plot
grid = gs.GridSpec(4, 4)
grid.update(hspace = 0.5)
fig = plt.figure()
for n in range(4):
    for v in range(n+1):
        # define the location of the subplot
        ax = fig.add_subplot(grid[n , v])
        for i, x in enumerate(x_val):
            y_val[i] = BSpoly(n, v, x)
        ax.plot(x_val, y_val)
        ax.set_title("n= "+str(n)+" v= "+str(v))
        ax.set_xlim([0, 1])
        ax.set_ylim([0,1.5])
        if v != 0:
            ax.tick_params( labelleft = "off")
        if n != 3:
            ax.tick_params(labelbottom = "off")

fig.suptitle("Problem 2")
fig

# problem 3
# loadin data first
mlb_data = np.load("MLB.npy")
height = mlb_data[:, 0]
weight = mlb_data[:, 1]
age    = mlb_data[:, 2]

mlbfig = plt.figure()
plt.scatter(height, weight, c = age)
plt.xlabel("height")
plt.ylabel("weight")
cbar = plt.colorbar()
cbar.set_label("age")

mlbfig

# problem 4
year, magnitude, longitude, latitude = np.load("earthquakes.npy").T

plt.hist(year, bins = range(2000, 2011))
plt.xlabel("year")
plt.ylabel("number of earthquake")
plt.title("Annual number of earthquakes")
plt.show()

freq, bin_edges = np.histogram(magnitude, bins=30)
bin_centers = (bin_edges[:-1] + bin_edges[1:])/2.
plt.plot(bin_centers, freq, 'k-', lw=4)
plt.xlabel("magnitude of the earthquakes")
plt.ylabel("Frequency")
plt.show()

plt.scatter(longitude, latitude, c = magnitude, alpha =0.2)
cbar = plt.colorbar()
cbar.set_label("Magnitude of the earthquakes")
plt.axis("equal")
plt.xlabel("longitude")
plt.ylabel("latitude")
plt.title("loaction of ")
plt.title("loaction and magnitude of earthquake")
plt.show()

# problem 5
x = np.linspace(-1, 3, 500)
X, Y = np.meshgrid(x, x.copy())
Z = (1 - X)**2 + 100*(Y - X**2)**2
prob5fig = plt.figure()
plt.subplot(121)
plt.pcolormesh(X, Y, Z, cmap = "viridis", norm = LogNorm())
plt.colorbar()
plt.plot(1, 1, "ro")

plt.subplot(122)
plt.contour(X, Y, Z, 48, cmap = "viridis", norm = LogNorm())
plt.colorbar()
plt.plot(1, 1, "ro")

plt.tight_layout()
plt.show()

#problem 6
# load in the data first
country_data = np.load("countries.npy")
countries = ["Austria", "Bolivia", "Brazil", "China",
"Finland", "Germany", "Hungary", "India",
"Japan", "North Korea", "Montenegro", "Norway",
"Peru", "South Korea", "Sri Lanka", "Switzerland",
"Turkey", "United Kingdom", "United States", "Vietnam"]

'''
we will plot the four charts as following
1. we will firstly calculate the per-capita GDP and draw a histogram of the
per-capita GDP
 

'''




# end of visualization lab
