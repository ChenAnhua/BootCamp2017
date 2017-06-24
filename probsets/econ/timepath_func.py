'''

This script is for functions on deriving the time path
The function will return an array with timepath of K and that of wage
and interest rate

'''
import numpy as np
import price_func as pf

def timepath(K_init, K_ss, T, Aval, alphaval, deltaval, nvec, type):
    tp = np.zeros([T, 4])
    if type == "linear":
        period_path  = np.linspace(1, T, num = T)
        K_path = np.linspace(K_init, K_ss, num = T)
    # creating an empty np.array
    tp[: , 0] = period_path
    tp[: , 1] = K_path
    tp[: , 2] = pf.wage_ss(tp[: , 1], nvec.sum(), Aval, alphaval)
    tp[: , 3] = pf.int_rate_ss(tp[: , 1], nvec.sum(), Aval, alphaval, deltaval)
    return tp
