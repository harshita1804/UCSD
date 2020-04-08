import numpy as np
import itertools as it
def solvefrob(coefs,b):
    '''
    Returns a set of possible values of x for the equation
    coefs*x = b
    '''
    assert isinstance(coefs,list)
    assert all(isinstance(i, int) for i in coefs)
    assert all(i>0 for i in coefs)
    assert isinstance(b,int)
    assert b>0

    ans = []
    new_per = list(it.product(range(b+1), repeat = len(coefs)))
    coefs_new = np.tile(coefs,(len(new_per),1))
    x = np.where(np.sum(new_per*coefs_new, axis = 1)==b)
    ans = []
    for i in x[0]:
        ans.append(tuple(new_per[i]))
    return ans
