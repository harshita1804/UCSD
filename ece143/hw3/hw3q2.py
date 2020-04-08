import calendar
def number_of_days(year,month):
    '''Returns the number of days in the given month of the given year.
    
    Parameters
    ----------
    year: year in the calendar.
    month: month between 1-12.
    
    Returns
    -------
    Int
        Number of days in that month of the year.
        
    Examples
    --------
       number_of_days(2020,2)
       
       returns: 29
       
    '''
    
    assert year>=0
    assert 12>= month >=1
    assert isinstance(year, int)
    assert isinstance(month, int)
    
    days = calendar.monthrange(year, month)
    
    return days[1]



def number_of_leap_years(year1,year2):
    
    '''Returns the number of leap years between given years.
    
    Parameters
    ----------
    year1: year in the calendar.
    year2: year in calendar.
    
    Returns
    -------
    Int
        Number of leap years between year1 and year2.
        
    Examples
    --------
       number_of_leap_years(2012,2016)
       
       returns: 2
       
    '''
    
    assert year1>=0
    assert year2>=0
    assert year2>=year1
    
    num_leap_years = 0
    for year in range(year1, year2+1):
        if(number_of_days(year,2)==29):
            num_leap_years+=1
        
    return num_leap_years

def get_day_of_week(year,month,day):
    
    '''Returns what day of the week is represented by the given date.
    
    Parameters
    ----------
    year: year in the calendar.
    month: month in calendar.
    day: day in the calendar. 
    Returns
    -------
    String
        Day of the week represented by the given date.
        
    Examples
    --------
       get_day_of_week(2020, 1, 22)
       
       returns: Wednesday
       
    '''
    assert year>=0
    assert 12>= month >=1
    assert 31>=day>=1
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day, int)
    
    days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
    return days[calendar.weekday(year,month,day)]
