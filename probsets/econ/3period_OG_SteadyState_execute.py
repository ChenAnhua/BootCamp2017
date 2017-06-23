# -*- coding: utf-8 -*-
'''
This script is modeling the steady state 3-period overlapping generation model

'''
#import pacakges
import numpy as np
import scipy.optimize as opt

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


'''
yrs_live    = 60
S           = 3
alpha       = 0.3
beta_annual = 0.06
beta        = beta_annual**(yrs_live/S) 
nvac        = np.array([1.0, 1.0, 0.2])
A           = 1.0
delta_annual= 0.05
delta       = 1-(1-delta_annual)**(yrs_live/S)

# Steady state equilibrium

def SSequi(b2val, b3val, args):
    beta, alpha, delta, A, nvac = args
    print(args)
    
    

'''
Demo by Rick Evanss

import numpy as np
import scipy.optimize as opt
## OG model 3 step
# first parameter
yrs_live = 60
S = 3
alpha= 0.3 # between 0.27 and 0.4, capital share of income
beta_annual = 0.06
beta = beta_annual**(yrs_live/S)


 # HH parameters
nvac = np.array([1.0, 1.0, 0.2])
A = 1.0
delta_annual = 0.05  # between 3 and 7 percent
delta = 1- (1- delta_annual)**(yrs_live/S)

def rfunc():
    return
def wfunc():
    return





# steady state equilibrium
def stuff(b2b3val, arg):
    beta = arg # beta, sigma, alpha, A, delta, nvac
    r = rfunc
    w = wfunc
    muc1 = (b2b3val)
    muc2 = (b2b3va)
    error1  = muc1 - beta*(1+r)*muc2
                          
    return(error)                  

b2bar, b3bar = opt.root()

'''



