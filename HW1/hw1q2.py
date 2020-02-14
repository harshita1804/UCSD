def compute_average_word_length(instring,unique=False):
    ''' Input(s): a string and a parameter unique which indicated whether or not duplication is allowed
        Output: Returns the average word length'''
    assert(isinstance(instring, str) == True)
    assert(isinstance(unique, bool) == True)
    instring = instring.lower()
    list_str = instring.split()
    if(unique is True):
        list_str = set(list_str)
    number_of_words = len(list_str)
    number_of_chars = sum(map(lambda x: len(x), list_str))
    return number_of_chars/number_of_words
