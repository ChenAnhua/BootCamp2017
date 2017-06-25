# -*- coding: utf-8 -*-
'''
This script is to derive the results of steady state/transitional state equilibrium
of a 3 period OG model. The general structure of the file is as following:
1) We import packages and functions first
2) We set the initialization of steady state and transitional state parameters
3) We derive results of steady state equilibrium
4) We then derive results of transitional state equilibrium

'''
#import pacakges
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
import price_func as pf
import utility_func as uf
import consumption_func as cf
import aggregatevar_func as af
import timepath_func as tf
import euler_func as ef
import HHsolution_func as hf
import TSconvergence_func as tcf


# Initialization
'''

Steady state parameters:

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
bvec_init   : initial savings for equilibrium calculation

transitional state parameters:
T           : number of periods included in the model to calculate the time path
m           : number of periods past the period when steady state is reached
K_init      : initial value of aggregate capital stock
tol         : tolerance for determining the TPI convergence
xi          : time path updating parameters

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
T           = 40
m           = 5
K_init      = bvec_init.sum()
tol         = 1e-9
xi          = 0.9


# derive the steady state equilibrium
'''

For details of EulerError function , please refer to the euler_func.py file

'''
ss_args = (1, 1, 1, 1, 1,  beta, alpha, delta, sigma, A, nvec, "SS")
report_ss = opt.root(ef.EulerError, bvec_init, args = (ss_args))
print(report_ss)
bvec_ss = report_ss.x
print("Steady State savings: ", bvec_ss)
K_ss  = af.capital(bvec_ss)
L_ss  = af.labor(nvec)
w_ss  = pf.wage(K_ss, L_ss, A, alpha)
r_ss  = pf.int_rate(K_ss, L_ss, A, alpha, delta)
c1_ss = cf.consump1(bvec_ss, w_ss, nvec)
c2_ss = cf.consump2(bvec_ss, r_ss, w_ss, nvec)
c3_ss = cf.consump3(bvec_ss, r_ss, w_ss, nvec)
print("Steady state period 1 consumption: ", c1_ss)
print("Steady state period 2 consumption: ", c2_ss)
print("Steady state period 3 consumption: ", c3_ss)
print("Steady state wage: ", w_ss)
print("Steady state compound interest rate: ", r_ss)
print("Steady state capital: ", K_ss)
print("Steady state labor: ", L_ss)

# derive the transitional state equlibrium
# we update the bvec_init and K_init first as in question 3
bvec_init = bvec_ss*np.array([0.8 , 1.1])
K_init    = bvec_init.sum()
# we firstly derive the initial time path
timepath_init = tf.timepath(0, K_init, K_ss, T, A, alpha, delta, nvec, m, "linear")
# then we derive the converged time path
tpi_result = tcf.tpi(timepath_init, xi, tol, bvec_init, T, m, beta, alpha, delta, sigma, A, nvec, bvec_ss, K_ss, "TS")
K_path = tpi_result[0][:, [0 , 1]]
w_path = tpi_result[0][:, [0 , 2]]
r_path = tpi_result[0][:, [0 , 3]]

# plotting the Aggreate capital
K_fig = plt.figure()
plt.plot(K_path[: , 0], K_path[: , 1])
plt.xlabel('periods')
plt.ylabel('aggregate capital stock')
plt.title('Time path of aggregate capital stock')
plt.show()
# also return the first period when steady state is reached (1e-4)
