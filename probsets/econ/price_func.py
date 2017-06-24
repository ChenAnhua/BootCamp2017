# -*- coding: utf-8 -*-
"""
This is script defines steady state price functions (wage and interset rate) based on firm
optimization

"""

def wage_ss (K, L, Aval, alphaval):
    w = (1 - alphaval)*Aval*((K/L)**alphaval)
    return w

def int_rate_ss (K, L, Aval, alphaval, deltaval):
    r = alphaval*Aval*(L/K)**(1-alphaval) - deltaval
    return r
