def get_trapped_water(seq):
    '''
    Returns the amount of water trapped 
    '''
    assert isinstance(seq, list)
    assert all(isinstance(i, int) for i in seq)
    assert all(i>=0 for i in seq)
    
    left_max = 0
    right_max = 0
    left_idx = 0
    right_idx = len(seq)-1
    ans = 0
    while(left_idx<right_idx):
        if(seq[left_idx]<seq[right_idx]):
            if(seq[left_idx]>=left_max):
                left_max = seq[left_idx]
            else:
                ans += left_max - seq[left_idx]
            left_idx = left_idx + 1
        else:
            if(seq[right_idx]>=right_max):
                right_max = seq[right_idx]
            else:
                ans += right_max - seq[right_idx]
            right_idx = right_idx - 1
    return ans
