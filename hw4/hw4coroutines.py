def tracker(p,limit):
    '''
    Returns the number of odd values
    '''
    assert isinstance(limit, int)
    assert limit>0
    i = 0 
    while True:
        try: 
            x = next(p).seconds  

            if(x%2!=0):
                i = i +1
            if(i<=limit):
                new_limit = yield i
#                 print(new_limit)
#                 print(f'limit is {limit}')
                if new_limit is not None:
                    limit = new_limit 
#                     print(f'limit is {limit}')
            else:
                break
        except StopIteration:
            pass
