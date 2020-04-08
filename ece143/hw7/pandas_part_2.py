import pandas as pd

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
    
def count_month_yr(x):
    '''
     Returns a dataframe which has counts of values of the column 'month-yr'
    '''
    assert type(x) is pd.DataFrame
    assert len(x)>0

    new_df = add_month_yr(x)

    return pd.DataFrame(new_df['month-yr'].value_counts())
