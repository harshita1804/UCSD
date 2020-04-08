import string
def input_file_processing(fname):
    '''
    Returns a sentences from the file fname without punctuations and in lower case
    '''
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip(string.punctuation).lower() for x in content]

    return content
    

def encrypt_message(message,fname):
    
    '''
       Given `message`, which is a lowercase string without any punctuation, and `fname` which
       is the name of a text file source for the codebook, generate a sequence of 2-tuples that
       represents the `(line number, word number)` of each word in the message. The output is
       a list of 2-tuples for the entire message. Repeated words in the message should not
       have the same 2-tuple.
       
       :param message: message to encrypt
       :type message: str
       :param fname: filename for source text
       :type fname: str
       :returns: list of 2-tuples
    '''

    assert isinstance(message, str)
    assert isinstance(fname, str)
    assert message.islower()

    from collections import defaultdict
    
    list_of_tuples = []
    
    content = input_file_processing(fname)
    dict_of_words = defaultdict(list)
    
    for line_number, line in enumerate(content):
        for word_number, word in enumerate(line.split()):
            dict_of_words[word].append((line_number, word_number))
 
    message = message.strip(string.punctuation)
    msg_count = {}
    for msg in message.split():
        if msg in msg_count.keys():
            msg_count[msg]+=1
        else:
            msg_count[msg]=1

    assert all(val<=len(dict_of_words[msg]) for val in msg_count.values())
   
    for msg in message.split():
        list_of_tuples.append(dict_of_words[msg].pop(0))
    
    return list_of_tuples

    
def decrypt_message(inlist,fname):
    '''
      Given `inlist`, which is a list of 2-tuples`fname` which is the
      name of a text file source for the codebook, return the encrypted message.
     
      :param message: inlist to decrypt
      :type message: list
      :param fname: filename for source text
      :type fname: str
      :returns: string decrypted message
    '''
    
    assert isinstance(inlist, list)
    assert all(isinstance(i, tuple) for i in inlist)
    assert isinstance(fname, str)
    
    content = input_file_processing(fname)
    text = []
    for tup in inlist:
        x, y = tup
        l = content[x].split()
        
        text.append(l[y])
    
    return ' '.join(text)
