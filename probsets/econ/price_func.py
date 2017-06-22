# -*- coding: utf-8 -*-
"""
This is script defines price functions (wage and interset rate) based on firm 
optimization

"""

def wage (b2val, b3val, Aval, alphaval):
    w = (1 - alphaval)*Aval*((b2val +b3val)/2)**alphaval
    return w

def int_rate (b2val, b3val, Aval, alphaval, deltaval):
    r = (alphaval)*Aval*(2/(b2val +b3val))**(1-alphaval) - deltaval
    return r


