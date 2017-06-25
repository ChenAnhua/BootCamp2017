'''

This script is for functions on deriving the time path
The function will return an array with timepath of K and that of wage
and interest rate



'''
import numpy as np
import price_func as pf

def timepath(K_path_update, K_init, K_ss, T, Aval, alphaval, deltaval, nvec, m, type):
    '''
    Please note that row number of K_path_update is K while that of tp is K + m

    '''
    tp = np.zeros([T + m, 4])
    period_path  = np.linspace(1, T + m, num = T + m)
    if type == "linear":
        K_path = np.linspace(K_init, K_ss, num = T)
    if type == "update":
        K_path = K_path_update
    # creating an empty np.array
    tp[: , 0] = period_path
    tp[: -m, 1] = K_path
    tp[-m: , 1] = K_ss
    tp[: , 2] = pf.wage(tp[: , 1], nvec.sum(), Aval, alphaval)
    tp[: , 3] = pf.int_rate(tp[: , 1], nvec.sum(), Aval, alphaval, deltaval)
    return tp
