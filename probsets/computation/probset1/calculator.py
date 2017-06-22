# -*- coding: utf-8 -*-
"""

This script is for problemset 1 standard library 

"""
def sumcal(arg1, arg2):
    result = arg1 + arg2
    return result

def productcal (arg1, arg2):
    result = arg1*arg2
    return result

def sqrtcal (arg):
    result = arg**(0.5)
    return result

if __name__ == "__main__":
    
    print ("This file was executed from the command line or an interpreter.")
else:
    print ("This file was imported.")
