def is_string_integer(x):
    ''' Input: character of length 1
        Output: Returns True if the given input
                represents a valid integer in base 10'''
   
    assert(len(x) == 1)
    
    return x.isnumeric()

