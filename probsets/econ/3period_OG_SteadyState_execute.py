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

# Derive the eror of Euler equation in steady state equilibrium
def EquiError(bvec, *args):
    b2val, b3val = bvec
    w1, w2, w3, r2, r3, beta, alpha, delta, sigma, A, nvec, model_choice = args
    K = af.capital(bvec)
    L = af.capital(nvec)
    if (model_choice == "SS"):
        w = pf.wage_ss(K, L, A, alpha)
        w1= w2 = w3 = w
        r = pf.int_rate_ss(K, L, A, alpha, delta)
        r2= r3 = r
    c1  = cf.consump1(bvec, w1, nvec)
    c2  = cf.consump2(bvec, r2, w2, nvec)
    c3  = cf.consump3(bvec, r3, w3, nvec)
    mu1 = uf.mar_util(c1, sigma)
    mu2 = uf.mar_util(c2, sigma)
    mu3 = uf.mar_util(c3, sigma)
    error1 = mu1 - beta*(1 + r2)*mu2
    error2 = mu2 - beta*(1 + r3)*mu3
    error  = np.array([error1, error2])
    return error

# derive the steady state equilibrium
bvec_init = np.array([0.1, 0.1])
ss_args = (1, 1, 1, 10000, 1,  beta, alpha, delta, sigma, A, nvec, "SS")
bvec_ss = opt.root(EquiError, bvec_init, args = (ss_args))
print(bvec_ss)
print("Steady State savings: ", bvec_ss.x)
K = af.capital(bvec_ss.x)
L = af.labor(nvec)
w = pf.wage_ss(K, L, A, alpha)
r = pf.int_rate_ss(K, L, A, alpha, delta)
c1 = cf.consump1(bvec_ss.x, w, nvec)
c2 = cf.consump2(bvec_ss.x, r, w, nvec)
c3 = cf.consump3(bvec_ss.x, r, w, nvec)
print("Steady state period 1 consumption: ", c1)
print("Steady state period 2 consumption: ", c2)
print("Steady state period 3 consumption: ", c3)
print("Steady state wage: ", w)
print("Steady state interest rate: ", r)
