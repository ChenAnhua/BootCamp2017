# -*- coding: utf-8 -*-
"""
This is script defines price functions (wage and interset rate) based on firm
optimization

function input;
K                      : capital
L                      : labor supply
Aval                   : TFP
alpha                  : capital income share
delta                  : period depreciation rate

function output:
w                      : wage
r                      : period (20 year compund) interest rate

"""

def wage (K, L, Aval, alphaval):
    w = (1 - alphaval)*Aval*((K/L)**alphaval)
    return w

def int_rate (K, L, Aval, alphaval, deltaval):
    r = alphaval*Aval*(L/K)**(1-alphaval) - deltaval
    return r
