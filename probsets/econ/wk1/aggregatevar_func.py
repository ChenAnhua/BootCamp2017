'''

This script is for the aggregate macro variable function labor and capital (L and K)

Function input:
bvec                : vector of savings
nvec                : vector of labor supply

Function output:
K                   : capital
L                   : labor supply

'''
def capital(bvec):
    K = bvec.sum()
    return K

def labor(nvec):
    L = nvec.sum()
    return L
