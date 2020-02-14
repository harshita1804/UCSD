def map_bitstring(x):
    
    '''Returns a dictionary of mappings between the list of bitstrings and the numbers 0 or 1.
       0 if the number of 0 in x[i]> number of 1 in x[i], else 1. 

    Parameters
    ----------
    x: list of bitstrings.
    Returns
    -------
    Dictionary
        A dictionary of mappings between the number of bistrings and the number of 0 
        present in the bitstring.

    Examples
    --------
       >>> x= ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']
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
    

def gather_values(x):
    '''
    Returns a dictionary of strings as keys with values in form of a list that is formed using
    map_birstrings function

    Parameters
    ----------
    x: list of bitstrings.
    Returns
    -------
    Dictionary
        A dictionary of strings as keys with values in form of a list that is formed using
        map_birstrings function

    Examples
    --------
       >>> x=get_sample(nbits=2,prob={'00':1/4,'01':1/4,'10':1/4,'11':1/4},n=20)
       >>> print(x)
         ['10', '11', '01', '00', '10', '00', '00', '11', '10', '00', '00', '01', 
         '01', '11', '10', '00', '11', '10', '11', '11']
         
         So when x is as above, our function returns, 
         
         {'10': [1, 1, 1, 1, 1],
          '11': [1, 1, 1, 1, 1, 1],        
          '01': [1, 1, 1],                 
           '00': [0, 0, 0, 0, 0, 0]}    
    '''
    assert isinstance(x, list)
    assert all(isinstance(d, str) for d in x)
    
    dict_of_mappings = map_bitstring(x)
    from collections import defaultdict
    d_dict = defaultdict(list)
    for i in x:
        d_dict[i].append(dict_of_mappings[i])
    return d_dict
    

def threshold_values(seq,threshold=1):
    '''
    Returns a dictionary of strings as keys with values in form of a list that is formed using
    gather_values function

    Parameters
    ----------
    seq: list of bitstrings.
    threshold: the threshold for setting zero and one
    Returns
    -------
    Dictionary
        A dictionary of strings as keys with values that are either 0 or 1 depending on the threshold

    Examples
    --------
       for the dict generated from gather_values, we get,
           {'10': [1, 1, 1, 1, 1],
            '11': [1, 1, 1, 1, 1, 1],  
            '01': [1, 1, 1],  
            '00': [0, 0, 0, 0, 0, 0]} 
            
            threshold_values gives:
             {'10': 1,
              '11': 1,  
              '01': 0,  
              '00': 0}  
    '''
    assert isinstance(seq, list)
    assert all(isinstance(d, str) for d in seq)
    assert isinstance(threshold, int)
    assert threshold>=0
    
    z = gather_values(seq)
    
    for k, v in z.items():
        z[k] = sum(v)
    from collections import Counter

    k = Counter(z)
    s = [key[0] for key in k.most_common(threshold)]
    
    for i in z:
        if i in s:
            z[i] = 1
        else:
            z[i] = 0
    return dict(sorted(z.items(), key = lambda x: x))
