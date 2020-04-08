import pandas as pd
import calendar

def add_month_yr(x):
    '''
     Returns dataframe x with an additional column month_yr added to it
    '''
    assert type(x) is pd.DataFrame 
    assert len(x)>0
    assert all(isinstance(i, str)for i in x['Timestamp'])
    
    col_to_add = pd.to_datetime(x['Timestamp'])
    year = col_to_add.dt.to_period('Y')
    month = col_to_add.dt.strftime('%b')

    x['month-yr'] = month + '-' + year.map(str)
    
    return x

def fix_categorical(x):
    '''
     Returns a dataframe 
    '''
    assert type(x) is pd.DataFrame
    assert len(x)>0
    assert 'month-yr' in x.columns
    assert 'Timestamp' in x.columns
    
    month_list = list(calendar.month_abbr)
    #print(month_list)
    month_yr_unique = list(set(x['month-yr']))
    #print(month_yr_unique)
    sort_month_yr =  lambda x:x.split('-')[1]+'{0:02d}'.format(month_list.index(x.split('-')[0]))
    month_yr_unique.sort(key = sort_month_yr)
    cats = pd.CategoricalDtype(month_yr_unique, ordered = True) 
    x['month-yr'] = x['month-yr'].astype({'month-yr':cats})
    return x
    
