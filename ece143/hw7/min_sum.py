import itertools as it
import math

def get_min_split(seq):
    
    '''
     Returns the min split
    '''
    
    assert isinstance(seq, list)
    assert all(isinstance(i, (int, float)) for i in seq)
    assert len(set(seq)) == len(seq)
    assert all(i>0 for i in seq)
    
    table_lookup = []
    
    for i in range(1, int(math.floor(len(seq)/2))+1):
        for subset in it.combinations(seq, i):
            table_lookup.append((subset, abs(sum(seq) - 2*sum(subset))))
    
    minimum_diff = min([z[1] for z in table_lookup])
    
    return [(list(z[0]), list(set(seq)- set(z[0]))) for z in table_lookup if z[1] == minimum_diff]
