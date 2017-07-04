'''

This script defines the consumption functions
notice: all the periods here are in terms of individual perspectives

function input:
bvec                  : savings
nvec                  : vector of labor supply
w1                    : period 1 wage
w2                    : period 2 wage
w3                    : period 3 wage
r2                    : period 2 interest rate
r3                    : period 3 interest rate

function output:
consump               : consumption

'''
def consump1(bvec, w1, nvec):
    b2val, b3val = bvec
    consump = (w1*nvec[0] - b2val)
    return consump

def consump2(bvec, r2, w2, nvec):
    b2val, b3val = bvec
    consump = ((1 + r2)*b2val + w2*nvec[1] - b3val)
    return consump

def consump3(bvec, r3, w3, nvec):
    b2val, b3val = bvec
    consump = ((1 + r3)*b3val + w3*nvec[2])
    return consump
