'''

This script is for solving the household situation based on the assumed
capital/wage/interest rate time path. It will return an array of errors
between time path capital and capital that satisfies the equilibrium condition

'''
import numpy as np
import scipy.optimize as opt
import price_func as pf
import utility_func as uf
import consumption_func as cf
import aggregatevar_func as af
import timepath_func as tf
import euler_func as ef

def HHsol(timepathval, *args):
    tp = timepathval
    bvec_init_val, T, m, beta, alpha, delta, sigma, A, nvec, bvec_ss, model_choice = args
    # we will firstly create an array to store the calclated savings
    saving_mat = np.zeros([T + m, 3])
    saving_mat[0, 0:-1] = bvec_init_val

    # 1. we firslty need to calculate out the b(3,2)
    '''

    Plesae note that r2 corresponding to the first element of interest rate in tp
    and w2 corresponding to the first element of wage in tp. b21 correspoding to
    saving_mat[0,0]

    '''
    def get_b32(b32, *args):
        r2, r3, b21, w2, w3, beta, sigma, nvec = args
        c2  = cf.consump2(np.array([b21, b32]), r2, w2, nvec)
        c3  = cf.consump3(np.array([b21, b32]), r3, w3, nvec)
        mu2 = uf.mar_util(c2, sigma)
        mu3 = uf.mar_util(c3, sigma)
        error =  mu2 - beta*(1 + r3)*mu3
        return error
    #deriving the b32
    b32_init = 0.1
    b32_args  = (tp[0 , 3], tp[1 , 3], saving_mat[0 , 0], tp[0 , 2], tp[1 , 2], beta, sigma, nvec)
    b32 = opt.root(get_b32, b32_init, args = (b32_args))
    b32 = b32.x
    saving_mat[1 , 1] = b32

    # 2. we then calculate the HH solution within the period
    for i in np.nditer(tp[0: -2, 0].astype("int")):
        w1 = tp[i - 1 , 2]
        w2 = tp[i , 2]
        w3 = tp[i + 1 , 2]
        r2 = tp[i , 3]
        r3 = tp[i + 1, 3]
        ts_args = (w1, w2, w3, r2, r3,  beta, alpha, delta, sigma, A, nvec, model_choice)
        bvec_ts = opt.root(ef.EulerError, bvec_init_val, args = (ts_args))
        saving_mat[i , 0] = bvec_ts.x[0]
        saving_mat[i + 1, 1] = bvec_ts.x[1]

    # 3. we also need to calculate the b2T
    #saving_mat[T-1 , 0] = bvec_ss[0]

    #now we will construct the ts_error
    saving_mat[: , 2] = saving_mat[: , 0] + saving_mat[: , 1]
    return saving_mat
