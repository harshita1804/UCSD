import pandas as pd
def split_count(x):
    '''
     Returns a dataframe object created from the input which is a series object 
    '''
    assert type(x) is pd.Series
    assert len(x)>0
    
    split_dict = {}
    for i in x:
        for key_of_dict in i.split(','):
            key_of_dict = key_of_dict.strip()
            if key_of_dict in split_dict.keys() :
                split_dict[key_of_dict] +=1
            else:
                split_dict[key_of_dict] =1
    df = pd.DataFrame.from_dict(split_dict, orient='index', columns = ['count'])
    
    return df
    
