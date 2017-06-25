'''

This script is mainly for CRRA utility function and marginal utility function
The utility function is based on consumption

funciton input:
consumption                        : consumption drived from consumption_func
sigma                              : risk aversion

function output:
mar_util                           : marginal utility

'''
def mar_util(consumption, sigma):
    mar_util = (consumption)**(-sigma)
    return mar_util
