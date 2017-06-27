'''

This script is for homework on plotting introduction

'''
import numpy as np
from matplotlib import pyplot as plt


# Prob 1
def prob1_preli(n):
    n_mat = np.random.normal(0, 1, n**2).reshape((n, n))
    n_mean= n_mat.mean( axis = 1)
    n_var = n_mean.var()
    return n_var

def prob1_plot(my_list):
    my_list = np.array(my_list)
    vfunc   = np.vectorize(prob1_preli)
    result_list = vfunc(my_list)
    # plotting the graph
    plt.plot(result_list)
    plt.show()
    print(result_list)
    return result_list

# prob1 result
prob1_plot([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000])

# Prob2
def prob2(boundary):
    x  = np.linspace(-boundary, boundary, 1000)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.arctan(x)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.show()
#Porb2 results
prob2(2*np.pi)

# prob 3
def prob3(xrange, yrange, style, lsize, msize, resol):
    xlb, xub = xrange
    ylb, yub = yrange
    x = np.linspace(xlb, xub, resol)
    y = 1/(x - 1)
    # insert nan at discontinuing point
    pos = np.where(abs(x - 1) <= 0.05)[0]+1
    x = np.insert(x, pos, np.nan)
    y = np.insert(y, pos, np.nan)
    # plotting
    plt.plot(x, y, style, linewidth = lsize, markersize = msize)
    plt.ylim(ylb, yub)
    plt.show()

#prob 3 results
prob3((-2, 6), (-6, 6), "m--", 3, 1, 1000)

#prob 4
def prob4(xrange, yrange, axislim, style, lsize, msize, title, titlesize, suptitle, suptitlesize, resol):
    xlb, xub = xrange
    ylb, yub = yrange
    style1, style2, style3, style4 = style
    lsize1, lsize2, lsize3, lsize4 = lsize
    msize1, msize2, msize3, msize4 = msize
    title1, title2, title3, title4 = title

    x = np.linspace(xlb, xub, resol)

    plt.subplot(221)
    plt.plot(x, np.sin(x), style1, linewidth = lsize1, markersize = msize1)
    plt.title(title1, fontsize = titlesize)
    plt.axis(axislim)

    plt.subplot(222)
    plt.plot(x, np.sin(2*x), style2, linewidth = lsize2, markersize = msize2)
    plt.title(title2, fontsize = titlesize)
    plt.axis(axislim)

    plt.subplot(223)
    plt.plot(x, 2*np.sin(x), style3, linewidth = lsize3, markersize = msize3)
    plt.title(title3, fontsize = titlesize)
    plt.axis(axislim)

    plt.subplot(224)
    plt.plot(x, 2*np.sin(2*x), style4, linewidth = lsize4, markersize = msize4)
    plt.title(title4, fontsize = titlesize)
    plt.axis(axislim)

    plt.suptitle(suptitle)


    plt.show()

#prob4 results
xrange = (-1, 3*np.pi)
yrange = (-3, 3)
axislim = (0, 2*np.pi, -2, 2)
style = ("g-", "r--", "b--", "m:")
lsize = (2,2,2,2)
msize = (1,1,1,1)
title = ("subplot1", "subplot2", "subplot3", "subplot4")
titlesize = 7
suptitle = "Problem 4"
suptitlesize = 10
resol = 1000
prob4(xrange, yrange, axislim, style, lsize, msize, title, titlesize, suptitle, suptitlesize, resol)

#prob 5
# loading the data first
def prob5(filename):
    fars_data = np.load(filename)
    plt.subplot(121)
    x = fars_data[:, 1]
    y = fars_data[:, 2]
    plt.plot(x, y, "k,")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis("equal")

    plt.subplot(122)
    plt.hist(fars_data[: , 0], bins = np.arange(-0.5, 24.5))
    plt.xlim(-1, 24)
    plt.xlabel("car crash hour", fontsize = 10)

    plt.show()

#prob5 results
prob5("FARS.npy")

# prob6
def prob6(bounds, resol):
    xlb, xub, ylb, yub = bounds
    x = np.linspace(xlb, xub, resol)
    y = np.linspace(ylb, yub, resol)
    X, Y = np.meshgrid(x, y)
    Z = (np.sin(X) * np.sin(Y))/(X*Y)

    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap = "viridis")
    plt.colorbar()
    plt.axis([xlb, xub, ylb, yub])

    plt.subplot(122)
    plt.contour(X, Y, Z, 10, cmap="Spectral")
    plt.colorbar()
    plt.axis([xlb, xub, ylb, yub])


    plt.show()
prob6((-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi), 1000)






# end of plottingintro probset
