def write_chunks_of_five(words,fname):
    '''
        input: list of words and name of the output file
        output: writes list of words in chunks of file to the output file
    '''
    assert isinstance(fname, str)
    assert isinstance(words, list)
    assert all(isinstance(w, str) for w in words)

    text = []
    for i in range(0, len(words), 5):
        text.append(" ".join(words[i:i+5]))
    f = open(fname, 'w')
    f.write("\n".join(text))
    f.close()
