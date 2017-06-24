# -*- coding: utf-8 -*-
'''
This script is modeling the steady state 3-period overlapping generation model

'''
#import pacakges
import numpy as np
import scipy.optimize as opt
import price_func as pf
import utility_func as uf
import consumption_func as cf
import aggregatevar_func as af
import timepath_func as tf
import euler_func as ef
import HHsolution_func as hf
# Initialization
'''
yrs_live    : years of an agent's life expectancy
S           : number of periods in an agent's life
alpha       : share of capital in income
beta_annual : annual impatiency discount factor
beta        : impatiency discount factor in one period
nvac        : labor supply of each period of an agent's life
A           : TFP
delta_annual: annual depreciation rate
delta       : depreciation rate in one period
sigma       : the risk aversion of CRRA utility function


'''
# initialization for steady state model
yrs_live    = 60
S           = 3
alpha       = 0.35
beta_annual = 0.96
beta        = beta_annual**(yrs_live/S) #0.55
nvec        = np.array([1.0, 1.0, 0.2])
A           = 1.0
delta_annual= 0.05
delta       = 1-(1-delta_annual)**(yrs_live/S)
sigma       = 3
bvec_init   = np.array([0.1, 0.1])


# initialization for transitional state
T           = 20
K_init      = bvec_init.sum()



# derive the steady state equilibrium
ss_args = (1, 1, 1, 1, 1,  beta, alpha, delta, sigma, A, nvec, "SS")
report_ss = opt.root(ef.EulerError, bvec_init, args = (ss_args))
print(report_ss)
bvec_ss = report_ss.x
print("Steady State savings: ", bvec_ss)
K_ss = af.capital(bvec_ss)
L_ss = af.labor(nvec)
w_ss = pf.wage_ss(K_ss, L_ss, A, alpha)
r_ss = pf.int_rate_ss(K_ss, L_ss, A, alpha, delta)
c1_ss = cf.consump1(bvec_ss, w_ss, nvec)
c2_ss = cf.consump2(bvec_ss, r_ss, w_ss, nvec)
c3_ss = cf.consump3(bvec_ss, r_ss, w_ss, nvec)
print("Steady state period 1 consumption: ", c1_ss)
print("Steady state period 2 consumption: ", c2_ss)
print("Steady state period 3 consumption: ", c3_ss)
print("Steady state wage: ", w_ss)
print("Steady state interest rate: ", r_ss)
print("Steady state capital: ", K_ss)
print("Steady state labor: ", L_ss)

# derive the transitional state equlibrium
#timepath = tf.timepath(K_init, K_ss, T, A, alpha, delta, nvec, "linear")
#saving_HH  = hf.HHsol(timepath, bvec_init, T, beta, alpha, delta, sigma, A, nvec, bvec_ss ,"TS")




# derive the transitional state equilibrium
