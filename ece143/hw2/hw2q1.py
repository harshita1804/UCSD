from itertools import product

def get_power_of3(x):
    ''' Input: an integer between 1 to 40 which is t be decomposed
        Output: Returns the decomposition of the integer'''
        
    assert(isinstance(x, int))
    assert(40>=x>=1)
    
    A = [-1,0,1]
    combinations = product(A,repeat=4)
    for z in combinations:
        s = z[0]*1 + z[1]*3 + z[2]*9 +z[3]*27
        if(s == x):
            return list(z)


#def get_power_of3(x):
#''' Input: an integer between 1 to 40 which is t be decomposed
#    Output: Returns the decomposition of the integer'''
#assert(isinstance(x, int))
#A = [-1,0,1]
#combinations = list(product(A,repeat=4))
#t = [1,3,9,27]
#for z in combinations:
#    l  = 0
#    for a,b in zip(z,t):
#        l = l + a*b
#    if(l == x):
#        break
#return list(z)
