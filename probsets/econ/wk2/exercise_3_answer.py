import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from numba import jit
# exercise 1
# using numba to build linear interpolation function
@jit
def numbainterp(x, xp, fp):
    #fp = np.array([y for (x,y) in sorted(zip(xp,fp))])
    order = np.argsort(xp)
    xp = np.array(xp)[order]
    fp = np.array(fp)[order]
    x = np.array(x)
    y = np.zeros_like(x)
    for i in range(len(x)):
        if x[i] > xp[-1]:
            y[i] = fp[-1]
            #y[i] = fp[-1] + (fp[-1] - fp[-2])/(xp[-1] - xp[-2])*(x[i] - xp[-1])
        elif x[i] < xp[0]:
            y[i] = fp[0]
            #y[i] = fp[0] + (fp[1]- fp[0])/(xp[1] - xp[0])*(x[i] - xp[0])
        for j in range(0, (len(xp)-1)):
            if xp[j] == x[i]:
                y[i] = fp[j]
            elif xp[j] < x[i] and xp[j+1]> x[i]:
                y[i] = (fp[j+1]- fp[j])/(xp[j+1]-xp[j])*(x[i] - xp[j]) + fp[j]

    return(y)

def numbainterp_adv(x, xp, fp):
    #fp = np.array([y for (x,y) in sorted(zip(xp,fp))])
    order = np.argsort(xp)
    xp = np.array(xp)[order]
    fp = np.array(fp)[order]
    x = np.array(x)
    y = np.zeros_like(x)
    for i in range(len(x)):
        if x[i] > xp[-1]:
            y[i] = fp[-1]
            #y[i] = fp[-1] + (fp[-1] - fp[-2])/(xp[-1] - xp[-2])*(x[i] - xp[-1])
        elif x[i] < xp[0]:
            y[i] = fp[0]
            #y[i] = fp[0] + (fp[1]- fp[0])/(xp[1] - xp[0])*(x[i] - xp[0])
        for j in range(0, (len(xp)-1)):
            if xp[j] == x[i]:
                y[i] = fp[j]
            elif xp[j] < x[i] and xp[j+1]> x[i]:
                y[i] = (fp[j+1]- fp[j])/(xp[j+1]-xp[j])*(x[i] - xp[j]) + fp[j]

    return(y)

xp = [1, 2, 3]
fp = [3, 2, 0]
x = [0, 1, 1.5, 2.72, 3.14]
np.interp(x, xp, fp)
numbainterp(x, xp, fp)
#%timeit np.interp(x, xp, fp)
#%timeit numbainterp(x, xp, fp)
