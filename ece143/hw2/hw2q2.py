def write_columns(data,fname):
    '''
    Input: data and filename
    Output: Writes data_value, data_value**2, (data_value + data_value**2)/3) onto the given file fname for every data_value
    '''
    assert isinstance(fname, str)
    assert isinstance(data, list)
    assert all(isinstance(d,(int, float)) for d in data)
    s = []
    for data_value in data:
        s.append('%.2f'%data_value +',' + '%.2f'%(data_value**2) + ','+'%.2f'%((data_value+data_value**2)/3))
 
   f = open(fname, 'w')
   f.write("\n".join(s))
   f.close()
