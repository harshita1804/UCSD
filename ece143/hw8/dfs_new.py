def count_paths(m,n,blocks):
    '''
    Returns the number of connected path in a mxn grid using dfs
    '''
    assert m>1, n>1
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert isinstance(blocks, list)
    assert all(isinstance(i,tuple) for i in blocks)
    assert all(all(isinstance(i, int) for i in t) for t in blocks)
    visited = []
    def dfs(i,j):
        if 0 <= i < m and 0 <= j < n and (i,j) not in visited :
            if ((i,j) in blocks and (i,j) != (0,0)) or (i,j) == (m-1, n-1) :
                return 1
            dfs(i+1, j), dfs(i, j+1) 
            visited.append((i,j))
        return 0
    return sum(dfs(i,j) for i in range(m) for j in range(n))
