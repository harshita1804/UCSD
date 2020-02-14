def compute_sum_to_n(x):
    ''' Input: a non-negative integer
        Output: Returns the sum of all non-negative integers upto and including n'''
    assert(isinstance(x, int) == True)
    assert(x>=0)
    
    return sum([i for i in range(0,x+1)])

