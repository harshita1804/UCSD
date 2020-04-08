#multinomial sampler
import random
import math
def multinomial_sample(n,p,k=1):
    '''
    Return samples from a multinomial distribution.
                                                                             
    n:= number of trials
    p:= list of probabilities
    k:= number of desired samples
    '''
    assert isinstance(n, int)
    assert isinstance(k, int)
    assert all(i>=0 for i in p)
    assert all(isinstance(i, float) or isinstance(i,int) for i in p)
    assert math.isclose(sum(p),1)
    
    ans = []
    for val in range(k):
        temp = random.choices(range(len(p)), p, k = n)
        num = [0]*len(p)
        for i in temp:
            num[i] += 1
        ans.append(num)
    return ans  
