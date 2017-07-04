'''

This script is for functions on deriving and updating the time path
The function will return an array with timepath of K and that of wage
and interest rate

funciton input:

K_path_update           : if type is "update", this is the updated K_path within the first T periods
K_init                  : initial guess of K to calculate the initial path
K_ss                    : the steady state value of aggregate capital stock
T                       : number of periods included in the model to calculate the time path
Aval                    : TFP value
alphaval                : share of capital in income
deltaval                : depreciation rate within a period
nvec                    : vector of labor supply
m                       : number of periods past the period when steady state is reached
type                    : either "linear" or "update"

function output:

tp                      : time path array, including periods, K, wage and interest rate

Please note that row number of K_path_update is T while that of tp is K + m

'''
import numpy as np
import price_func as pf

def timepath(K_path_update, K_init, K_ss, T, Aval, alphaval, deltaval, nvec, m, type):
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
    '''
    We call in the wage and interest rate function to derive paths of w and r
    based on K path
    '''
    tp[: , 2] = pf.wage(tp[: , 1], nvec.sum(), Aval, alphaval)
    tp[: , 3] = pf.int_rate(tp[: , 1], nvec.sum(), Aval, alphaval, deltaval)
    return tp
