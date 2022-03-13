import numpy as np 

def sum_prod_diags(matrix):
    m, l = np.array(matrix), len(matrix)
    return sum([np.prod( np.diagonal(m,r)) for r in range(-l+1,l)]) - sum([np.prod( np.diagonal(np.fliplr(m),r)) for r in range(-l+1,l)])