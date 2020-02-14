import random
def get_sample(nbits=3,prob=None,n=1):
    
    '''Returns a list n of random samples from a finite probability mass function 
       defined by a dictionary with keys defined by a specified number of bits.

    Parameters
    ----------
    nbits: number of bits.
    prob: dict of strings and the probability of drawing the corresponding string.
    n: number of random samples to be returned from the given dict.

    Returns
    -------
    List
        A lists n random samples from the given dict.

    Examples
    --------
       get_sample(nbits=3,prob=p,n=4)
       ['101', '000', '001', '100'] 
     '''
    
    assert n>=0
    assert nbits>=1
    assert sum([v for v in prob.values()]) ==1
    
    return random.choices(list(prob.keys()), k = n)
    
