def map_bitstring(x):
    
    '''Returns a dictionary of mappings between the list of bitstrings and the 
       numbers 0 or 1.
       0 if the number of 0 in x[i]> number of 1 in x[i], else 1. 

    Parameters
    ----------
    x: list of bitstrings.
    Returns
    -------
    Dictionary
        A dictionary of mappings between the number of bistrings and the number         of 0 
        present in the bitstring.

    Examples
    --------
       >>> x= ['100', '100', '110', '010', '111', '000', '110', '010', '011',
               '000']
       >>> map_bitstring(x) 
           {'100': 0, '110': 1, '010': 0, '111': 1, '000': 0, '011': 1} 

     '''
    
    
    assert isinstance(x, list)
    assert all(isinstance(d, str) for d in x)
    mapping = []
    for bstring in x:
        length = len(bstring)
        numberOfOnes = bstring.count('1')
        if(length - numberOfOnes>numberOfOnes):
            mapping.append(0)
        else:
            mapping.append(1)
    return dict(zip(x, mapping))
    
