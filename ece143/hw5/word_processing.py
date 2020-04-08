def get_average_word_length(words):
    
    '''
    Returns the average length of words that are in the input list. 

    Parameters
    ----------
    words: list of strings.
    Returns
    -------
    Float
        A floating point number is returned which represents the average length         of the words contained in the input list.

    Examples
    --------
       >>> x= ['the', 'and', 'if', 'no']
       >>> get_average_word_length(x) 
           2.5
    '''
    
    assert isinstance(words, list) 
    assert all(isinstance(d, str) for d in words)
    assert words is not None
    
    number_of_words = len(words)
    number_of_chars = sum(map(lambda x: len(x), words))
    
    return number_of_chars/number_of_words

def get_longest_word(words):
    '''
    Returns the longest word in the input list. 

    Parameters
    ----------
    words: list of strings.
    Returns
    -------
    String
        The longest word in the list.

    Examples
    --------
       >>> x= ['the', 'if', 'no']
       >>> get_longest_word(x) 
           the
    '''
    
    assert isinstance(words, list) 
    assert all(isinstance(d, str) for d in words)
    assert words is not None
    
    max_len = 0
    longest_word = max(words, key = lambda x:len(x))
    
    return longest_word

def get_longest_words_startswith(words,start):
    '''
    Returns the longest word in the input list that starts with the 
    character specified in start. 

    Parameters
    ----------
    words: list of strings.
    start: the letter with which the string starts
    Returns
    -------
    String
        The longest word in the list starts with the 
        character specified in start.

    Examples
    --------
       >>> x= ['the', 'if', 'no']
       >>> get_longest_word(x, 't') 
           the
    '''
    
    assert isinstance(words, list) 
    assert all(isinstance(d, str) for d in words)
    assert isinstance(start, str)
    assert start is not None
    assert words is not None
    
    words_start = [x for x in words if x.startswith(start)]
    longest_words_startswith = get_longest_word(words_start)
    
    return longest_words_startswith

def get_most_common_start(words):
    '''
    Returns the alphabet with which most of the words in the input list start. 

    Parameters
    ----------
    words: list of strings.
    Returns
    -------
    String
        The alphabet with which most of the words in the input list start.

    Examples
    --------
       >>> x= ['the','that', 'if', 'no']
       >>> get_most_common_start(x) 
           t
    '''
    assert isinstance(words, list) 
    assert all(isinstance(d, str) for d in words)
    assert words is not None
    
    alphabets = ['a','b', 'c','d','e', 'f','g','h','i','j','k', 'l','m', 'n','o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    max_length = 0
    ans = ''
    for alpha in alphabets:
        words_start = [x for x in words if x.lower().startswith(alpha)]
        if(len(words_start)>max_length):
            max_length = len(words_start)
            ans = alpha
        
    return ans

def get_most_common_end(words):
    
    '''
    Returns the alphabet with which most of the words in the input list end. 

    Parameters
    ----------
    words: list of strings.
    Returns
    -------
    String
        The alphabet with which most of the words in the input list end.

    Examples
    --------
       >>> x= ['tint','that', 'if', 'no']
       >>> get_most_common_end(x) 
           t
    '''
    
    assert isinstance(words, list) 
    assert all(isinstance(d, str) for d in words)
    assert words is not None
    
    alphabets = ['a','b', 'c','d','e', 'f','g','h','i','j','k', 'l','m', 'n','o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    max_length = 0
    ans = ''
    for alpha in alphabets:
        words_start = [x for x in words if x.lower().endswith(alpha)]
        if(len(words_start)>max_length):
            max_length = len(words_start)
            ans = alpha
        
    return ans 
