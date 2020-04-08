def fibonacci(n):
    '''Yields the next number in fibonacci series.
    
    Parameters
    ----------
    n: number of fibonacci number to be generated.
    
    Returns
    -------
    List
        A list of first n fibonacci numbers.
        
    Examples
    --------
       list(fibonacci(10))
       
       returns the list:
       
       [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
       
    '''
    
    assert isinstance(n, int)
    a = 0
    b = 1
    yield(1)
    for i in range (1,n):
        yield(a+b)
        t = a+b
        a = b
        b = t
