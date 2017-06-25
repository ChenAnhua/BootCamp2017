'''

This script is for function to derive the error of Euler equation of equilibrium
for both steady state and transitional state

function input:
bvec                  : savings
nvec                  : vector of labor supply
w1                    : period 1 wage
w2                    : period 2 wage
w3                    : period 3 wage
r2                    : period 2 interest rate
r3                    : period 3 interest rate
beta                  : discount factor
alpha                 : capital income share
delta                 : depreciation rate
sigma                 : risk aversion
A                     : TFP
model_choice          : indicator of whether it's a steady state equilibrium

funciton output:
return the error of the Euler function


'''
import numpy as np
import aggregatevar_func as af
import price_func as pf
import consumption_func as cf
import utility_func as uf


def EulerError(bvec, *args):
    b2val, b3val = bvec
    w1, w2, w3, r2, r3, beta, alpha, delta, sigma, A, nvec, model_choice = args
    K = af.capital(bvec)
    L = af.capital(nvec)
    if (model_choice == "SS"):
        w = pf.wage(K, L, A, alpha)
        w1= w2 = w3 = w
        r = pf.int_rate(K, L, A, alpha, delta)
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
