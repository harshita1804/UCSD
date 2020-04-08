enter = True
def count_paths(m,n,blocks):
    '''
    Returns the number of connected path in a mxn grid using dfs
    '''
    assert m>0, n>0
    assert (0,0) not in blocks
    assert (m-1, n-1) not in blocks
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(blocks, list)
    assert all(isinstance(i,tuple) for i in blocks)
    assert all(all(isinstance(i, int) for i in t) for t in blocks)
    global enter
    if enter:
        enter = False
    if(m,n) == (1,1):
        return 1
    elif m>0 and n>0:
        valid_m = 0
        valid_n = 0
        if m>1 and (m-2, n-1) not in blocks:
            valid_m = 1
        if n>1 and (m-1, n-2) not in blocks:
            valid_n = 1
            
        if valid_m and valid_n:
            return count_paths(m-1, n, blocks) + count_paths(m, n-1, blocks)
        elif valid_n and not valid_m:
            return count_paths(m, n-1, blocks)
        elif valid_m and not valid_n:
            return count_paths(m-1, n, blocks)
        else:
            return 0
