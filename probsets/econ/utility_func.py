'''

This script is mainly for CRRA utility function and marginal utility function
The utility function is based on price parameters and wealth distributiion (savings)

'''
def mar_util(consumption, sigma):
    mar_util = (consumption)**(-sigma)
    return mar_util
