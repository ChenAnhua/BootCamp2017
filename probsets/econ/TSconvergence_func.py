'''

This script is for function to test the convergence TPI method

function input:

tp_init                          : initial timepath derived
xival                            : time path updating parameter
tolval                           : tolerance to inidcate the convergence of TPI method
timepathval                      : the given timepath of K
bvec_init_val                    : initial savings guess
T                                : number of periods included in the model to calculate the time path
m                                : number of periods past the period when steady state is reached
beta                             : impatiency discount factor in one period
alpha                            : share of capital in income
delta                            : depreciation rate in one period
sigma                            : the risk aversion of CRRA utility function
A                                : TFP
nvec                             : vector of labor supply
bvec_ss                          : vector of steady state savings
K_ss                             : steady state capital stock
model_choice                     : whether it's steady state (SS) or not

function output:
(tp, saving_HH)                  : time path tuple of aggregate variables



'''
import numpy as np
import scipy.optimize as opt
import price_func as pf
import utility_func as uf
import consumption_func as cf
import aggregatevar_func as af
import timepath_func as tf
import euler_func as ef
import HHsolution_func as hf

def tpi(tp_init, xival, tolval, *args):
    bvec_init_val, T, m, beta, alpha, delta, sigma, A, nvec, bvec_ss, K_ss, model_choice = args
    '''
    We will firstly derive the epsilon between the initial K time path and caluclated K path (K prime)
    and decide whether it already statisfies the tolerance condition

    '''
    saving_HH_init  = hf.HHsol(tp_init, bvec_init_val, T, m, beta, alpha, delta, sigma, A, nvec, bvec_ss ,"TS")
    epsilon_init = sum(((tp_init[: -m, 1] - saving_HH_init[: -m, 2])/tp_init[: -m, 1])**2)
    if epsilon_init > tolval:
        '''
        if the initial epsilon is larger than the tolerance
        we update the time path and calculated time path and recalculate the epsilon

        '''
        tp = tp_init
        saving_HH = saving_HH_init
        epsilon = epsilon_init
        iter_num = 0
        while epsilon > tolval:
            update = xival*saving_HH[: -m, 2] + (1 - xival)*tp[: -m, 1]
            tp = tf.timepath(update, 0, K_ss, T, A, alpha, delta, nvec, m, "update")
            saving_HH = hf.HHsol(tp, bvec_init_val, T, m, beta, alpha, delta, sigma, A, nvec, bvec_ss ,"TS")
            epsilon = sum(((tp[: -m, 1] - saving_HH[: -m, 2])/tp[: -m, 1])**2)
            iter_num = iter_num + 1
            print("iteration: ", iter_num, "       epsilon: ", epsilon)

        result = (tp, saving_HH)
    else:
        result =  (tp_init, saving_HH_init)
    return result
