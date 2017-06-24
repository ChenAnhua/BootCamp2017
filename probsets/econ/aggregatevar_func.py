'''

This script is for the aggregate macro variable function labor and capital (L and K)

'''
def capital(bvec):
    K = bvec.sum()
    return K

def labor(nvec):
    L = nvec.sum()
    return L
