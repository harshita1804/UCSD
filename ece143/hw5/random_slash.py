import numpy as np
import random
def gen_rand_slash(m=6,n=6,direction='back'):
    '''
     this function generates an ndarray containing a back or forward slash (1's) with all other 0's according to requirements
    :param: m (length of the row)
    :type : int
    :param: n (length of the column)
    :type : int
    :param: direction ('back' or 'forward' slash)
    :type: str
    '''
    assert isinstance(m,int)
    assert isinstance(n, int)
    assert m>=2 and n>=2
    assert isinstance(direction, str)
    assert direction == 'back' or direction == 'forward'
    
    max_len = min(m,n)
    len_array = random.choice(range(2,max_len+1))
    
    array = np.zeros((m,n))
    
    if direction=='back':
        # start position
        r_pos = random.choice(range(m-len_array+1))
        c_pos = random.choice(range(n-len_array+1))
        for i in range(len_array):
            array[r_pos][c_pos] = 1
            r_pos += 1
            c_pos += 1
    else:
        # start position
        r_pos = random.choice(range(m-len_array+1))
        c_pos = random.choice(range(len_array-1,n))
        for i in range(len_array):
            array[r_pos][c_pos] = 1
            r_pos += 1
            c_pos -= 1
    
    return array
